# ConcurrentHashMap 与 HashMap 异同

两者都是基于哈希表的 `Map` 实现，JDK 8+ 底层均为数组 + 链表 + 红黑树，但**线程安全与 null 语义**差异是面试重点。

## 相同点

| 点 | 说明 |
|----|------|
| 数据结构 | 哈希表定位，冲突用链表/树 |
| 无序 | 不保证插入顺序（`LinkedHashMap` 才保证） |
| 核心 API | `put` / `get` / `remove` 等 |

## 不同点

| 维度 | HashMap | ConcurrentHashMap |
|------|---------|-------------------|
| 线程安全 | 否 | 是 |
| null | 允许 1 个 null 键、多个 null 值 | **键值均不允许 null** |
| 锁机制 | 无（并发需外部同步） | JDK 8+：**CAS 占空桶** + **synchronized 锁桶头** |
| 扩容 | 2 倍扩容 | 2 倍扩容，**只扩不缩** |
| 迭代器 | fail-fast | 弱一致，不抛 CME |
| 原子 API | 无 | `putIfAbsent`、`compute`、`merge` 等 |

## JDK 7 vs JDK 8（CHM）

| 版本 | 结构 | 并发控制 |
|------|------|----------|
| JDK 7 | Segment 数组 | Segment 分段锁 |
| JDK 8+ | Node 数组 + 链表/树 | 桶级 synchronized / CAS |

## 树化阈值（与 HashMap 一致）

- 单桶链表 **≥ 8** 且 table 长度 **≥ 64** → 红黑树
- 树节点 **≤ 6** → 退化为链表

## 选用建议

- 单线程、可接受 null → `HashMap`
- 高并发读写 → `ConcurrentHashMap`（不要用 `Hashtable`）
- 需全表 `synchronized` 遍历 → `Collections.synchronizedMap`

## 面试一句话

> HashMap 非线程安全且可 null；CHM 线程安全、不可 null，JDK 8 桶锁 + CAS，树化 8/退化 6。
