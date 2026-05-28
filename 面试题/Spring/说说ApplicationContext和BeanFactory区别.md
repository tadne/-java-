# 说说ApplicationContext和BeanFactory区别

两者都是 Spring **IoC 容器**，`ApplicationContext` 继承 `BeanFactory`。

## 核心对比

| 对比项 | BeanFactory | ApplicationContext |
|--------|-------------|-------------------|
| 定位 | 基础 IoC 容器 | 企业级增强容器 |
| 功能 | Bean 创建、获取、依赖注入 | 事件、国际化、资源、AOP、环境抽象等 |
| 单例初始化 | 默认**延迟**（getBean 时） | 默认**预实例化**单例（非 @Lazy） |
| 常用实现 | `DefaultListableBeanFactory` | `AnnotationConfigApplicationContext`、Boot 上下文 |
| 实际使用 | 框架内部、扩展场景 | **开发主流** |

## ApplicationContext 额外能力

- 发布 `ApplicationEvent`
- 统一访问 `Resource`（classpath、file）
- 自动注册 `BeanPostProcessor`（AOP 等）
- 集成 `Environment`（profile、属性源）

## SpEL

- `ApplicationContext` 支持 **SpEL**（`#{...}`）在配置中引用 Bean、运算。
- 纯 `BeanFactory` 不直接提供 SpEL 集成。

## 面试要点

- ApplicationContext **is-a** BeanFactory，功能更全。
- 面试答：日常用 ApplicationContext；BeanFactory 更底层、延迟加载。
- Boot 启动后本质是 `ApplicationContext`。

## 面试一句话

> ApplicationContext 是 BeanFactory 的子接口，增加事件、资源、AOP 等能力并默认预初始化单例，是实际开发使用的容器。
