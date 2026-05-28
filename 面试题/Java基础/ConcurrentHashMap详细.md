# ConcurrentHashMap 详解

`ConcurrentHashMap` 是线程安全的 `Map`，JDK 7 与 JDK 8+ 实现差异很大，**面试以 JDK 8+ 为准**。

## 版本对比

| 特性 | JDK 7 | JDK 8+ |
|------|-------|--------|
| 结构 | Segment 数组 + 桶 | Node 数组 + 链表/红黑树 |
| 锁 | Segment 分段锁 | 桶头 synchronized / CAS |
| 缩容 | 有 Segment 级概念 | **不支持缩容**（与 HashMap 不同） |
| null | 不允许 | 不允许 |

## JDK 8+ 核心结构

- `Node<K,V>[] table`：哈希表
- 链表长度 ≥ 8 且数组长度 ≥ 64 时树化；≤ 6 时退化链表
- `sizeCtl`：控制初始化和扩容阈值

## 主要操作

### get(key)

- **一般不加锁**
- 先读 table 元素（volatile 语义），再沿链表/树查找
- 扩容迁移期间通过 `ForwardingNode` 到新表查找

### put(key, value)

1. 表未初始化 → 协助初始化（CAS `sizeCtl`）
2. 桶为空 → CAS 放入首个 Node
3. 桶非空 → `synchronized` 锁住头节点，链表插入或树插入
4. 元素数超阈值 → **扩容**（2 倍，多线程可协助转移）

### remove(key)

- 需锁住桶头，逻辑类似 HashMap，保证并发安全

## 与 HashMap 的差异

| 点 | HashMap | ConcurrentHashMap |
|----|---------|-------------------|
| 线程安全 | 否 | 是 |
| null | 允许一个 null 键 | 键值均不可 null |
| 扩容 | 支持 | 只扩不缩 |
| 并发度 | — | 桶级 |

## 常用原子 API

- `putIfAbsent(k, v)`：不存在才放入
- `replace(k, old, new)`：CAS 式替换
- `compute` / `merge`：原子计算（注意 lambda 内勿做重入锁）

## 面试高频

1. **为什么 get 不加锁？** 依赖 volatile 读可见 + 扩容时的 ForwardingNode 设计
2. **size 怎么统计？** `baseCount` + `CounterCell` 分散累加，弱一致
3. **1.7 和 1.8 区别？** Segment 锁 → 桶锁 + CAS，结构更像 HashMap

## 一句话总结

> JDK 8 的 CHM 用 CAS 占空桶、synchronized 锁冲突桶，get 无锁读；不支持 null，只扩容不缩容。
