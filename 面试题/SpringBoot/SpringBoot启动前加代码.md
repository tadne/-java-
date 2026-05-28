# SpringBoot启动前加代码

需区分 **容器启动前**、**Bean 初始化后**、**应用启动完成后** 三个时机。

## 时机对比

| 时机 | 方式 | 执行阶段 |
|------|------|----------|
| Bean 初始化后 | `@PostConstruct` | 单 Bean 创建完成、依赖注入后 |
| 容器就绪后 | `ApplicationRunner` / `CommandLineRunner` | **Spring 上下文已刷新完成** |
| 最早介入 | `ApplicationContextInitializer` | 上下文 refresh **之前** |
| 监听事件 | `ApplicationListener<ApplicationReadyEvent>` | 应用完全就绪 |

## ApplicationRunner（启动后逻辑，常用）

```java
@Component
public class InitRunner implements ApplicationRunner {
    @Override
    public void run(ApplicationArguments args) {
        // 初始化缓存、加载字典等
    }
}
```

## @PostConstruct（Bean 级）

```java
@Component
public class MyService {
    @PostConstruct
    public void init() {
        // 当前 Bean 初始化后执行
    }
}
```

## 注意

- `@PostConstruct` 不是“Boot 启动前”，而是**该 Bean 实例化之后**。
- 需要改 Banner、环境变量等极早逻辑用 `SpringApplication` 回调或 `ApplicationContextInitializer`。

## 面试要点

- 启动后任务：`ApplicationRunner`；Bean 内初始化：`@PostConstruct`。
- `CommandLineRunner` 与 `ApplicationRunner` 类似，参数形式不同。

## 面试一句话

> 启动后逻辑用 ApplicationRunner，Bean 初始化用 @PostConstruct，极早介入用 ApplicationContextInitializer。
