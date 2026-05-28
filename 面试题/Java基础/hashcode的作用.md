# hashCode 的作用

## 核心作用

1. **配合 `equals`**：相等对象必须有相同 hashCode（`Object` 规范）
2. **哈希容器定位桶**：`HashMap`、`HashSet` 等用 `hashCode` 计算下标，再在桶内用 `equals` 解决冲突

## 与 equals 的约定

| 规则 | 说明 |
|------|------|
| 若 `equals` 为 true | hashCode **必须相同** |
| hash 相同 | `equals` **不一定** true（冲突） |
| 重写 equals | **必须**重写 hashCode |

## 在 HashMap 中的流程

```
key.hashCode() → 扰动 → (n-1) & hash → 桶下标
→ 遍历链表/树 → equals 比较
```

## 常见面试点

- 为什么用 `31` 计算 `String.hashCode`？乘子小、溢出可控、对字符分布友好
- 两个不相等对象能否 hash 相同？**可以**（鸽巢原理）

## 面试一句话

> hashCode 用于哈希定位；equals 判等；相等则 hash 必同，hash 同未必相等。
