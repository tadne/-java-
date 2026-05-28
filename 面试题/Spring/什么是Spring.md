# 什么是Spring

Spring 是开源的 **Java 企业级应用开发框架**，提供 IoC 容器、AOP、数据访问、Web、消息等一站式能力。

## 两大核心

| 核心 | 作用 |
|------|------|
| **IoC** | 控制反转，容器管理 Bean 与依赖 |
| **AOP** | 面向切面，统一处理事务、日志等横切逻辑 |

## 主要模块（Spring Framework 6 / Boot 3 时代）

| 模块 | 功能 |
|------|------|
| Core Container | Bean、DI、事件、SpEL |
| AOP | 切面、代理 |
| Data Access | JDBC、ORM 集成、事务 |
| Web MVC | Servlet 栈的 MVC |
| WebFlux | 响应式 Web（Reactor） |
| Test | 单元/集成测试支持 |
| Integration | 消息、邮件、调度等 |

## 与 Spring Boot 关系

- **Spring Framework**：基础能力。
- **Spring Boot**：约定优于配置 + 自动配置 + 内嵌容器，快速构建可运行应用。

## 优点（面试常答）

- 分层、模块化，可按需选用
- 生态成熟（Spring Cloud、Security、Data 等）
- 便于测试与扩展

## 面试要点

- Spring 核心是 IoC + AOP，不是单纯“另一个 MVC 框架”。
- Boot 是在 Framework 之上的快速启动与自动配置方案。

## 面试一句话

> Spring 是以 IoC 和 AOP 为核心的企业级开发框架，Boot 在其上提供自动配置与开箱即用。
