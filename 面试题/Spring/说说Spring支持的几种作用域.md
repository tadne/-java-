# 说说Spring支持的几种作用域

Bean **作用域**决定实例个数与生命周期。

## 作用域一览

| 作用域 | 说明 | 销毁 |
|--------|------|------|
| **singleton**（默认） | 容器内唯一实例 | 容器关闭 |
| **prototype** | 每次 `getBean` 新建 | **容器不管理**，需自行处理 |
| **request** | 每个 HTTP 请求一个实例 | 请求结束 |
| **session** | 每个 HTTP 会话一个实例 | 会话失效 |
| **application** | 每个 `ServletContext` 一个 | Web 应用停止 |
| **websocket** | 每个 WebSocket 一个 | 连接关闭 |

> `request` / `session` / `application` / `websocket` 仅在 Web 环境（`WebApplicationContext`）有效。

## singleton vs prototype

| | singleton | prototype |
|---|-----------|-----------|
| 实例数 | 1 | 每次获取新建 |
| 循环依赖 | 字段/setter 可三级缓存解决 | ❌ 不支持循环依赖 |
| 典型用途 | Service、Dao | 有状态、需隔离的对象 |

## request vs prototype（易混）

| | request | prototype |
|---|---------|-----------|
| 环境 | 仅 Web | 任意 |
| 销毁 | 容器管理 | 不管理 |
| 粒度 | 一次 HTTP 请求 | 每次 getBean |

## 配置方式

```java
@Component
@Scope("prototype")
public class TaskContext { }
```

```xml
<bean id="task" class="..." scope="prototype"/>
```

## 面试要点

- 默认 singleton；有状态慎用在单例中。
- prototype 不参与循环依赖三级缓存。
- Web 作用域把状态绑定到请求/会话。

## 面试一句话

> Spring 默认 singleton 单例；prototype 每次新建且容器不销毁；Web 还有 request、session 等作用域。
