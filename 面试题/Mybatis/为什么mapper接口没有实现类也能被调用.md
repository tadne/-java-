# 为什么mapper接口没有实现类也能被调用

## 原因

MyBatis 在运行时为 Mapper 接口生成 **JDK 动态代理**对象，调用接口方法时进入 `MapperProxy.invoke()`，再映射到 XML/注解中的 SQL 执行。

## 流程

```
Mapper 接口
  → MapperRegistry 注册
  → MapperProxyFactory.newInstance()
  → MapperProxy（InvocationHandler）
  → MapperMethod 解析 SQL
  → SqlSession 执行 JDBC
```

## 关键类

| 类 | 作用 |
|----|------|
| `MapperRegistry` | 注册 Mapper 接口 |
| `MapperProxyFactory` | 创建代理 |
| `MapperProxy` | 拦截方法调用 |
| `MapperMethod` | 绑定方法名与 SQL、参数 |

## Spring 集成

- `@MapperScan` 扫描接口，注册为 Bean。
- 实际注入的是代理对象，不是实现类。

## 常见误区

- 接口方法**不能重载**（同一 namespace 下 id = 方法名，必须唯一）。
- 不需要 `@Entity`（那是 JPA）；MyBatis 用 POJO + 映射即可。

## 面试要点

- JDK 动态代理 + 方法名与 SQL id 绑定。
- Spring Boot 通过 `@MapperScan` 注册代理 Bean。

## 面试一句话

> MyBatis 用 JDK 动态代理为 Mapper 接口生成代理，invoke 时根据方法名找到 SQL 并由 SqlSession 执行。
