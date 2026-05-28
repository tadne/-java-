# Mybatis中的设计模式

MyBatis 源码中大量运用经典设计模式。

## 常见模式

| 模式 | 体现 |
|------|------|
| **工厂模式** | `SqlSessionFactory`、`ObjectFactory`、`MapperProxyFactory` |
| **建造者模式** | `XMLConfigBuilder`、`XMLMapperBuilder`、`CacheBuilder` |
| **单例模式** | `ErrorContext`、部分工厂类 |
| **代理模式** | `MapperProxy`、延迟加载代理 |
| **模板方法** | `BaseExecutor` 定义执行流程，子类实现细节 |
| **装饰器模式** | 缓存装饰链（`LruCache`、`FifoCache` 包装 `PerpetualCache`） |
| **适配器模式** | 日志适配（Log4j、SLF4J 等） |
| **组合模式** | 动态 SQL 节点树（`SqlNode`） |
| **迭代器模式** | `PropertyTokenizer` 解析 OGNL 属性路径 |

## 执行链路（简）

```
SqlSession → Executor → StatementHandler → JDBC
                ↑ 插件 Interceptor 可拦截
```

## 面试要点

- 工厂 + 建造者负责对象创建；代理负责 Mapper 与懒加载。
- 插件机制基于**责任链式** Interceptor 包装四大对象。

## 面试一句话

> MyBatis 常用工厂、建造者、代理、装饰器、模板方法等模式，插件通过拦截 Executor 等对象扩展功能。
