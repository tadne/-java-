#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""润色指定面试题目录下的 Markdown：纠错、结构化、补全「面试一句话」。"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TARGET_DIRS = [
    ROOT / "面试题" / "Java基础",
    ROOT / "面试题" / "操作系统",
    ROOT / "面试题" / "计算机网络",
    ROOT / "面试题" / "面经",
    ROOT / "面试题" / "项目",
    ROOT / "计算机网络",
]

SKIP_FILES = {
    "ConcurrentHashMap详细.md",
    "HashMap的长度为什么是2的n次.md",
    "Java的四种引用,强弱软虚.md",
    "有没有可能两个不相等对象有相同hashcode.md",
}

# 计算机网络：已有较好结构则仅做轻量替换
NETWORK_LIGHT_ONLY = True

GLOBAL_REPLACEMENTS: list[tuple[str, str]] = [
    ("你好，这是Bing。我很高兴你对Java编程感兴趣。😊", ""),
    ("你好，这是Bing", ""),
    ("村出纳", "存储"),
    ("SoftRefef=rence", "SoftReference"),
    ("无关平台", "跨平台"),
    ("HashMap 会缩容", "HashMap 只扩容不缩容"),
    ("CHM 支持 null 作为值", "CHM 键值均不允许 null"),
    ("ConcurrentHashMap和HashMap都可存储空键或空值", "仅 HashMap 允许 null 键/值；CHM 键值均不可为 null"),
    ("都允许key和value为null", "仅 HashMap 允许 null 键/值（CHM 不允许）"),
    ("采用分段锁机制来保证线程安全", "JDK 8+ 用 CAS 占空桶 + synchronized 锁桶头保证线程安全"),
    ("ConcurrentHashMap使用分段锁", "JDK 8+ ConcurrentHashMap 使用桶级 synchronized/CAS（JDK 7 为 Segment 分段锁）"),
    ("树化阈值.*7", "树化阈值 ≥8"),
    ("退化.*5", "退化阈值 ≤6"),
    ("第四次回收", "第四次挥手"),
    ("​", ""),
]

FACTUAL_PATTERNS: list[tuple[re.Pattern[str], str]] = []

ONE_LINERS: dict[str, str] = {
    "ConcurrentHashMap与HashMap异同": "HashMap 非线程安全且可 null；CHM 线程安全、不可 null，JDK8 桶锁+CAS。",
    "HashMap和HashTable区别": "HashMap 快且可 null 非线程安全；Hashtable 全表 synchronized 已过时，并发用 CHM。",
    "equals和==的区别": "== 比基本类型值或引用地址；equals 默认同地址，重写后比逻辑相等。",
    "hashcode的作用": "配合 equals：相等对象 hash 必同；用于 HashMap 等定位桶，冲突靠 equals 链式比对。",
    "进程和线程的区别": "进程是资源分配单位，线程是 CPU 调度单位；线程更轻、切换开销更小。",
    "TCP三次握手": "SYN→SYN+ACK→ACK 共三步，双方确认 seq/ack 后进入 ESTABLISHED。",
    "TCP四次挥手": "FIN/ACK 四次关闭全双工连接，主动方常经历 TIME_WAIT。",
}


def collect_files() -> list[Path]:
    seen: set[Path] = set()
    out: list[Path] = []
    for d in TARGET_DIRS:
        if not d.is_dir():
            continue
        for p in sorted(d.rglob("*.md")):
            rp = p.resolve()
            if rp in seen or p.name in SKIP_FILES:
                continue
            seen.add(rp)
            out.append(p)
    return out


def apply_global(text: str) -> str:
    for old, new in GLOBAL_REPLACEMENTS:
        text = text.replace(old, new)
    for pat, repl in FACTUAL_PATTERNS:
        text = pat.sub(repl, text)
    return text


def normalize_indent(line: str) -> str:
    m = re.match(r"^(\t+)(.*)$", line)
    if m:
        return "  " * len(m.group(1)) + m.group(2)
    return line


