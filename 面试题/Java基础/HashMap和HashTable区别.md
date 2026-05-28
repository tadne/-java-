# HashMap 和 HashTable 区别

`Hashtable` 是早期线程安全实现，**已不推荐**；并发场景应使用 `ConcurrentHashMap`。

## 对比表

| 维度 | HashMap | Hashtable |
|------|---------|-----------|
| 线程安全 | 否 | 是（方法级 `synchronized`） |
| null | 允许 null 键/值 | **不允许**，否则 NPE |
| 继承 | `AbstractMap` | 已废弃的 `Dictionary` |
| 初始容量 | 16（2 的幂） | 11 |
| 扩容 | 容量 ×2 | 容量 ×2 + 1 |
| 迭代器 | fail-fast | 枚举（非 fail-fast） |
| 性能 | 高 | 低（全表锁） |

## 线程安全实现

- **Hashtable**：几乎每个公有方法 `synchronized`，等价全表一把锁
- **推荐**：`ConcurrentHashMap`（JDK 8+ CAS + 桶锁，粒度更细）

## HashMap 要点（易混）

- 容量为 **2 的 n 次幂**，下标 `(n-1) & hash`
- **只扩容不缩容**
- 链表 **≥8** 且 table **≥64** 树化；树 **≤6** 退链表

## 场景选型

| 场景 | 推荐 |
|------|------|
| 单线程 | `HashMap` |
| 多线程 | `ConcurrentHashMap` |
| 遗留代码 | 勿新增 `Hashtable` |

## 面试一句话

> HashMap 快、可 null、非线程安全；Hashtable 全方法 synchronized 已过时，并发用 CHM。
