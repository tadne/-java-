# 为什么使用SpringBoot

Spring Boot 基于 Spring Framework，通过**自动配置**和**起步依赖**实现快速构建可运行的 Spring 应用。

## 核心价值

| 价值 | 说明 |
|------|------|
| **开箱即用** | 内嵌 Tomcat/Jetty/Undertow，无需部署 WAR |
| **自动配置** | 根据 classpath 和配置自动装配 Bean |
| **简化依赖** | Starter 统一管理版本，避免冲突 |
| **生产就绪** | Actuator 监控、外部化配置、健康检查 |

## 对比传统 Spring

| 传统 Spring | Spring Boot |
|-------------|-------------|
| 大量 XML / JavaConfig | 约定优于配置 |
| 手动配 Servlet 容器 | 内嵌容器，`java -jar` 运行 |
| 依赖版本自己协调 | BOM（`spring-boot-dependencies`） |

## 常用工具

- `spring-boot-devtools`：开发热重启
- `spring-boot-starter-test`：测试支持
- `spring-boot-starter-actuator`：监控端点

## 面试要点

- Boot 不是新框架，是 Spring 的快速启动与自动配置方案。
- 核心：`@SpringBootApplication` = 配置 + 自动配置 + 组件扫描。

## 面试一句话

> Spring Boot 用自动配置和 Starter 简化 Spring 开发与部署，内嵌容器一条命令即可运行。
