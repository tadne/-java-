# 什么是Mybatis

MyBatis 是开源的 **Java 持久层框架**，通过 XML 或注解将 SQL 与 Java 对象映射，半自动 ORM（SQL 由开发者编写）。

## 核心特点

| 特点 | 说明 |
|------|------|
| SQL 可控 | 手写 SQL，便于优化与复杂查询 |
| 映射灵活 | `resultMap`、注解、自动驼峰映射 |
| 轻量 | 相比全自动 ORM 学习曲线平缓 |
| 插件机制 | 分页（PageHelper）、拦截器扩展 |

## 与 Hibernate 对比（简）

| | MyBatis | Hibernate |
|---|---------|-----------|
| SQL | 手写为主 | 自动生成为主 |
| 适用 | SQL 优化敏感、复杂报表 | 领域模型驱动、CRUD 为主 |

## 核心组件

- `SqlSessionFactory`：会话工厂
- `SqlSession`：执行 SQL 的会话（线程不安全，勿共享）
- `Mapper` 接口：JDK 动态代理执行 SQL

## 面试要点

- MyBatis 是 **半自动 ORM**，强调 SQL 与映射分离。
- 常与 Spring Boot 通过 `mybatis-spring-boot-starter` 集成。

## 面试一句话

> MyBatis 是半自动持久层框架，开发者写 SQL，框架负责参数绑定和结果映射，灵活且易优化。
