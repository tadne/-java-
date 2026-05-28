# mapper方法不能被重载

## 原因

MyBatis 将 **接口全限定名 + 方法名** 作为 SQL 语句的唯一 id（`namespace.id`）。

同一 Mapper 接口中两个同名方法（参数不同）会映射到**同一个 id**，导致冲突或不可预期行为。

```text
cn.example.UserMapper.selectById  → 只能对应一条 SQL
```

## 正确做法

### 1. 不同方法名

```java
User selectById(Long id);
List<User> selectByName(String name);
```

### 2. 动态 SQL 合并

```xml
<select id="findUsers" resultType="User">
  SELECT * FROM user
  <where>
    <if test="id != null">AND id = #{id}</if>
    <if test="name != null">AND name = #{name}</if>
  </where>
</select>
```

## 面试要点

- 映射键是 **方法名**，不是 Java 重载签名。
- 类似逻辑用动态 SQL 的 `<if>`、`<choose>` 实现。

## 面试一句话

> Mapper 方法不能重载，因为 SQL 的 id 只有 namespace+方法名，重载会冲突，应改名或用动态 SQL。
