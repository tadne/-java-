#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量润色仓库内所有 Markdown 笔记（安全替换 + 结构整理）。"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".idea", "scripts", "__pycache__"}
SKIP_FILES = {"学习变更说明.md"}  # 单独维护

# 已深度人工重写的文件，仅做全局错别字替换，不再改结构
LIGHT_TOUCH_ONLY = {
    "volatile关键字和能否保证有序性.md",
    "SynchronizeMap和ConcurentMap的区别.md",
    "ConcurrentHashMap详细.md",
    "简述JVM的内存模型.md",
    "说说ThreadLocal原理.md",
    "Java的四种引用,强弱软虚.md",
    "HashMap的长度为什么是2的n次.md",
    "有没有可能两个不相等对象有相同hashcode.md",
    "什么是JVM,为什么java是无关平台的语言.md",
    "MinorGC和FullGC.md",
    "Spring解决循环依赖.md",
    "分布式锁.md",
    "常用线程池.md",
    "元空间代替永久代.md",
    "GFS.md",
    "分布式基础理论.md",
}

GLOBAL_REPLACEMENTS: list[tuple[str, str]] = [
    ("你好，这是Bing。我很高兴你对Java编程感兴趣。😊", ""),
    ("你好，这是Bing", ""),
    ("村出纳", "存储"),
    ("SoftRefef=rence", "SoftReference"),
    ("softReference", "SoftReference"),
    ("finaliz()", "finalize()"),
    ("销毁性能", "消耗性能"),
    ("无关平台", "跨平台"),
    ("JDK 9 及以上版本中叫做元空间", "JDK 8 及以上版本中叫做元空间"),
    ("JDK 9+ 及以上", "JDK 8+"),
    ("在 JDK 9 及以上版本", "在 JDK 8 及以上版本"),
    ("-XX**：", "-XX:"),
    ("del',ARGV[1]", "del', KEYS[1]"),
    ("return redis.call('del',ARGV[1])", "return redis.call('del', KEYS[1])"),
    ("CHM 支持 null 作为值", "CHM 键值均不允许 null"),
    ("支持null作为值", "不允许 null 键值"),
    ("快照（snapshot）", "弱一致性迭代"),
    ("HashMap 会缩容", "HashMap 只扩容不缩容"),
]


def normalize_line_indent(line: str) -> str:
    m = re.match(r"^(\t+)(.*)$", line)
    if m:
        return "  " * len(m.group(1)) + m.group(2)
    return line

SECTION_HEADING_RE = re.compile(
    r"^(#{1,6})\s*(.+)$"
)
KV_RE = re.compile(r"^(\s*)-\s*\*\*(.+?)\*\*[：:]\s*(.*)$")


def apply_global_replacements(text: str) -> str:
    for old, new in GLOBAL_REPLACEMENTS:
        text = text.replace(old, new)
    return text


def ensure_h1(lines: list[str], title: str) -> list[str]:
    for line in lines:
        if line.strip():
            if line.strip().startswith("# "):
                return lines
            break
    return [f"# {title}", ""] + lines


def dedupe_blank(lines: list[str]) -> list[str]:
    out: list[str] = []
    prev_blank = False
    for line in lines:
        blank = not line.strip()
        if blank and prev_blank:
            continue
        out.append(line.rstrip())
        prev_blank = blank
    while out and not out[-1].strip():
        out.pop()
    return out


def promote_duplicate_h2(lines: list[str]) -> list[str]:
    """连续重复的 ## 标题只保留一个。"""
    out: list[str] = []
    prev_h2 = None
    for line in lines:
        m = re.match(r"^##\s+(.+)$", line.strip())
        if m:
            h = m.group(1).strip()
            if h == prev_h2:
                continue
            prev_h2 = h
        else:
            if line.strip():
                prev_h2 = None
        out.append(line)
    return out


def add_interview_footer(lines: list[str], title: str) -> list[str]:
    body = "\n".join(lines)
    if "## 面试要点" in body or "## 小结" in body or "面试一句话" in body:
        return lines
    non_empty = [l for l in lines if l.strip() and not l.strip().startswith("#")]
    if len(non_empty) > 45:
        return lines
    # 从 **关键词** 行提取要点
    points: list[str] = []
    for line in lines:
        m = KV_RE.match(line)
        if m:
            key, val = m.group(2).strip(), m.group(3).strip()
            if key and len(key) < 40:
                points.append(f"- **{key}**" + (f"：{val[:80]}" if val else ""))
        if len(points) >= 5:
            break
    if len(points) < 2:
        return lines
    return lines + ["", "## 面试要点", ""] + points[:5]


def polish_content(text: str, title: str, light: bool) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = apply_global_replacements(text)
    lines = [normalize_line_indent(ln) for ln in text.split("\n")]
    lines = ensure_h1(lines, title)
    lines = dedupe_blank(lines)
    lines = promote_duplicate_h2(lines)
    if not light:
        lines = add_interview_footer(lines, title)
    lines = dedupe_blank(lines)
    return "\n".join(lines) + "\n"


def collect_md_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if any(p in SKIP_DIRS for p in path.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        files.append(path)
    return sorted(files)


def main() -> None:
    updated = 0
    for path in collect_md_files():
        original = path.read_text(encoding="utf-8", errors="replace")
        light = path.name in LIGHT_TOUCH_ONLY
        new = polish_content(original, path.stem, light)
        if new != original:
            path.write_text(new, encoding="utf-8")
            updated += 1
    print(f"Polished {updated} / {len(collect_md_files())} markdown files.")


if __name__ == "__main__":
    main()
