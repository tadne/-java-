# SpringBoot中的监视器是什么,作用,原理

监视器指 **Spring Boot Actuator**（生产级监控与管理），不是 `@EnableActuator`（正确为引入 starter 自动配置）。

## 是什么

- `spring-boot-starter-actuator` 提供一组 **HTTP/JMX 端点**
- 默认基础路径：`/actuator`（Boot 2.x+）

## 常用端点

| 端点 | 作用 |
|------|------|
| `/actuator/health` | 健康检查（数据库、磁盘等） |
| `/actuator/info` | 应用信息 |
| `/actuator/metrics` | 指标（JVM、HTTP、自定义） |
| `/actuator/loggers` | 查看/调整日志级别 |
| `/actuator/env` | 环境属性（生产需鉴权） |

## 配置示例

```yaml
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics
  endpoint:
    health:
      show-details: when_authorized
```

## 原理

1. 自动配置 `Endpoint` Bean
2. 通过 **MVC 或 WebFlux** 暴露 HTTP 端点
3. 与 **Micrometer** 集成，可对接 Prometheus、Grafana

## 安全

- 生产环境必须配合 **Spring Security** 限制端点访问
- 不要暴露 `env`、`beans` 等敏感端点到公网

## 面试要点

- Actuator = 监控 + 运维端点，依赖 Micrometer 指标体系。
- 生产要鉴权 + 最小暴露。

## 面试一句话

> Spring Boot Actuator 提供 health、metrics 等运维端点，基于自动配置和 Micrometer 实现应用监控。
