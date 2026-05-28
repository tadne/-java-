# 说说mybatis的缓存机制

MyBatis 提供**一级缓存**和**二级缓存**；生产环境热点数据更常用 **Redis** 等外部缓存。

## 两级缓存对比

| 级别 | 作用域 | 默认 | 说明 |
|------|--------|------|------|
| **一级缓存** | `SqlSession` | 开启 | 同一会话内相同 SQL+参数命中缓存 |
| **二级缓存** | `Mapper` 命名空间 | 关闭 | 跨 `SqlSession`，需显式开启 |

## 一级缓存

- 生命周期与 `SqlSession` 一致，关闭会话即失效。
- `localCacheScope`：
  - `SESSION`（默认）：同 Session 内缓存
  - `STATEMENT`：语句执行后清空，相当于不用一级缓存
- `update/insert/delete/commit/close` 会清空一级缓存。

## 二级缓存

- 需在 Mapper XML 中 `<cache/>` 或注解开启。
- 实体类需**可序列化**（缓存实现常基于序列化）。
- 多表关联、分布式场景慎用（脏读、一致性难保证）。

## 实现原理（简述）

- 底层用 `PerpetualCache`（HashMap）+ **装饰器**（LRU、FIFO、定时过期等）组成缓存链。

## 与 Redis

| | MyBatis 缓存 | Redis |
|---|--------------|-------|
| 粒度 | 会话/Mapper | 应用级、分布式 |
| 场景 | 简单本地加速 | 高并发、共享缓存 |

## 面试要点

- 一级 Session 级默认开；二级 Mapper 级默认关。
- 写操作会使相关缓存失效；分布式推荐 Redis 而非二级缓存。

## 面试一句话

> MyBatis 一级缓存绑定 SqlSession 默认开启，二级缓存跨 Session 需配置且生产多用 Redis 替代。
