# Spring的IOC理解

## IoC 是什么

**控制反转（Inversion of Control）**：对象的创建、依赖关系、生命周期由 **容器**管理，调用方不再 `new` 或自行组装依赖。

**依赖注入（DI）** 是 IoC 最常见的实现方式。

## 两种容器

| 容器 | 特点 |
|------|------|
| `BeanFactory` | 基础 IoC，默认延迟加载 |
| `ApplicationContext` | 增强版：事件、国际化、资源加载、AOP 等；启动时初始化单例 Bean |

实际开发几乎都用 **ApplicationContext**（如 `AnnotationConfigApplicationContext`、Boot 的上下文）。

## Bean 是什么

- 由容器管理的对象，元数据在 **BeanDefinition** 中（类名、作用域、属性、依赖等）。
- 定义方式：XML、`@Component` 扫描、`@Bean` 方法。

## 三种注入方式（Spring 官方推荐顺序）

| 方式 | 说明 | 推荐度 |
|------|------|--------|
| **构造器注入** | 依赖在创建时注入，易保证不可变、易测 | 首选 |
| **Setter 注入** | 可选依赖、可重新注入 | 可选依赖时用 |
| **字段注入** | `@Autowired` 直接标字段 | 简洁但不利于测试，不推荐在核心类滥用 |

## 实例化方式

- 反射调用构造器（默认）
- 静态/实例工厂方法（`FactoryBean`）

## 面试要点

- IoC 管“谁创建、谁装配”；DI 管“依赖怎么传进来”。
- 构造器注入利于不可变对象；字段注入不利于单元测试。
- `ApplicationContext` = `BeanFactory` + 企业级特性。

## 面试一句话

> IoC 把对象创建和依赖交给 Spring 容器，通过构造器、setter 或字段注入实现，实际使用 ApplicationContext 作为容器。