def strip_bad_interview_section(lines: list[str]) -> list[str]:
    """删除自动生成的劣质「## 面试要点」块。"""
    out: list[str] = []
    i = 0
    while i < len(lines):
        if re.match(r"^##\s+面试要点\s*$", lines[i].strip()):
            j = i + 1
            while j < len(lines) and not re.match(r"^##\s+", lines[j]):
                j += 1
            i = j
            continue
        out.append(lines[i])
        i += 1
    return out


def rename_summary_footer(lines: list[str]) -> list[str]:
    return [
        re.sub(r"^##\s+一句话总结\s*$", "## 面试一句话", line)
        for line in lines
    ]


def ensure_h1(lines: list[str], title: str) -> list[str]:
    for line in lines:
        if line.strip():
            if line.strip().startswith("# "):
                return lines
            break
    return [f"# {title}", ""] + lines


def promote_bold_sections(lines: list[str]) -> list[str]:
    """将顶层 `- **标题**` 提升为 `## 标题`（仅当缺少足够 ## 时）。"""
    h2_count = sum(1 for ln in lines if re.match(r"^##\s+", ln))
    if h2_count >= 2:
        return lines
    out: list[str] = []
    for line in lines:
        m = re.match(r"^(\s*)-\s*\*\*(.+?)\*\*\s*$", line)
        if m and len(m.group(1)) == 0:
            out.append(f"## {m.group(2).strip()}")
            out.append("")
        else:
            out.append(line)
    return out


def dedupe_blank(lines: list[str]) -> list[str]:
    out: list[str] = []
    prev = False
    for line in lines:
        blank = not line.strip()
        if blank and prev:
            continue
        out.append(line.rstrip())
        prev = blank
    while out and not out[-1].strip():
        out.pop()
    return out


def extract_one_liner(lines: list[str], stem: str) -> str:
    if stem in ONE_LINERS:
        return ONE_LINERS[stem]
    for line in lines:
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("```") or s.startswith("|"):
            continue
        s = re.sub(r"^[-*]\s*", "", s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
        s = re.sub(r"\s+", " ", s).strip("：: ")
        if len(s) > 20:
            if len(s) > 120:
                s = s[:117] + "…"
            return s
    return f"掌握「{stem}」的核心概念与常见追问即可。"


def ensure_footer(lines: list[str], stem: str) -> list[str]:
    body = "\n".join(lines)
    if "## 面试一句话" in body:
        return lines
    one = extract_one_liner(lines, stem)
    return lines + ["", "## 面试一句话", "", f"> {one}"]


def needs_network_light_only(path: Path, text: str) -> bool:
    if "计算机网络" not in path.parts or "面试题" in path.parts:
        return False
    if not NETWORK_LIGHT_ONLY:
        return False
    # 已有多个 ## 且行数较多 → 轻触
    h2 = len(re.findall(r"^##\s+", text, re.M))
    return h2 >= 3 and len(text.splitlines()) > 35


def polish(text: str, path: Path) -> str:
    stem = path.stem
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = apply_global(text)
    light = needs_network_light_only(path, text)
    lines = [normalize_indent(ln) for ln in text.split("\n")]
    lines = ensure_h1(lines, stem)
    lines = strip_bad_interview_section(lines)
    lines = rename_summary_footer(lines)
    if not light:
        lines = promote_bold_sections(lines)
    lines = dedupe_blank(lines)
    if not light or "## 面试一句话" not in "\n".join(lines):
        lines = ensure_footer(lines, stem)
    lines = dedupe_blank(lines)
    return "\n".join(lines) + "\n"


def main() -> int:
    updated: list[str] = []
    for path in collect_files():
        original = path.read_text(encoding="utf-8", errors="replace")
        new = polish(original, path)
        if new != original:
            path.write_text(new, encoding="utf-8")
            updated.append(str(path.relative_to(ROOT)))
    print(f"MODIFIED_COUNT={len(updated)}")
    for rel in updated:
        print(rel)
    return 0


if __name__ == "__main__":
    sys.exit(main())
