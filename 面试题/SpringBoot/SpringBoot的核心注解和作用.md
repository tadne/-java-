# SpringBoot的核心注解和作用

## @SpringBootApplication

组合注解，等价于：

| 注解 | 作用 |
|------|------|
| `@SpringBootConfiguration` | 标记配置类（本质是 `@Configuration`） |
| `@EnableAutoConfiguration` | 启用自动配置（加载 `META-INF/spring/*.imports`） |
| `@ComponentScan` | 扫描当前包及子包组件（默认主类所在包） |

## @EnableAutoConfiguration 原理（简）

1. 加载 `spring.factories` / `AutoConfiguration.imports` 中的自动配置类
2. 根据 `@ConditionalOnXxx` 条件决定是否生效
3. 与 `application.yml` 属性绑定

## 其他常用注解

| 注解 | 作用 |
|------|------|
| `@RestController` | REST 控制器 |
| `@ConfigurationProperties` | 批量绑定配置前缀 |
| `@ConditionalOnProperty` | 按配置开关 Bean |

## 启动类示例

```java
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

## 面试要点

- 一个注解启动：配置类 + 自动配置 + 扫描。
- 自动配置是 Boot 的核心，由条件注解控制加载。

## 面试一句话

> @SpringBootApplication 组合了配置、自动配置和组件扫描，是 Spring Boot 应用的启动入口注解。
