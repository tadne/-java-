# SpringBoot实现热部署有哪几种方式

热部署：修改代码或配置后**无需手动重启**即可生效（主要限开发环境）。

## 方式对比

| 方式 | 说明 | 场景 |
|------|------|------|
| **spring-boot-devtools** | 双 ClassLoader 快速重启 | 开发首选 |
| **JRebel** | 字节码热替换，商业 | 体验好，收费 |
| **Spring Loaded** | Java Agent 热替换 | 已较少使用 |

## Devtools 原理

- **Base ClassLoader**：加载不变依赖（第三方 jar）
- **Restart ClassLoader**：加载项目代码
- 文件变更 → 丢弃 Restart CL → 快速重启（比冷启动快，仍是一次上下文重启）

## 使用步骤

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-devtools</artifactId>
  <scope>runtime</scope>
  <optional>true</optional>
</dependency>
```

```yaml
spring:
  devtools:
    restart:
      enabled: true
      exclude: static/**,public/**
```

IDEA：开启 **Build project automatically** + 注册表 `compiler.automake.allow.when.app.running`。

## Restart vs Reload

| | Restart（devtools） | Reload（JRebel） |
|---|---------------------|------------------|
| 粒度 | 重启应用上下文 | 类级别热替换 |
| 速度 | 较快 | 更快 |

## 面试要点

- Devtools 是**快速重启**，不是不重启 JVM。
- 生产环境应关闭 devtools。

## 面试一句话

> 开发热部署常用 devtools 双类加载器快速重启，JRebel 可做字节码热替换，生产禁用 devtools。
