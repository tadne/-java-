# Object 类

## 地位

- `Object` 是 Java 根类，所有类直接或间接继承它
- `Object` 中的实例方法可被所有子类使用

## 构造方法

- 仅 **无参构造**（没有“所有类共有”的字段，故无带参构造）

## 常用方法

| 方法 | 说明 |
|------|------|
| `String toString()` | 对象的字符串表示；`println` 打印引用类型时底层会调用 |
| `boolean equals(Object obj)` | 比较是否“相等”；未重写时比较 **引用地址** |
| `int hashCode()` | 哈希码；与 `equals` 配套使用 |
| `Object clone()` | 浅克隆（类需实现 `Cloneable`） |
| `void finalize()` | 已废弃，勿依赖 |

空值判断请用 **`Objects.isNull` / `Objects.nonNull`**（`java.util.Objects`），不在 `Object` 上。

## equals 与 hashCode

- **默认**：`equals` 比较地址（同 `==`）
- **重写后**：通常按业务字段比较内容
- **契约**：重写 `equals` 必须同时重写 `hashCode`；`equals` 为 true 的两个对象 `hashCode` 必须相同
- **HashMap 键**：自定义类作 key 时必须遵守上述契约

## 调用方决定重写版本

```java
StringBuilder sb = new StringBuilder("hi");
String str = "hi";
sb.equals(str);  // false，走 StringBuilder 未重写的 Object.equals
str.equals(sb);  // false，String 先判断类型再比内容
```

`String` 已重写 `equals`/`hashCode`；`StringBuilder` 未重写 `equals`。

## 面试要点

- 所有类的祖先；默认 `equals`/`hashCode` 基于地址
- 重写 `equals` 必重写 `hashCode`；作 Map 键更要遵守
- `toString` 影响打印表现；空判断用 `Objects` 工具类
