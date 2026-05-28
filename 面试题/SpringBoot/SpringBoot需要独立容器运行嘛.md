# SpringBoot需要独立容器运行嘛

## 结论

**不需要。** Spring Boot 默认内嵌 Web 容器，打成可执行 JAR 即可运行。

## 内嵌容器

| 容器 | Starter |
|------|---------|
| Tomcat（默认） | `spring-boot-starter-web` |
| Jetty | 排除 tomcat 引入 jetty |
| Undertow | 排除 tomcat 引入 undertow |

```bash
java -jar myapp.jar
```

## 部署到外部容器（可选）

1. 打包方式改为 **WAR**
2. 主类继承 `SpringBootServletInitializer`
3. 部署到 Tomcat 10+（Boot 3 需 Jakarta Servlet 6）

```java
@SpringBootApplication
public class Application extends SpringBootServletInitializer {
    @Override
    protected SpringApplicationBuilder configure(SpringApplicationBuilder builder) {
        return builder.sources(Application.class);
    }
}
```

## 对比

| 方式 | 优点 |
|------|------|
| 可执行 JAR | 部署简单、云原生友好 |
| 外部 WAR | 符合传统企业 Tomcat 运维规范 |

## 面试要点

- 默认内嵌 Tomcat，独立容器非必须。
- Boot 3 使用 `jakarta.*` 包名，外部容器需匹配版本。

## 面试一句话

> Spring Boot 默认内嵌 Tomcat，java -jar 即可运行，也可打 WAR 部署外部容器。
