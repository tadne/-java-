# Spring中用了哪些设计模式

Spring 在 IoC、AOP、Web 等模块中大量运用经典设计模式。

## 常见模式一览

| 模式 | Spring 中的体现 |
|------|-----------------|
| **工厂模式** | `BeanFactory` / `ApplicationContext` 创建与管理 Bean；`FactoryBean` 自定义工厂 |
| **单例模式** | 默认 `singleton` 作用域；内部 `singletonObjects`（一级缓存） |
| **代理模式** | AOP：`JDK Proxy` / `CGLIB`；`RestTemplate` 等对底层 API 的封装 |
| **模板方法** | `JdbcTemplate`、`JmsTemplate`、`RedisTemplate` 固定流程、子类/回调填细节 |
| **观察者模式** | `ApplicationEvent` / `ApplicationListener` 事件机制 |
| **适配器模式** | `HandlerAdapter` 适配不同 Controller；Spring MVC 多种 View 适配 |
| **装饰器模式** | `BeanWrapper`；缓存装饰器链（MyBatis 同类思路） |
| **策略模式** | `Resource` 加载（classpath、file、url）；多种 `TransactionManager` |
| **责任链模式** | Servlet `Filter` 链；`HandlerInterceptor` 链 |

## AOP 代理（面试高频）

| 场景 | 实现 |
|------|------|
| 目标有接口 | JDK 动态代理 |
| 目标无接口 | CGLIB 子类代理 |

## BeanFactory vs ApplicationContext

| | BeanFactory | ApplicationContext |
|---|-------------|-------------------|
| 定位 | 基础 IoC 容器 | 增强容器（事件、国际化、AOP 等） |
| 默认加载 | 延迟（getBean 时） | 启动时预实例化单例（非懒加载） |

## 面试要点

- 工厂 + 单例是 IoC 核心；AOP 用代理模式。
- MVC 中 `DispatcherServlet` 协调多个策略/适配器组件。
- 能说清 JDK 与 CGLIB 选用条件加分。

## 面试一句话

> Spring 核心是工厂+单例管理 Bean，AOP 用 JDK/CGLIB 代理，此外还有模板方法、观察者、适配器、责任链等模式。
