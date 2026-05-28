# 什么时候会触发 Full GC

**Full GC** 通常回收**整堆**及与方法区相关的元数据（具体范围取决于收集器），伴随明显 **STW**，应尽量减少。

## 常见触发原因

| 原因 | 说明 |
|------|------|
| 老年代空间不足 | 晋升失败、长期存活对象过多、大对象 |
| **元空间不足** | 类加载过多，调 `-XX:MaxMetaspaceSize` 或排查类泄漏 |
| `System.gc()` | 建议式，生产慎用 |
| 分配担保失败 | Minor GC 前老年代连续空间不足（与收集器/参数有关） |
| G1  evacuation 失败 | 并发标记后回收跟不上分配 |
| CMS（历史） | promotion failed、concurrent mode failure |

> **易错**：元空间问题应调 Metaspace、减少无效类加载，**不是**“用 CMS 解决元空间”。

## 与 Minor GC 对比

| | Minor GC | Full GC |
|---|----------|---------|
| 范围 |  mainly 新生代 | 通常整堆 + 元数据相关 |
| 频率 | 较高 | 应低 |
| 停顿 | 通常较短 | 较长 |

## 收集器视角

| 收集器 | 备注 |
|--------|------|
| Parallel | Full GC 较常见，关注吞吐 |
| **G1** | Mixed GC，可设 `-XX:MaxGCPauseMillis` |
| **ZGC** | 并发为主，停顿极短（JDK 15+ 生产可用度提高） |

## 排查思路

1. 开启 GC 日志，看 `Full GC` 原因字段。
2. `jmap -heap`、`jstat` 看老年代、元空间趋势。
3. 代码：缓存、ThreadLocal 未 remove、大集合、频繁反射/动态代理类加载。

## 面试一句话

> Full GC 多因老年代或元空间不足、分配担保或 G1 失败；用日志定位原因，JDK 8+ 关注 Metaspace，生产优先 G1/ZGC 并减少无效 Full GC。
