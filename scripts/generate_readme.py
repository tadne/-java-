#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 README.md 知识库目录索引。"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {".git", ".idea", "scripts", "README.md"}


def rel_link(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def tree_section(dir_path: Path, level: int = 0) -> list[str]:
    lines: list[str] = []
    indent = "  " * level
    items = sorted(dir_path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    for item in items:
        if item.name in SKIP or item.name.startswith("."):
            continue
        if item.is_dir():
            md_files = sorted(item.rglob("*.md"))
            subdirs = [p for p in item.iterdir() if p.is_dir() and p.name not in SKIP]
            if subdirs:
                lines.append(f"{indent}- **{item.name}/**")
                lines.extend(tree_section(item, level + 1))
            elif md_files:
                if len(md_files) <= 8:
                    lines.append(f"{indent}- **{item.name}/**")
                    for f in md_files:
                        lines.append(f"{indent}  - [{f.stem}]({rel_link(f)})")
                else:
                    lines.append(
                        f"{indent}- **{item.name}/**（{len(md_files)} 篇）"
                    )
            else:
                lines.append(f"{indent}- **{item.name}/**")
        elif item.suffix == ".md" and item.parent == dir_path:
            lines.append(f"{indent}- [{item.stem}]({rel_link(item)})")
    return lines


def main() -> None:
    sections: list[str] = [
        "# Java 学习笔记",
        "",
        "> 2023 年 3 月起整理的 Java 全栈学习笔记，持续更新。",
        "> 原文多为手敲速记，已统一整理为 Markdown 格式，便于检索与阅读。",
        "",
        "## 使用说明",
        "",
        "- 按目录主题浏览，面试题目录按技术栈分类",
        "- 计算机网络部分参考 [小林 coding](https://xiaolincoding.com/) 整理",
        "- 文件按创建时间排序阅读时，可在 IDE 中按修改/创建时间查看",
        "",
        "## 目录总览",
        "",
    ]

    top_dirs = sorted(
        [p for p in ROOT.iterdir() if p.is_dir() and p.name not in SKIP],
        key=lambda p: p.name,
    )

    # 自定义排序：基础 -> 框架 -> 中间件 -> 面试
    order = [
        "java基础", "常用API类", "多线程", "JVM", "23种设计模式",
        "Spring", "springBoot", "SpringCloud", "MySQL", "redis",
        "RabbitMq", "ElasticSearch", "分布式", "计算机网络",
        "面试题",
    ]
    ordered = []
    names = {p.name: p for p in top_dirs}
    for name in order:
        if name in names:
            ordered.append(names.pop(name))
    ordered.extend(sorted(names.values(), key=lambda p: p.name))

    for d in ordered:
        md_count = len(list(d.rglob("*.md")))
        sections.append(f"### [{d.name}]({rel_link(d)}/)（{md_count} 篇）")
        sections.append("")
        sections.extend(tree_section(d, 0))
        sections.append("")

    sections.extend([
        "## 文档格式说明",
        "",
        "| 元素 | 说明 |",
        "|------|------|",
        "| `# 标题` | 与文件名一致的一级标题 |",
        "| `## 小节` | 章节、概念块标题 |",
        "| `- **关键词**：说明` | 要点对照式笔记 |",
        "| 嵌套列表 | 表示层级与从属关系 |",
        "",
        "## 贡献与维护",
        "",
        "- 新增笔记请直接使用 `.md` 格式",
        "- 批量转换脚本：`scripts/convert_txt_to_md.py`（历史 txt 已迁移完毕）",
        "",
    ])

    (ROOT / "README.md").write_text("\n".join(sections), encoding="utf-8")
    print("README.md generated")


if __name__ == "__main__":
    main()
