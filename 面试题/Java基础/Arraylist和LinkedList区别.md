# ArrayList 和 LinkedList 区别

两者均实现 `List`，**线程都不安全**（并发用 `CopyOnWriteArrayList` 等）。

## 对比表

| 维度 | ArrayList | LinkedList |
|------|-----------|------------|
| 底层 | 动态数组 | 双向链表 |
| 随机访问 | O(1) `get(i)` | O(n) |
| 头尾插入 | 尾插均摊 O(1)；头插 O(n) | 头尾 O(1) |
| 中间插入/删 | O(n) 移动元素 | O(n) 找节点 + O(1) 改链 |
| 内存 | 连续、缓存友好 | 额外指针开销 |
| 适用 | 读多、按下标访问 | 头尾频繁增删 |

## 选型

- 默认列表、大量 `get` → **ArrayList**
- 队列/双端队列语义 → `LinkedList` 或 `ArrayDeque`（常更优）

## 面试一句话

> ArrayList 数组随机访问快；LinkedList 链表头尾增删快、按下标慢。
