# Mybatis的优缺点

## 优点

| 优点 | 说明 |
|------|------|
| SQL 可控 | 手写 SQL，易优化、走索引、写复杂查询 |
| 学习成本适中 | 比全自动 ORM 直观，XML/注解映射清晰 |
| 灵活映射 | resultMap 支持嵌套、集合、多表 |
| 插件扩展 | PageHelper、自定义 Interceptor |
| 与 Spring 集成成熟 | `mybatis-spring-boot-starter` |

## 缺点

| 缺点 | 说明 |
|------|------|
| SQL 工作量大 | 表多时 XML 维护成本高 |
| 运行时错误 | SQL/映射错误在运行期才发现 |
| 二级缓存局限 | 分布式一致性差，生产多用 Redis |
| 依赖数据库方言 | 换库可能要改 SQL |

## 适用场景

- 互联网业务、报表、SQL 调优敏感项目
- 团队熟悉 SQL，需要精细控制执行计划

## 面试要点

- 半自动 ORM：灵活 vs 开发效率的权衡。
- 与 JPA/Hibernate：MyBatis 偏 SQL 驱动，Hibernate 偏对象驱动。

## 面试一句话

> MyBatis 优点是可控 SQL 和灵活映射，缺点是 SQL 维护成本和运行时映射错误，适合重视 SQL 优化的项目。
