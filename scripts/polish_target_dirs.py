#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""润色 redis / MySQL / MQ / ES / Spring / SpringCloud / 分布式 等目录下的 Markdown。"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from polish_all_md import (  # noqa: E402
    KV_RE,
    apply_global_replacements,
    dedupe_blank,
    ensure_h1,
    normalize_line_indent,
    promote_duplicate_h2,
)

TARGET_DIRS = [
    "redis",
    "MySQL",
    "RabbitMq",
    "ElasticSearch",
    "Spring",
    "springBoot",
    "SpringCloud",
    "分布式",
]

LIGHT_TOUCH_ONLY = {"分布式锁.md", "GFS.md", "分布式基础理论.md"}

EXTRA_REPLACEMENTS: list[tuple[str, str]] = [
    ("ROB和AOF", "RDB 和 AOF"),
    ("支持ROB和AOF", "支持 RDB 和 AOF"),
    ("文件时间处理器", "文件事件处理器"),
    ("的事件处理器处理时间", "的事件处理器处理事件"),
    ("Redis最大位512m", "Redis 最大为 512MB"),
    ("最大位512m", "最大为 512MB"),
    ("用redis称为分布式缓存", "用 Redis 作为分布式缓存"),
    ("MUITI命令", "MULTI 命令"),
    ("SortedSet和LIst", "SortedSet 和 List"),
    ("LIst基于", "List 基于"),
    ("LIst不能", "List 不能"),
    ("OlogN", "O(log N)"),
    ("主流的出发RDB", "主流的触发 RDB"),
    ("在指目录中", "在指定目录中"),
    ("Redisclust", "Redis Cluster"),
    ("reds会返回", "Redis 会返回"),
    ("每秒一次的评论", "每秒一次的频率"),
    ("Redis Cluste ", "Redis Cluster "),
    ("内存储存", "内存存储"),
    ("列队数据", "对列数据"),
    ("lombook", "Lombok"),
    ("ikun分词器", "IK 分词器"),
]

ERRONEOUS_CMD_H2 = re.compile(r"^##\s+(z[A-Za-z].*)$")
ORPHAN_SECTION = re.compile(r"^-\s+\*\*([^*]+)\*\*\s*$")


def apply_extra_replacements(text: str) -> str:
    for old, new in EXTRA_REPLACEMENTS:
        text = text.replace(old, new)
    return apply_global_replacements(text)


def fix_erroneous_command_headers(lines: list[str]) -> list[str]:
    out: list[str] = []
    for line in lines:
        m = ERRONEOUS_CMD_H2.match(line.strip())
        out.append(m.group(1) if m else line)
    return out


def promote_orphan_section_bullets(lines: list[str]) -> list[str]:
    out: list[str] = []
    for i, line in enumerate(lines):
        m = ORPHAN_SECTION.match(line.strip())
        if m:
            title = m.group(1).strip()
            if 2 < len(title) < 45:
                prev = lines[i - 1].strip() if i > 0 else ""
                if prev.startswith("##") or not prev:
                    out.append(f"## {title}")
                    continue
        out.append(line)
    return out


def count_h2(lines: list[str]) -> int:
    return sum(1 for ln in lines if re.match(r"^##\s+", ln) and not ln.startswith("###"))


def structure_long_unheaded(lines: list[str], min_lines: int = 80) -> list[str]:
    non_empty = [l for l in lines if l.strip() and not l.strip().startswith("#")]
    if len(non_empty) < min_lines or count_h2(lines) >= 3:
        return lines
    out: list[str] = []
    promoted = 0
    topic_re = re.compile(r"^(\s{0,2})-\s*\*\*([^*]+)\*\*\s*$")
    for i, line in enumerate(lines):
        if line.strip().startswith("#"):
            out.append(line)
            continue
        m = topic_re.match(line.rstrip())
        if m and len(m.group(2).strip()) <= 40:
            prev = lines[i - 1].strip() if i > 0 else ""
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if (not prev or prev.startswith("#")) and (
                not nxt.strip() or nxt.startswith("  ") or nxt.startswith("-")
            ):
                out.append(f"## {m.group(2).strip().rstrip('?').rstrip('？')}")
                promoted += 1
                continue
        out.append(line)
    return out if promoted >= 2 else lines


def extract_points(lines: list[str]) -> list[str]:
    points: list[str] = []
    for line in lines:
        m = KV_RE.match(line)
        if m:
            key, val = m.group(2).strip(), m.group(3).strip()
            if key and len(key) < 50:
                points.append(f"- **{key}**" + (f"：{val[:100]}" if val else ""))
        elif re.match(r"^##\s+", line.strip()):
            t = line.strip()[3:].strip()
            if t not in ("面试要点", "小结") and len(t) < 35:
                points.append(f"- {t}")
        if len(points) >= 6:
            break
    return points


def add_footer(lines: list[str], path: Path) -> list[str]:
    body = "\n".join(lines)
    if any(x in body for x in ("## 面试要点", "## 小结", "## 面试一句话")):
        return lines
    non_h = [l for l in lines if l.strip() and not l.strip().startswith("#")]
    if len(non_h) < 3:
        return lines
    points = extract_points(lines)
    if len(points) < 2:
        for line in lines:
            if line.strip().startswith("- ") and len(line.strip()) > 6:
                points.append(line.strip())
            if len(points) >= 5:
                break
    if len(points) < 2:
        return lines
    section = "## 小结" if "总结" in path.stem else "## 面试要点"
    return lines + ["", section, ""] + points[:6]


def polish_content(text: str, path: Path, light: bool) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = apply_extra_replacements(text)
    lines = [normalize_line_indent(ln) for ln in text.split("\n")]
    lines = ensure_h1(lines, path.stem)
    lines = fix_erroneous_command_headers(lines)
    lines = promote_orphan_section_bullets(lines)
    if not light:
        lines = structure_long_unheaded(lines)
    lines = promote_duplicate_h2(lines)
    lines = add_footer(lines, path)
    lines = dedupe_blank(lines)
    return "\n".join(lines) + "\n"


def collect_files() -> list[Path]:
    files: list[Path] = []
    for name in TARGET_DIRS:
        base = ROOT / name
        if base.is_dir():
            files.extend(base.rglob("*.md"))
    return sorted(set(files))


def main() -> None:
    files = collect_files()
    modified: list[str] = []
    for path in files:
        original = path.read_text(encoding="utf-8", errors="replace")
        light = path.name in LIGHT_TOUCH_ONLY
        new = polish_content(original, path, light)
        if new != original:
            path.write_text(new, encoding="utf-8")
            modified.append(str(path.relative_to(ROOT)).replace("\\", "/"))
    print(f"Modified {len(modified)} / {len(files)} files")
    for name in modified:
        print(name)


if __name__ == "__main__":
    main()
