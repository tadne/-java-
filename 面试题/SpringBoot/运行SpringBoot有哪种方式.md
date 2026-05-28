# 运行SpringBoot有哪种方式

## 三种常见方式

| 方式 | 命令/操作 | 场景 |
|------|-----------|------|
| **IDE 运行** | 运行主类 `main` | 开发调试 |
| **Maven/Gradle** | `mvn spring-boot:run` / `gradle bootRun` | 开发、CI |
| **可执行 JAR** | `java -jar app.jar` | **生产部署** |

## 可执行 JAR 原理

- `spring-boot-maven-plugin` 打 **fat jar**
- 内嵌容器随应用启动，`Main-Class` 为 `JarLauncher`

```bash
mvn clean package -DskipTests
java -jar target/myapp-0.0.1-SNAPSHOT.jar
```

## 外部容器（WAR）

- 继承 `SpringBootServletInitializer`
- 打包 WAR 部署到 Tomcat（Boot 3 需 Jakarta EE 9+ 容器）

## 面试要点

- 默认不需要外部 Tomcat，内嵌容器即可。
- 生产标准：`java -jar` + 外部化配置。

## 面试一句话

> Spring Boot 可 IDE 运行、Maven 插件运行，或打 fat jar 用 java -jar 部署，内嵌容器无需外部 Tomcat。
