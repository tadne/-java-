# equals 和 == 的区别

## 对比表

| | `==` | `equals()` |
|---|------|------------|
| 类型 | 运算符 | `Object` 实例方法，可重写 |
| 基本类型 | 比较**值** | 不能用于基本类型 |
| 引用类型 | 比较**引用地址**（是否同一对象） | 默认同 `==`；重写后比较**逻辑相等** |
| 典型重写 | — | `String`、`Integer` 等按内容比较 |

## 使用注意

```java
String a = new String("hi");
String b = new String("hi");
a == b;        // false，不同对象
a.equals(b);   // true，内容相同
```

- **重写 `equals` 必须同时重写 `hashCode`**，否则违反约定，在 `HashMap` 等容器中行为异常
- `equals` 需满足：自反、对称、传递、一致；与 `null` 比较返回 `false`

## 与 hashCode 的关系

- 若 `a.equals(b)` 为 true，则 `a.hashCode() == b.hashCode()` 必须成立
- 反之不成立：hash 相同的两对象可以 `equals` 为 false（哈希冲突）

## 面试一句话

> `==` 比基本类型值或引用地址；`equals` 默认同地址，重写后比业务字段，且须配合 `hashCode`。
