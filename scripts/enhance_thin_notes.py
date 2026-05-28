#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为过短的面试题笔记补充「面试要点」与基础结构（不覆盖已有优质长文）。"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {".git", ".idea", "scripts"}
SKIP_NAMES = LIGHT = {
    "学习变更说明.md", "README.md",
    *{
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
    },
}


def content_lines(text: str) -> list[str]:
    return [
        l for l in text.splitlines()
        if l.strip() and not l.strip().startswith("#")
        and l.strip() != "---"
    ]


def extract_bullets(lines: list[str], max_n: int = 6) -> list[str]:
    bullets: list[str] = []
    for line in lines:
        s = line.strip()
        if s.startswith("- "):
            bullets.append(s)
        m = re.match(r"^-\s*\*\*(.+?)\*\*[：:]?\s*(.*)", s)
        if m and len(bullets) < max_n:
            k, v = m.group(1), m.group(2)
            if k not in {b.split("**")[1] if "**" in b else "" for b in bullets}:
                bullets.append(f"- **{k}**" + (f"：{v[:100]}" if v else ""))
    return bullets[:max_n]


def needs_footer(text: str) -> bool:
    return (
        "## 面试要点" not in text
        and "## 小结" not in text
        and "面试一句话" not in text
    )


def enhance(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="replace")
    if path.name in LIGHT or not needs_footer(text):
        return False
    body_lines = content_lines(text)
    if len(body_lines) > 50:
        return False
    bullets = extract_bullets(body_lines)
    if len(bullets) < 2:
        return False
    title = path.stem
    if not text.lstrip().startswith("# "):
        text = f"# {title}\n\n" + text
    text = text.rstrip() + "\n\n## 面试要点\n\n" + "\n".join(bullets) + "\n"
    path.write_text(text, encoding="utf-8")
    return True


def main() -> None:
    n = 0
    for path in sorted(ROOT.rglob("*.md")):
        if any(p in SKIP for p in path.parts) or path.name in SKIP_NAMES:
            continue
        if enhance(path):
            n += 1
    print(f"Enhanced {n} thin notes with 面试要点 section.")


if __name__ == "__main__":
    main()
