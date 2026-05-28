# mybatis实现一对一有哪些方式怎么操作

一对一：一个对象属性引用另一个对象（如 User → Address）。

## 方式对比

| 方式 | 说明 | SQL 次数 |
|------|------|----------|
| **association + 联表** | 一次 JOIN 查询，resultMap 映射 | 1 次 |
| **association + 嵌套查询** | 主查询 + `select` 子查询 | N+1（可延迟加载） |
| **@One 注解** | 注解版嵌套查询 | N+1 |

## 1. 联表查询（推荐，避免 N+1）

```xml
<resultMap id="userMap" type="User">
  <id column="id" property="id"/>
  <association property="address" javaType="Address">
    <id column="addr_id" property="id"/>
    <result column="city" property="city"/>
  </association>
</resultMap>

<select id="selectUser" resultMap="userMap">
  SELECT u.*, a.id AS addr_id, a.city
  FROM user u LEFT JOIN address a ON u.address_id = a.id
  WHERE u.id = #{id}
</select>
```

## 2. 嵌套查询

```xml
<association property="address" column="address_id"
             select="cn.example.AddressMapper.selectById"/>
```

## 3. 注解 @One

```java
@Results({
  @Result(property = "address", column = "address_id",
          one = @One(select = "cn.example.AddressMapper.selectById"))
})
User selectUser(Long id);
```

## 面试要点

- 性能优先用 **JOIN + association**。
- 嵌套查询注意 N+1，可开 `lazyLoadingEnabled` 延迟加载。

## 面试一句话

> 一对一用 association 映射，联表一次查清最优，嵌套 select 或 @One 会多查但可延迟加载。
