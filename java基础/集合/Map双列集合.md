# Map 双列集合

## 概念

- 一次存一对数据：**键（key）** 与 **值（value）**
- **键不可重复**，值可重复；一个键对应一个值
- 键值对整体在 Java 中常称为 **Entry**（`Map.Entry`）

## 常用 API（`Map` 接口）

| 方法 | 说明 |
|------|------|
| `V put(K key, V value)` | 添加；键已存在则覆盖并返回旧值 |
| `V remove(Object key)` | 按键删除，返回被删的值 |
| `void clear()` | 清空 |
| `boolean containsKey / containsValue` | 是否包含指定键/值 |
| `int size()` | 元素个数 |
| `Set<K> keySet()` | 所有键 |
| `Set<Map.Entry<K,V>> entrySet()` | 所有键值对 |

创建示例：`Map<String, String> map = new HashMap<>();`

## 遍历方式

**1. 键找值**

```java
for (String key : map.keySet()) {
    System.out.println(key + "=" + map.get(key));
}
```

**2. 键值对（Entry）**

```java
for (Map.Entry<String, String> entry : map.entrySet()) {
    System.out.println(entry.getKey() + "=" + entry.getValue());
}
```

**3. Lambda**

```java
map.forEach((key, value) -> System.out.println(key + "=" + value));
```

## HashMap

- **特点**：无序、键不重复、无索引（通过 key 定位）
- **底层**：数组 + 链表；JDK 8+ 链表过长且数组足够大时转 **红黑树**
- **哈希**：根据 **键** 计算哈希，与值无关
- **冲突**：同一桶位用 `equals` 比较键；相同则覆盖
- **JDK 7**：新节点头插链表；**JDK 8+**：尾插，减少死链风险
- **扩容**：默认容量 16、负载因子 0.75；**只扩容不缩容**（容量不会因删除元素而减小）
- **重写约定**：自定义类作 key 时须同时重写 `equals` 与 `hashCode`，且满足：`equals` 相等则 `hashCode` 相同

## LinkedHashMap

- `HashMap` 子类，**保持插入或访问顺序**（双向链表维护顺序）

## TreeMap

- 对 **键** 排序：自然顺序（`Comparable`）或构造时传入 `Comparator`

## Hashtable 与 ConcurrentHashMap

| 对比项 | HashMap | Hashtable | ConcurrentHashMap |
|--------|---------|-----------|-------------------|
| 线程安全 | 否 | 是（方法 synchronized） | 是（分段/CAS） |
| null 键/值 | 允许 | 不允许 | 不允许 |
| 推荐使用 | 单线程 | **已过时** | 多线程 |

- **Hashtable**：已被废弃思路，多线程请用 **ConcurrentHashMap**，勿用 Hashtable。
- Hashtable 默认容量 11，扩容约 **2n+1**；HashMap 容量为 **2 的幂**，用 `(n-1) & hash` 代替取模。

## 面试要点

- Map 存键值对；键唯一，值可重复
- HashMap：数组+链表+红黑树；**只扩容不缩容**
- 作 key 的类：**equals 与 hashCode 契约**（相等对象 hash 必同）
- 有序用 LinkedHashMap；按键排序用 TreeMap
- 多线程用 ConcurrentHashMap，不用 Hashtable
