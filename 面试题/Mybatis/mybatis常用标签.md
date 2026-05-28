# mybatis常用标签

## 映射文件结构

| 标签 | 作用 |
|------|------|
| `<mapper namespace="">` | 根元素，namespace 通常 = Mapper 接口全名 |

## CRUD

| 标签 | 作用 |
|------|------|
| `<select>` | 查询 |
| `<insert>` | 插入，可用 `useGeneratedKeys` 回填主键 |
| `<update>` | 更新 |
| `<delete>` | 删除 |

## 结果映射

| 标签 | 作用 |
|------|------|
| `<resultMap>` | 自定义映射规则 |
| `<id>` / `<result>` | 主键/普通字段映射 |
| `<association>` | 一对一 |
| `<collection>` | 一对多 |

## 动态 SQL

| 标签 | 作用 |
|------|------|
| `<if>` | 条件 |
| `<choose>` / `<when>` / `<otherwise>` | 多分支 |
| `<where>` | 自动处理 AND/OR |
| `<set>` | 更新时自动逗号 |
| `<foreach>` | 遍历 in、批量插入 |
| `<trim>` | 自定义前缀后缀 |

## 示例

```xml
<select id="find" resultType="User">
  SELECT * FROM user
  <where>
    <if test="name != null">AND name = #{name}</if>
  </where>
</select>
```

## 面试要点

- 动态 SQL 核心：if、where、foreach。
- association/collection 处理关联关系。

## 面试一句话

> MyBatis 常用标签包括 CRUD 四标签、resultMap 映射、以及 if/where/foreach 等动态 SQL 标签。
