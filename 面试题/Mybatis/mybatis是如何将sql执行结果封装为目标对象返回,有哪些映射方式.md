# mybatis是如何将sql执行结果封装为目标对象返回,有哪些映射方式

## 封装流程

1. 执行 SQL 得到 `ResultSet`
2. 根据返回值类型（`resultType` / `resultMap`）选择 `ResultSetHandler`
3. 按列名（或映射规则）通过反射设置对象属性
4. 返回单个对象、List、Map 或基本类型

## 默认映射规则

- `resultType` 为 POJO：列名与属性名一致时自动映射（可开驼峰）
- 基本类型：取第一行第一列
- `Map`：列名为 key

## 映射方式

| 方式 | 说明 |
|------|------|
| **resultType** | 列名=属性名或别名匹配 |
| **resultMap** | 自定义列与属性、嵌套、鉴别器 |
| **SQL 别名** | `AS` 对齐属性名 |
| **注解 @Results** | 注解定义映射 |

## resultMap 示例

```xml
<resultMap id="userMap" type="User">
  <id column="id" property="id"/>
  <result column="user_name" property="userName"/>
</resultMap>
```

## 多结果类型

| 返回类型 | 处理 |
|----------|------|
| `User` | 单行 → 对象 |
| `List<User>` | 多行 → 列表 |
| `int` | 影响行数或 count |
| `Map` | 每行一个 Map |

## 面试要点

- 核心：ResultSet → 反射设值 + 映射配置。
- 字段名不一致必须用 resultMap 或别名。

## 面试一句话

> MyBatis 通过 ResultSetHandler 按 resultType/resultMap 把结果集反射封装成对象，映射方式有自动、resultMap、别名和注解。
