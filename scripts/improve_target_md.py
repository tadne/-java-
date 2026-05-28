#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""深度改进指定目录 Markdown：结构、错别字、Java 事实。"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET_DIRS = ["java基础", "多线程", "常用API类", "JVM", "23种设计模式"]

REPLACEMENTS = [
    ("无关平台", "跨平台"),
    ("村出纳", "存储"),
    ("Compartor", "Comparator"),
    ("toStirng", "toString"),
    ("unLock()", "unlock()"),
    ("void Lock()", "void lock()"),
    ("void unLock()", "void unlock()"),
    ("clone(int a)", "clone()"),
    ("简间接", "间接"),
    ("HashMap会缩容", "HashMap只扩容不缩容"),
    ("HashMap 会缩容", "HashMap 只扩容不缩容"),
    ("finaliz()", "finalize()"),
    ("SoftRefef=rence", "SoftReference"),
    ("JDK 9 及以上版本中叫做元空间", "JDK 8 起元空间替代永久代"),
    ("你好，这是Bing。我很高兴你对Java编程感兴趣。😊", ""),
    ("你好，这是Bing", ""),
    ("ikun分词", "IK 分词"),
    ("CHM 支持 null", "ConcurrentHashMap 不允许 null"),
    ("equals和hashcode没有关系", "重写 equals 必须同时重写 hashCode"),
    ("重写equals方法和hashCode方法就好了", "重写 toString；用作 HashMap 键时还需同时重写 equals 与 hashCode"),
    ("boolean isNull(Object obj)", "Objects.isNull(obj)（java.util.Objects）"),
    ("boolean nonNull(Object obj)", "Objects.nonNull(obj)"),
]

# 代码块内误升为标题的行
CODE_H_RE = re.compile(r"^##\s*(@Override|}|{|\)|;|return|public|private|INSTANCE|//)")


def is_skip(path: Path, lines: list[str], text: str) -> bool:
    if len(lines) <= 70:
        return False
    has_h1 = any(l.strip().startswith("# ") for l in lines)
    h2 = sum(1 for l in lines if re.match(r"^##\s+\S", l))
    footer = "## 小结" in text or "## 面试要点" in text
    return has_h1 and h2 >= 3 and footer


def fix_code_headers(lines: list[str]) -> list[str]:
    out: list[str] = []
    in_fence = False
    for line in lines:
        if line.strip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence or CODE_H_RE.match(line.strip()):
            if line.startswith("## "):
                line = line[3:]  # 去掉误加的 ##
        # 修复 for 循环被拆成标题
        if line.strip().startswith("## }"):
            line = line.replace("## }", "}")
        if "- **for (" in line or line.strip().startswith("- **for ("):
            line = re.sub(r"^- \*\*for \((.+?)\*\*：", r"for (\1) {", line)
        out.append(line)
    return out


def normalize_structure(lines: list[str]) -> list[str]:
    """顶级列表去多余缩进；孤立 **标题** 升为 ##。"""
    out: list[str] = []
    for line in lines:
        if re.match(r"^  +- ", line):
            line = line.lstrip()
            if not line.startswith("- "):
                line = "- " + line
        m = re.match(r"^  - \*\*(.+?)\*\*\s*$", line)
        if m:
            line = f"## {m.group(1).strip()}"
        out.append(line)
    return out


def ensure_h1(lines: list[str], title: str) -> list[str]:
    for line in lines:
        if line.strip():
            if line.strip().startswith("# "):
                return lines
            break
    return [f"# {title}", ""] + lines


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


def smart_footer(lines: list[str]) -> list[str]:
    body = "\n".join(lines)
    if "## 小结" in body or "## 面试要点" in body:
        return lines
    bullets: list[str] = []
    for line in lines:
        if re.match(r"^##\s+", line) and "面试" not in line and "小结" not in line:
            t = line[3:].strip()
            if 2 < len(t) < 40:
                bullets.append(f"- {t}")
        m = re.match(r"^- \*\*(.+?)\*\*[：:]\s*(.+)$", line.strip())
        if m:
            bullets.append(f"- **{m.group(1)}**：{m.group(2)[:90]}")
        if len(bullets) >= 5:
            break
    if len(bullets) < 2:
        return lines
    non_empty = [l for l in lines if l.strip() and not l.startswith("#")]
    head = "## 小结" if len(non_empty) < 22 else "## 面试要点"
    return lines + ["", head, ""] + bullets[:5]


def improve_text(text: str, title: str) -> str:
    for a, b in REPLACEMENTS:
        text = text.replace(a, b)
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    lines = ensure_h1(lines, title)
    lines = fix_code_headers(lines)
    lines = normalize_structure(lines)
    lines = smart_footer(lines)
    lines = dedupe_blank(lines)
    return "\n".join(lines) + "\n"


def main() -> None:
    modified: list[str] = []
    skipped: list[str] = []
    for d in TARGET_DIRS:
        for path in sorted((ROOT / d).rglob("*.md")):
            if "面试题" in path.parts:
                continue
            orig = path.read_text(encoding="utf-8", errors="replace")
            lines = orig.splitlines()
            if is_skip(path, lines, orig):
                skipped.append(path.name)
                continue
            new = improve_text(orig, path.stem)
            if new != orig:
                path.write_text(new, encoding="utf-8")
                modified.append(str(path.relative_to(ROOT)).replace("\\", "/"))
    print(f"SKIP (well-structured >70): {len(skipped)}")
    print(f"MODIFIED: {len(modified)}")
    for m in modified:
        print(m)


if __name__ == "__main__":
    main()
