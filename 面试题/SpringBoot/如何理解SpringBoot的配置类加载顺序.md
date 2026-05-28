# 如何理解SpringBoot的配置类加载顺序

Spring Boot 从多个**属性源（PropertySource）**加载配置，**优先级高的覆盖低的**。

## 优先级（由高到低，常见）

| 优先级 | 来源 |
|--------|------|
| 1 | 命令行参数 `--key=value` |
| 2 | `SPRING_APPLICATION_JSON` 环境变量 / 系统属性 |
| 3 | `java -D` 系统属性 |
| 4 | 操作系统环境变量 |
| 5 | `application-{profile}.yml`（jar 外 > jar 内） |
| 6 | `application.yml` / `application.properties`（jar 外 > jar 内） |
| 7 | `@PropertySource` 指定文件 |
| 8 | 默认属性 `SpringApplication.setDefaultProperties` |

> 测试环境还有 `@TestPropertySource`、`@DynamicPropertySource` 等，优先级更高。

## profile

```yaml
spring:
  profiles:
    active: dev
```

加载 `application-dev.yml`，覆盖默认配置。

## bootstrap（Spring Cloud）

- `bootstrap.yml` 在 **application 之前**加载，用于配置中心（Nacos、Config Server）。
- 纯 Boot 项目通常只用 `application.yml`。

## yml vs properties

- 同一位置同时存在时，**properties 覆盖 yml**（后加载的 properties 优先，以 Boot 2.4+ 文档为准，面试答“后加载者优先”）。
- 建议项目统一用一种格式。

## 面试要点

- 口诀：**命令行 > 环境变量 > profile 文件 > 默认 application**。
- 外部 config 目录（`spring.config.location`）可覆盖 jar 内配置。

## 面试一句话

> Spring Boot 配置按属性源优先级加载，命令行和环境变量最高，application-{profile} 覆盖默认 application。
