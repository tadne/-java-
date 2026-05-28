# SynchronizedMap 和 ConcurrentHashMap 的区别

> 文件名中的 `Concurent` 为历史拼写，实际指 `ConcurrentHashMap`。

## 对比总览

| 维度 | `Collections.synchronizedMap` | `ConcurrentHashMap` |
|------|------------------------------|---------------------|
| 锁粒度 | 整张 Map（`synchronized(map)`） | JDK8+：桶头节点 / 红黑树根 |
| 并发度 | 低，读写互斥 | 高，不同桶可并发 |
| null | 不允许 null 键/值（与 Hashtable 一致） | **键和值均不允许 null** |
| 迭代器 | 需手动同步，否则可能 CME | 弱一致性，不抛 CME |
| 复合操作 | `if (!map.containsKey(k)) map.put(k,v)` 非原子 | 提供 `putIfAbsent` 等原子 API |

## 实现方式

### SynchronizedMap

```java
Map<K,V> syncMap = Collections.synchronizedMap(new HashMap<>());
```

- 每个方法用 `synchronized(mutex)` 包裹底层 Map
- 遍历时仍需：`synchronized (syncMap) { for (...) }`

### ConcurrentHashMap（JDK 8+，面试重点）

- **结构**：数组 + 链表 + 红黑树（与 HashMap 类似）
- **put**：空桶 CAS 插入；有冲突则 `synchronized` 锁住桶头
- **get**：通常无锁，靠 `volatile` 保证 Node 可见性
- **size**：基于 baseCount + CounterCell，非精确快照

> JDK 7 的 **Segment 分段锁** 已过时，面试应优先讲 JDK 8+ 实现。

## 迭代与“快照”误区

- ConcurrentHashMap **不会**复制整张 Map 做快照
- 迭代器是 **弱一致性**：能反映创建后已完成的写，但不保证遍历期间看到所有并发修改
- 不会抛 `ConcurrentModificationException`，也不等于强一致快照

## null 规则（易错）

```java
// 以下均会 NPE
concurrentHashMap.put(null, "v");
concurrentHashMap.put("k", null);
```

设计原因：在并发场景下，`get(key)==null` 无法区分「不存在」与「值为 null」。

## 选型建议

| 场景 | 推荐 |
|------|------|
| 高并发读写 | `ConcurrentHashMap` |
| 低频同步、已有 HashMap | `synchronizedMap` |
| 读多写少、允许复制 | `CopyOnWriteArrayMap`（较少用） |
| 需要排序 | `ConcurrentSkipListMap` |

## 面试一句话

> `synchronizedMap` 锁整张表；`ConcurrentHashMap` 锁桶、支持更高并发，且不允许 null 键值，迭代为弱一致性而非全表快照。
