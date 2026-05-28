# 如何理解SpringBoot的Starters

## 什么是 Starter

**Starter** 是一组 curated 依赖描述符，把实现某功能所需的库打包在一起，并配合**自动配置**开箱即用。

命名：`spring-boot-starter-{name}`

## 工作原理

```
引入 starter
  → 传递依赖（带版本，由 BOM 管理）
  → 自动配置类（@ConditionalOnXxx）根据 classpath 生效
  → 可通过 application.yml 覆盖默认行为
```

## 常见 Starter

| Starter | 功能 |
|---------|------|
| `spring-boot-starter-web` | Web MVC + 内嵌 Tomcat + Jackson |
| `spring-boot-starter-data-jpa` | JPA + Hibernate |
| `spring-boot-starter-redis` | Redis + Lettuce |
| `spring-boot-starter-security` | Spring Security |
| `spring-boot-starter-test` | JUnit 5、Mockito、AssertJ |

## 版本管理

- 父 POM `spring-boot-starter-parent` 或导入 `spring-boot-dependencies` BOM
- 无需为每个依赖写版本号

## 自定义 Starter（了解）

1. `xxx-spring-boot-autoconfigure`：自动配置类
2. `xxx-spring-boot-starter`：依赖 autoconfigure + 第三方库
3. `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports`

## 面试要点

- Starter = **依赖聚合** + **自动配置**，不是新框架。
- 条件注解决定哪些 Bean 被创建。

## 面试一句话

> Starter 把相关依赖和自动配置打包在一起，引入即可用，版本由 Spring Boot BOM 统一管理。
