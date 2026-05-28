# Autowired和resource注解的区别

两者都用于依赖注入，来源与匹配规则不同。

## 对比表

| 对比项 | @Autowired | @Resource |
|--------|------------|-----------|
| 来源 | Spring 框架 | JSR-250（`javax.annotation` / `jakarta.annotation`） |
| 默认匹配 | **byType**（类型） | **byName**（名称），找不到再 byType |
| 指定名称 | `@Qualifier("name")` | `name` 属性 |
| 注入位置 | 字段、构造器、setter | 字段、setter（**不支持构造器**） |
| 是否必须 | `required=false` 可省略 | 找不到默认抛异常（无 required） |
| 多实现类 | 配合 @Qualifier 或 @Primary | 指定 name 或 type |

## 匹配流程简述

**@Autowired**：先按类型找唯一 Bean → 多个候选时按字段名/参数名匹配 → 仍冲突需 @Qualifier/@Primary。

**@Resource**：先按 `name` → 再按字段名 → 再按类型。

## 示例

```java
@Autowired
@Qualifier("mysqlDataSource")
private DataSource dataSource;

@Resource(name = "mysqlDataSource")
private DataSource ds;
```

## 面试要点

- @Autowired 是 Spring 的，默认按类型；@Resource 是标准注解，默认按名称。
- 构造器注入推荐 @Autowired（@Resource 不支持构造器）。
- 多 Bean 时：Autowired 用 @Qualifier，Resource 用 name。

## 面试一句话

> @Autowired 默认按类型注入属 Spring，@Resource 默认按名称属 JSR-250；多实现时分别用 @Qualifier 和 name 指定。
