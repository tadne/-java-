# 说说什么是 fail-fast

## 定义

**fail-fast（快速失败）**：在迭代过程中，若集合被**结构性修改**（非迭代器自己的 `remove`），立即抛 `ConcurrentModificationException`。

## 机制

- 迭代时比较 `modCount` 与 `expectedModCount`
- 不一致 → 认为并发修改 → 抛异常

## 典型集合

| 类型 | 迭代器 |
|------|--------|
| `ArrayList`、`HashMap` | fail-fast |
| `ConcurrentHashMap` | 弱一致，不抛 CME |
| `CopyOnWriteArrayList` | 快照迭代 |

## 注意

- fail-fast **不能保证**在多线程下一定检测到所有并发修改
- 单线程中也不要在 `for-each` 里直接 `list.remove(i)`，用 `Iterator.remove()`

## 面试一句话

> fail-fast 在迭代中检测到结构被改就抛 CME；CHM、COW 等是弱一致/fail-safe 风格。
