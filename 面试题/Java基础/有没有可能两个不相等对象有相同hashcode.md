# 有没有可能两个不相等对象有相同 hashCode

**有可能。** 这叫 **哈希冲突（hash collision）**。

## 原因

- `hashCode()` 返回 32 位 int，对象数量可以远超 2³²
- 鸽巢原理：不同对象必然存在相同 hashCode
- **相等对象 hashCode 必须相同**；**hashCode 相同对象可以不相等**

## equals 与 hashCode 契约

| 关系 | 要求 |
|------|------|
| `a.equals(b) == true` | 必须 `a.hashCode() == b.hashCode()` |
| `hashCode` 相同 | **不要**求 `equals` 为 true |
| 重写 `equals` | **必须**重写 `hashCode` |

违反契约会导致 `HashMap`/`HashSet` 行为异常（“丢元素”、查不到）。

## HashMap 如何处理冲突

1. **链表**：同桶内用链表（或红黑树）存多个 Entry
2. **比较 equals**：`hashCode` 相同后，再对 key 调用 `equals` 判断是否同一键

```java
// 简化逻辑
int index = (n - 1) & hash(key);
for (Node e = table[index]; e != null; e = e.next) {
    if (e.hash == hash && (e.key == key || key.equals(e.key)))
        return e.value;
}
```

## 其他解决思路（了解）

| 方法 | 说明 |
|------|------|
| 拉链法 | HashMap 采用，同桶链表/树 |
| 开放定址 | 冲突后探测下一个空位 |
| 再哈希 | 换第二个 hash 函数 |

## 面试一句话

> 不相等对象可以有相同 hashCode；HashMap 用链表/红黑树解决冲突，最终靠 equals 区分键。
