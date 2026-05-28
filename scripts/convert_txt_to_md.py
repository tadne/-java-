#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""将仓库内 .txt 笔记批量转换为格式统一的 Markdown。"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".idea", "scripts", "node_modules"}


def count_leading_tabs(line: str) -> int:
    n = 0
    for ch in line:
        if ch == "\t":
            n += 1
        else:
            break
    return n


def strip_leading_tabs(line: str) -> str:
    return line.lstrip("\t")


def is_section_heading(text: str) -> bool:
    """短行、无句号结尾，或常见章节后缀，视为小节标题。"""
    if not text or len(text) > 80:
        return False
    if text.endswith(("。", "；", "，", ".", ";", "：", ":")) and "：" not in text and ":" not in text:
        return False
    if re.match(r"^\d+[\.\)、]\s*", text):
        return False
    suffixes = (
        "简介", "概念", "原理", "总结", "区别", "步骤", "方案",
        "机制", "特性", "架构", "介绍", "理解", "分析", "实现",
    )
    if any(text.endswith(s) for s in suffixes):
        return True
    if "：" in text or ":" in text:
        return False
    return len(text) <= 40 and not text.endswith("。")


def format_key_value(text: str) -> str | None:
    m = re.match(r"^(.+?)[：:]\s*(.*)$", text)
    if not m:
        return None
    key, val = m.group(1).strip(), m.group(2).strip()
    if not key or len(key) > 50:
        return None
    if val:
        return f"**{key}**：{val}"
    return f"**{key}**"


def convert_body(lines: list[str], title: str) -> list[str]:
    out: list[str] = []
    i = 0
    while i < len(lines):
        raw = lines[i].rstrip()
        if not raw.strip():
            out.append("")
            i += 1
            continue

        depth = count_leading_tabs(raw)
        text = strip_leading_tabs(raw).strip()

        # 跳过与文件名重复的纯标题首行
        if i == 0 and text.replace(" ", "") == title.replace(" ", ""):
            i += 1
            continue

        indent = "  " * depth

        kv = format_key_value(text)
        if kv and depth <= 2:
            out.append(f"{indent}- {kv}")
            i += 1
            continue

        if depth == 0 and is_section_heading(text):
            out.append(f"## {text}")
            i += 1
            continue

        if re.match(r"^\d+[\.\)、]\s+", text):
            out.append(f"{indent}{text}")
            i += 1
            continue

        if depth > 0:
            out.append(f"{indent}- {text}")
        else:
            out.append(text)
        i += 1

    # 合并连续空行、去除尾部空行
    cleaned: list[str] = []
    prev_blank = False
    for line in out:
        blank = not line.strip()
        if blank and prev_blank:
            continue
        cleaned.append(line)
        prev_blank = blank
    while cleaned and not cleaned[-1].strip():
        cleaned.pop()
    return cleaned


def convert_file(txt_path: Path) -> Path:
    md_path = txt_path.with_suffix(".md")
    if md_path.exists():
        return md_path  # 已有 md 则跳过（如计算机网络部分）

    raw = txt_path.read_text(encoding="utf-8", errors="replace")
    lines = raw.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    title = txt_path.stem

    body = convert_body(lines, title)
    parts = [f"# {title}", ""]
    parts.extend(body)
    parts.append("")
    md_path.write_text("\n".join(parts), encoding="utf-8")
    return md_path


def collect_txt_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.txt"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def main() -> int:
    root = ROOT
    if len(sys.argv) > 1:
        root = Path(sys.argv[1]).resolve()

    txt_files = collect_txt_files(root)
    converted = 0
    skipped = 0
    removed = 0

    for txt in txt_files:
        md = txt.with_suffix(".md")
        if md.exists():
            skipped += 1
            txt.unlink()
            removed += 1
            continue
        convert_file(txt)
        converted += 1
        txt.unlink()
        removed += 1

    print(f"Converted: {converted}, skipped (md exists): {skipped}, removed txt: {removed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
