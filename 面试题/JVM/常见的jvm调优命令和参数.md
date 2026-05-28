# 常见的 JVM 调优命令和参数

## 诊断命令

| 命令 | 作用 |
|------|------|
| `jps` | 列出 Java 进程 PID、主类 |
| `jstat` | GC、类加载、编译等统计（如 `jstat -gcutil pid 1s`） |
| `jmap` | 堆概要、`-dump` 生成堆转储 |
| `jstack` | 线程栈、死锁检测 |
| `jcmd` | 统一诊断（JDK 7+，推荐） |
| `jconsole` / `jvisualvm` / MAT | 图形化监控与分析 |

> `jhat` 已过时，堆分析多用 **MAT**、**VisualVM**、**async-profiler** 等。

## 常用 JVM 参数

| 类别 | 参数示例 | 说明 |
|------|----------|------|
| 堆 | `-Xms`、`-Xmx` | 初始/最大堆，建议设成相同避免扩容 |
| 新生代 | `-Xmn`、`-XX:NewRatio`、`-XX:SurvivorRatio` | 新生代大小与 Eden/Survivor 比例 |
| 元空间 | `-XX:MetaspaceSize`、`-XX:MaxMetaspaceSize` | **JDK 8+**，非 PermSize |
| 栈 | `-Xss` | 每线程栈大小 |
| 直接内存 | `-XX:MaxDirectMemorySize` | NIO DirectBuffer |
| GC 日志 | `-Xlog:gc*`（JDK 9+） | 分析停顿与原因 |

## 收集器选择（面试常问）

| 场景 | 建议 |
|------|------|
| 吞吐优先 | Parallel GC |
| 均衡、可设停顿目标 | **G1**（`-XX:+UseG1GC`，JDK 9+ 默认） |
| 超大堆、极低停顿 | **ZGC**、Shenandoah |

> CMS 在 JDK 14 移除；面试答 PermGen 调优应改为 **Metaspace**。

## 调优原则

1. 先度量（GC 日志、APM），再改参数。
2. 减少 Full GC：合理堆、避免泄漏、控制类加载。
3. 慎用 `System.gc()`。

## 面试一句话

> 用 jstat/jmap/jstack 定位问题；JDK 8 调元空间与 G1/ZGC，堆用 -Xms/-Xmx，先证据后调参。
