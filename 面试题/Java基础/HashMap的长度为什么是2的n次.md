# HashMap 的长度为什么是 2 的 n 次幂

## 核心原因

HashMap 的容量（table 长度）必须是 **2 的 n 次幂**，以便用位运算快速定位桶下标，并在扩容时高效迁移。

## 1. 下标计算：位运算代替取模

```java
// 实际：index = (n - 1) & hash
int index = hash & (table.length - 1);
```

- `length` 为 2^n 时，`length - 1` 的二进制为 `000...111`，`&` 等价于 `% length` 且更快
- 若 length 不是 2 的幂，`hash % length` 分布可能不均匀

### hash 扰动（JDK 8）

```java
static final int hash(Object key) {
    int h;
    return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
}
```

高 16 位与低 16 位异或，减少低位冲突。

## 2. 扩容：容量翻倍，非“缩容”

> **易错**：标准 `HashMap` **只扩容、不缩容**，没有 `length / 2` 的缩容逻辑。

- 默认负载因子 **0.75**
- 元素数 > `capacity * 0.75` 时扩容为 **2 倍**
- JDK 8 扩容时，节点要么留在原索引，要么到 `原索引 + oldCap`（利用 `hash & oldCap` 判断）

```java
// 扩容示例
int newCapacity = oldCapacity << 1;  // 乘 2
```

## 3. 与红黑树的关系

- 单桶链表长度 **≥ 8** 且 table 长度 **≥ 64** → 树化
- 树化节点 **≤ 6** → 退化为链表
- 2 的幂与树化无直接因果关系，但保证哈希分布均匀，间接减少极端链表

## 4. 为何不是质数（对比 Hashtable）

- Hashtable 早期用质数长度 + 取模，冲突处理不同
- HashMap 选择 2 的幂 + 位运算，在性能和实现简洁上更优

## 面试一句话

> 2 的 n 次幂让 `(n-1) & hash` 等价取模且更快；扩容翻倍；**HashMap 不会缩容**。
