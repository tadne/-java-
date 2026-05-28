# ES 集群

Elasticsearch 集群由多个**节点（Node）**组成，通过**分片（Shard）**水平扩展数据，通过**副本（Replica）**保证高可用。

## 核心概念

| 概念 | 说明 |
|------|------|
| 集群 Cluster | 一个或多个节点集合，共享 cluster name |
| 节点 Node | 单台 ES 实例，角色：master / data / ingest |
| 索引 Index | 逻辑库，可拆成多个主分片 |
| 分片 Shard | 主分片（Primary）负责写；副本分片（Replica）负责读与容灾 |
| 文档 Document | 最小数据单元，带 `_id` |

## 分片与副本

- 创建索引时指定 `number_of_shards`（主分片数，创建后一般不改）
- `number_of_replicas` 可动态调整
- 写请求路由到主分片，再同步副本；读可走主或副本

## 集群状态

- **green**：主副分片齐全
- **yellow**：主分片齐全，部分副本未分配（单节点常见）
- **red**：部分主分片不可用，数据可能丢失风险

## 脑裂与 master

- 7.x 后引入**合格 master 节点**概念，避免多 master
- 生产建议 3 个 dedicated master 节点（小规模可混合角色）

## 面试要点

- 水平扩展靠增加分片与节点，而非单机堆内存
- 副本提高读吞吐与可用性，写仍走主分片
- 分片数规划：单分片建议 20～50GB，过多分片元数据压力大
- yellow 常见于单节点无副本槽位；red 需尽快恢复主分片
