# HashMap 的 key 可以使用任意类吗

## 结论

**语法上**可以；**实践上**必须正确实现 `hashCode()` 与 `equals()`，且作为 key 的对象**不宜可变**。

## 要求

| 要求 | 原因 |
|------|------|
| 实现 `hashCode` + `equals` | 否则无法正确存取、去重 |
| 参与哈希的字段不可变 | 修改后 hash 变，key “丢失” |
| 避免用可变对象作 key | 如未冻结的 `StringBuilder` |

## 自定义类示例要点

```java
@Override
public boolean equals(Object o) { /* 同类型 + 字段比较 */ }

@Override
public int hashCode() {
    return Objects.hash(field1, field2);
}
```

## 不推荐作 key 的类型

- 未重写 `hashCode`/`equals` 的类（仅用地址哈希）
- 字段会变的可变对象

## 面试一句话

> 任意类都可作 key，但必须稳定、正确地实现 hashCode/equals，且 key 状态不可变。
