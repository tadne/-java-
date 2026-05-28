# -*- coding: utf-8 -*-
"""Batch-enhance JVM/JUC interview notes."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKIP = {"面试题/JVM/简述JVM的内存模型.md"}

PROTECTED = {
    "面试题/JVM/MinorGC和FullGC.md",
    "面试题/JVM/什么是JVM,为什么java是无关平台的语言.md",
    "面试题/JVM/元空间代替永久代.md",
    "面试题/JUC并发编程/volatile关键字和能否保证有序性.md",
    "面试题/JUC并发编程/SynchronizeMap和ConcurentMap的区别.md",
    "面试题/JUC并发编程/常用线程池.md",
    "面试题/JUC并发编程/说说ThreadLocal原理.md",
}

CONTENT: dict[str, str] = {}

def add(rel: str, body: str) -> None:
    CONTENT[rel.replace("\\", "/")] = body.strip() + "\n"

# ---------- JVM ----------
add("面试题/JVM/垃圾回收算法.md", r"""# 垃圾回收算法

JVM 通过 GC 回收堆中不可达对象。不同代/收集器组合不同算法，面试需能对应到 **新生代 / 老年代** 及现代收集器（**G1、ZGC**）。

## 算法对比

| 算法 | 过程 | 优点 | 缺点 | 典型使用 |
|------|------|------|------|----------|
| 标记-清除 | 标记存活 → 清除未标记 | 实现简单 | 碎片、两次扫描 | CMS 老年代（已逐步淘汰） |
| 复制 | 存活对象复制到另一块，清空原区 | 快、无碎片 | 浪费一半空间 | **新生代**（Eden + Survivor） |
| 标记-整理 | 标记 → 存活对象向一端移动 | 无碎片 | 移动成本高 | **老年代** |
| 分代收集 | 新生代复制 + 老年代整理/清除 | 贴合对象生命周期 | 跨代引用需 remembered set | 默认分代模型 |

## 分代收集（核心）

| 区域 | 特点 | 常用算法 |
|------|------|----------|
| 新生代 | 朝生夕灭 | 复制（Minor GC） |
| 老年代 | 长期存活 | 标记-整理或标记-清除 |

## 与收集器的关系（了解）

| 收集器 | 说明 |
|--------|------|
| Serial / Parallel | JDK 8 常见默认，吞吐优先 |
| **G1** | 分区、可设停顿目标，JDK 9+ 默认 |
| **ZGC / Shenandoah** | 超低停顿，大堆、低延迟场景 |

> Full GC 频率应通过堆大小、对象晋升、元空间（**JDK 8+ Metaspace**）与代码优化控制，而非死记某一种算法名。

## 面试一句话

> 新生代多用复制、老年代多用标记-整理/清除；分代收集是工程组合，生产上常配合 G1/ZGC 等收集器调停顿与吞吐。
""")

add("面试题/JVM/说说java内存结构.md", r"""# 说说 Java 内存结构（运行时数据区）

> **易混**：本节是 **JVM 运行时数据区**（物理/逻辑划分），不是 **JMM**（并发可见性规范）。JMM 见 `简述JVM的内存模型.md`。

## 总览

| 区域 | 线程 | 作用 | 典型异常 |
|------|------|------|----------|
| 程序计数器 | 私有 | 当前字节码行号 | — |
| 虚拟机栈 | 私有 | 栈帧、局部变量、操作数栈 | StackOverflowError / OOM |
| 本地方法栈 | 私有 | Native 方法 | 同上 |
| **堆** | 共享 | 对象实例、数组 | OOM |
| **方法区（元空间）** | 共享 | 类元信息、常量、静态变量 | OOM（元空间） |
| 直接内存 | — | NIO `DirectBuffer` 等 | OOM |

## 堆

- 几乎所有 **对象实例** 在堆上分配（逃逸分析后可能栈上分配，见专题）。
- 分 **新生代**（Eden + Survivor）与 **老年代**，对应 Minor / Full GC。

## 方法区与 JDK 8

| 版本 | 实现 |
|------|------|
| JDK 7 及以前 | 永久代 PermGen（在堆逻辑划分内） |
| **JDK 8+** | **元空间 Metaspace**（本地内存，默认上限很大） |

## 与 JMM 的区别

| | 运行时数据区 | JMM |
|---|--------------|-----|
| 层次 | JVM 实现/规范中的内存划分 | 多线程读写语义 |
| 例子 | 堆、栈、元空间 | happens-before、volatile |

## 面试一句话

> 线程私有：PC、虚拟机栈、本地方法栈；线程共享：堆、方法区（JDK 8 为元空间）。不要与 JMM 混为一谈。
""")

add("面试题/JVM/常见的jvm调优命令和参数.md", r"""# 常见的 JVM 调优命令和参数

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
""")

add("面试题/JVM/什么时候会触发FullGC.md", r"""# 什么时候会触发 Full GC

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
""")

add("面试题/JVM/永久代什么时候发生垃圾回收.md", r"""# 永久代 / 元空间什么时候发生垃圾回收

## 版本差异（必答）

| 版本 | 类元数据存储 | GC 名称习惯 |
|------|--------------|-------------|
| JDK 7 及以前 | **永久代 PermGen**（堆内逻辑区域） | Full GC 时回收 PermGen |
| **JDK 8+** | **元空间 Metaspace**（本地内存） | 类卸载随 Full GC / G1 Mixed 等 |

> 面试答“永久代”时需说明：**JDK 8 起已被元空间取代**。

## 何时回收类元数据

- **Full GC** 时通常会扫描并卸载**不可达**的类（需类加载器也可回收）。
- **G1**：可 `-XX:+ClassUnloadingWithConcurrentMark` 等，在 Mixed 等阶段参与类卸载。
- 触发 Full GC 的常见诱因：老年代满、**Metaspace 满**、`System.gc()` 等。

## 类卸载条件（简述）

1. 该类所有实例已回收；
2. 加载该类的 `ClassLoader` 已回收；
3. 该类对应的 `java.lang.Class` 对象不可达。

> 由 **应用 ClassLoader** 加载的类在容器热部署场景更易出现元空间泄漏。

## 调优参数

| 版本 | 参数 |
|------|------|
| JDK 7 | `-XX:PermSize`、`-XX:MaxPermSize` |
| **JDK 8+** | `-XX:MetaspaceSize`、`-XX:MaxMetaspaceSize` |

## 面试一句话

> JDK 7 永久代在 Full GC 时回收；JDK 8+ 元空间在本地内存，类卸载依附 Full GC/G1 Mixed，满则调 Metaspace 或查类加载器泄漏。
""")

# Additional JVM files - continued in same dict
add("面试题/JVM/java中的对象结构.md", r"""# Java 中的对象结构

HotSpot 中普通对象在堆上由 **对象头 + 实例数据 + 对齐填充** 组成。

## 结构示意

```
┌─────────────┬──────────────┬────────────┐
│  对象头      │  实例数据     │  对齐填充   │
│ Mark Word   │  字段值       │  8字节对齐  │
│ Klass Ptr   │              │            │
└─────────────┴──────────────┴────────────┘
```

## 对象头（64 位压缩指针开启时典型）

| 部分 | 内容 |
|------|------|
| Mark Word | 哈希、GC 年龄、锁状态（无锁/偏向/轻量/重量） |
| Klass Pointer | 指向类元数据的指针（类型信息在**元空间**） |

## 实例数据

- 父类字段在前，子类在后；同访问性下 JVM 可能重排以压缩空间。

## 对齐填充

- 对象大小需为 **8 字节** 整数倍（默认）。

## 数组对象

- 对象头额外包含 **数组长度**。

## 面试一句话

> 对象 = 对象头（Mark Word + 类型指针）+ 实例数据 + 对齐；锁信息与 GC 分代年龄在 Mark Word 中。
""")

add("面试题/JVM/对象头包含哪些内容.md", r"""# 对象头包含哪些内容

## 组成（普通对象）

| 部分 | 作用 |
|------|------|
| **Mark Word** | 运行时元数据：哈希码、GC 分代年龄、锁标志位等 |
| **Klass Pointer** | 指向方法区/元空间中类的元数据，确定对象类型 |

数组对象另有 **length** 字段记录长度。

## Mark Word 与锁（64 位简化）

| 锁状态 | 说明 |
|--------|------|
| 无锁 | 哈希、年龄等 |
| 偏向锁 | 记录偏向线程 ID（JDK 15+ 默认关闭偏向，实现有变） |
| 轻量级锁 | 栈中 Lock Record 与 CAS |
| 重量级锁 | 指向 Monitor |

## 与 synchronized 关系

- 同步基于对象头的 Mark Word + Monitor（重量级时）。
- 锁升级路径（历史考点）：无锁 → 偏向 → 轻量 → 重量（具体以 JDK 版本为准）。

## 面试一句话

> 对象头含 Mark Word（哈希、GC 年龄、锁状态）和类型指针；synchronized 与锁升级都依赖 Mark Word。
""")

add("面试题/JVM/jvm中对象创建的过程.md", r"""# JVM 中对象创建的过程

## 流程概览

```
new 指令 → 类加载检查 → 分配内存 → 初始化零值 → 设置对象头 → <init> 构造方法
```

## 分步说明

| 步骤 | 说明 |
|------|------|
| 类加载检查 | 常量池能否解析类，类是否已加载、链接、初始化 |
| 分配内存 | **指针碰撞**（堆规整）或 **空闲列表**（有碎片）；**TLAB** 线程本地分配 |
| 初始化零值 | 保证实例字段有默认零值 |
| 设置对象头 | Mark Word、Klass 指针等 |
| 执行构造 | `<init>` 按源码顺序执行 |

## 并发安全

- 指针碰撞 + CAS 或 **TLAB** 避免多线程分配冲突。

## 逃逸分析（扩展）

- JVM 可能 **栈上分配**、标量替换，对象不一定总在堆上（见「对象一定分配在堆中吗」）。

## 面试一句话

> new → 检查类 → TLAB/堆分配 → 零值 → 对象头 → 构造方法；高并发分配靠 TLAB 与指针碰撞。
""")

add("面试题/JVM/什么是指针碰撞.md", r"""# 什么是指针碰撞

## 概念

堆内存**规整**（复制 GC 或标记-整理后无碎片）时，用一根 **bump pointer** 划分已用/未用：分配对象只需移动指针，称为**指针碰撞**（Bump the Pointer）。

## 对比空闲列表

| 方式 | 适用堆状态 | 分配成本 |
|------|------------|----------|
| 指针碰撞 | 内存规整 | 极低 |
| 空闲列表 | 有碎片 | 需遍历链表找块 |

## 线程安全

- 多线程同时 bump：CAS 更新指针，或每线程 **TLAB** 内先分配，用尽再同步申请新 TLAB。

## 面试一句话

> 指针碰撞用于规整堆的快速分配；有碎片则用空闲列表，配合 TLAB 降低锁竞争。
""")

add("面试题/JVM/什么是空闲列表.md", r"""# 什么是空闲列表

## 概念

堆存在**碎片**时（如标记-清除后），JVM 维护链表记录各**空闲块**，分配时遍历找足够大的块，称为**空闲列表**（Free List）。

## 与指针碰撞

| | 指针碰撞 | 空闲列表 |
|---|----------|----------|
| 前提 | 堆规整 | 有碎片 |
| 典型场景 | 复制后的新生代、整理后的区域 | CMS 老年代等 |

## 额外成本

- 分配、合并空闲块需维护链表，可能产生**外部碎片**。

## 面试一句话

> 堆不规整时用空闲列表找块分配；规整堆用指针碰撞，二者是分配策略的两种实现。
""")

add("面试题/JVM/什么是TLAB.md", r"""# 什么是 TLAB

**TLAB（Thread Local Allocation Buffer）** 是堆 Eden 中为**每个线程**划出的一小块私有缓冲区，用于**无锁**快速分配对象。

## 原理

| 要点 | 说明 |
|------|------|
| 位置 | 仍在 **Eden**（堆的一部分） |
| 流程 | 线程在自有 TLAB 内指针碰撞分配；用尽再申请新 TLAB（可能 CAS） |
| 目的 | 减少多线程竞争 Eden 全局指针 |

## 相关参数（了解）

- `-XX:+UseTLAB`（默认开启）
- `-XX:TLABSize`、`-XX:ResizeTLAB` 等

## 面试一句话

> TLAB 是线程在 Eden 的私有分配缓冲，多数对象先在 TLAB 里分配，降低同步开销。
""")

add("面试题/JVM/对象一定分配在堆中吗.md", r"""# 对象一定分配在堆中吗

**不一定。** 规范层面对象在堆上；JVM 可通过**逃逸分析**做优化，使部分对象不占用堆。

## 逃逸分析

| 逃逸程度 | 优化可能 |
|----------|----------|
| 未逃逸 | 栈上分配、标量替换、锁消除 |
| 方法逃逸 | 优化受限 |
| 线程逃逸 | 必须堆上，线程间可见 |

## 常见优化

| 优化 | 说明 |
|------|------|
| **栈上分配** | 对象未逃出方法，在栈帧销毁时一并回收 |
| **标量替换** | 不建对象，拆成局部变量 |
| **锁消除** | 仅单线程使用的同步 |

## 开启（了解）

- `-XX:+DoEscapeAnalysis`（默认开启，以 JDK 为准）

## 面试一句话

> 语法上 new 在堆；JVM 对未逃逸对象可栈上分配或标量替换，故“对象一定在堆上”不严谨。
""")

add("面试题/JVM/说说对象分配规则.md", r"""# 说说对象分配规则

## 分配路径（HotSpot 常见）

| 顺序 | 规则 |
|------|------|
| 1 | **栈上分配**（逃逸分析通过） |
| 2 | **TLAB** 在 Eden 分配 |
| 3 | Eden 全局分配（指针碰撞） |
| 4 | **大对象** 可能直接进入老年代（`-XX:PretenureSizeThreshold`，Parallel 等） |
| 5 | **长期存活** 对象晋升老年代（年龄达 `-XX:MaxTenuringThreshold`） |
| 6 | **动态年龄** | Survivor 同年龄对象大小超 Survivor 一半，大于等于该年龄的对象晋升 |

## 分代示意

```
新对象 → Eden → (Minor GC) → Survivor 复制 → 年龄增加 → 老年代
```

## 与收集器

- **G1**：大对象进 Humongous 区；仍遵循分代思想但物理分区不同。
- 调优需结合 GC 日志，而非死记阈值。

## 面试一句话

> 优先 TLAB/Eden，大对象与高龄对象进老年代；未逃逸可栈上分配，具体阈值看 JVM 参数与收集器。
""")

add("面试题/JVM/判断一个对象是否可以被回收.md", r"""# 判断一个对象是否可以被回收

## 可达性分析（主流）

从 **GC Roots** 出发，不可达的对象可被回收（并非立即回收）。

### 常见 GC Roots

| 类型 | 示例 |
|------|------|
| 线程栈局部变量 | 栈帧中的引用 |
| 静态变量 | 方法区/元空间中类静态字段 |
| 常量 | 运行时常量池引用 |
| JNI 引用 | Native 方法引用的对象 |
| 同步锁 | 持有 Monitor 的对象 |
| JVM 内部引用 | 系统类加载器等 |

## 两次标记（finalize）

1. 第一次标记：不可达；
2. 若覆写 `finalize()` 且未执行过，放入 F-Queue 一次机会复活；
3. 第二次标记仍不可达则真正回收。

> **不推荐**依赖 `finalize`，JDK 9+ 已废弃相关机制倾向。

## 引用类型（补充）

| 引用 | 回收时机 |
|------|----------|
| 强 | 永不因引用类型本身回收 |
| 软 | OOM 前清理 |
| 弱 | 下次 GC |
| 虚 | 无法通过虚引用取对象，用于堆外清理跟踪 |

## 面试一句话

> 以 GC Roots 可达性为准；finalize 仅一次机会且不可靠，实际开发避免依赖。
""")

add("面试题/JVM/jvm的主要组成部分和作用.md", r"""# JVM 的主要组成部分和作用

## 组成

| 部分 | 作用 |
|------|------|
| **类加载子系统** | 加载、验证、准备、解析、初始化 Class |
| **运行时数据区** | PC、栈、堆、方法区/元空间、直接内存等 |
| **执行引擎** | 解释执行 + JIT 编译 |
| **本地接口 JNI** | 调用 Native 库 |
| **垃圾收集器** | 自动回收堆中无用对象 |

## 与 JDK/JRE 关系

| 组件 | 说明 |
|------|------|
| JRE | JVM + 核心类库 |
| JDK | JRE + 开发工具（javac、javadoc 等） |

## 跨平台

- `.java` → 字节码 → 各平台 JVM 解释/编译执行，实现**一次编译，到处运行**。

## 现代 GC（了解）

- 生产常见 **G1**；低延迟大堆可看 **ZGC**、Shenandoah。

## 面试一句话

> JVM = 类加载 + 运行时数据区 + 执行引擎 + GC + JNI；字节码在各平台由 JVM 运行。
""")

add("面试题/JVM/jvm类的生命周期.md", r"""# JVM 类的生命周期

## 七个阶段

```
加载 → 验证 → 准备 → 解析 → 初始化 → 使用 → 卸载
```

| 阶段 | 要点 |
|------|------|
| 加载 | 读字节流，生成 `Class` 对象，元数据进**元空间** |
| 验证 | 文件格式、元数据、字节码、符号引用 |
| 准备 | 静态变量零值（`static final` 常量可能直接赋值） |
| 解析 | 符号引用转直接引用 |
| 初始化 | `<clinit>` 执行静态块与静态变量赋值 |
| 使用 | 创建实例、调用方法 |
| 卸载 | 类、ClassLoader、实例都不可达时（较少见） |

## 主动初始化触发（部分）

- `new`、读取/赋值静态字段（非 final 编译期常量）、调用静态方法；
- 反射、子类初始化触发父类、主类（含 `main`）等。

## 面试一句话

> 类生命周期：加载链接初始化到使用，卸载需 ClassLoader 可回收；元数据在 JDK 8+ 存在 Metaspace。
""")

add("面试题/JVM/说说类加载和卸载.md", r"""# 说说类加载和卸载

## 类加载器层次（JDK 8）

| 加载器 | 加载范围 |
|--------|----------|
| Bootstrap | `lib` 核心类，`null` 表示 C++ 实现 |
| Extension | `lib/ext`（模块化后变化） |
| Application | `classpath` 用户类 |
| 自定义 | 继承 `ClassLoader`，如 Tomcat、SPI |

## 双亲委派

- 子加载器先委派父加载器；父无法加载子再加载。
- 目的：防止核心类被替换（如自定义 `java.lang.String`）。

## 打破双亲委派（了解）

- SPI（线程上下文类加载器）、OSGi、热部署等。

## 类卸载

- 需：实例全回收、加载该类的 **ClassLoader** 可回收、对应 `Class` 不可达。
- 应用服务器反复部署易导致 **元空间** 泄漏。

## 面试一句话

> 双亲委派保证核心类安全；卸载难，热部署要关注 ClassLoader 与 Metaspace 泄漏。
""")

add("面试题/JVM/说说堆和栈的区别.md", r"""# 说说堆和栈的区别

| 维度 | 栈（虚拟机栈） | 堆 |
|------|----------------|-----|
| 存储 | 栈帧、局部变量表、操作数栈 | 对象实例、数组 |
| 线程 | 每线程私有 | 所有线程共享 |
| 生命周期 | 方法调用创建/销毁栈帧 | 由 GC 管理 |
| 大小 | 较小，`-Xss` | 较大，`-Xms/-Xmx` |
| 异常 | StackOverflowError、OOM | OOM |
| 分配速度 | 快（移动栈指针） | 相对慢，涉及 GC |
| 引用关系 | 栈中引用指向堆中对象 | — |

## 易混

- **本地方法栈**：Native 方法。
- **方法区/元空间**：类元数据，不是“堆里的栈”。

## 与 JMM

- 栈变量线程私有，无可见性问题；堆上共享对象需 volatile、锁等保证 JMM 语义。

## 面试一句话

> 栈存栈帧和局部变量、线程私有；堆存对象、共享并由 GC 管理；栈引用指向堆中对象。
""")

add("面试题/JVM/什么是STW,什么是OopMap,什么是安全点.md", r"""# 什么是 STW、OopMap、安全点

## Stop-The-World（STW）

- GC 或部分 GC 阶段需要**暂停所有应用线程**，保证引用关系不变。
- **Minor GC** STW 通常较短；**Full GC**、部分老年代收集 STW 更长。
- **G1/ZGC** 目标缩短 STW，但并非完全无停顿。

## 安全点（Safepoint）

- 线程执行到**安全点**时才能暂停（如方法调用、循环回边等）。
- 不能在任意字节码中间停，否则栈上引用不一致。

## 安全区域（Saferegion）

- 线程处于 Sleep/Blocked 等无法跑到安全点时，进入安全区域，仍可参与 GC 根扫描。

## OopMap

- 记录**栈帧里哪些槽位是引用**（Ordinary Object Pointer Map）。
- GC 扫描根集合时根据 OopMap 找引用，避免把 int 当指针。

## 关系

```
应用运行 → 到达 Safepoint → STW → 根据 OopMap 扫描根 → GC → 恢复
```

## 面试一句话

> STW 暂停业务线程做 GC；只能在安全点停；OopMap 标记栈上哪些是对象引用供根扫描。
""")

# ---------- JUC (representative batch - script continues) ----------
add("面试题/JUC并发编程/对JMM内存模型的理解,为什么需要JMM.md", r"""# 对 JMM 的理解，为什么需要 JMM

## 是什么

**JMM（Java Memory Model）** 是规范，定义多线程下**共享变量**的可见性、有序性与 happens-before 规则，**不是** JVM 堆栈那种运行时数据区。

## 为什么需要

| 问题 | 没有 JMM 时 |
|------|-------------|
| CPU 缓存 | 每核一份缓存，写不一定立即可见 |
| 指令重排 | 编译器/CPU 优化改变执行顺序 |
| 平台差异 | 不同硬件内存模型不一致 |

JMM 屏蔽硬件差异，让 Java 并发语义**可移植、可推理**。

## 主内存与工作内存（抽象）

| 概念 | 含义 |
|------|------|
| 主内存 | 共享变量存储（对应堆等） |
| 工作内存 | 线程本地缓存副本（抽象，非严格等于虚拟机栈） |

## 如何保证三大特性

| 机制 | 可见性 | 有序性 | 原子性 |
|------|--------|--------|--------|
| `volatile` | ✅ | ✅（hb） | ❌ `i++` |
| `synchronized` | ✅ | ✅ | ✅ 块内 |
| `java.util.concurrent` | 视 API | 视 API | CAS、锁 |

## 与运行时数据区

- **JMM**：并发**语义**（happens-before）。
- **运行时数据区**：JVM **内存布局**（堆、栈、元空间）。

## 面试一句话

> JMM 统一多线程内存语义，解决缓存与重排；与堆栈划分是两层概念，volatile/锁实现其规则。
""")

add("面试题/JUC并发编程/什么是AQS.md", r"""# 什么是 AQS

**AQS（AbstractQueuedSynchronizer）** 是 JUC 同步器框架：**volatile state + CLH 双向队列 + CAS**。

## 核心结构

| 组件 | 作用 |
|------|------|
| `state` | 同步状态（重入次数、许可数等） |
| CLH 队列 | 封装等待线程 Node，FIFO |
| CAS | 原子改 state、入队/出队 |

## state 状态机（独占锁示例）

| state | 含义（ReentrantLock） |
|-------|------------------------|
| 0 | 未占用 |
| 1 | 被占用一次 |
| n | 重入 n 次 |

获取：`tryAcquire` CAS 0→1 或重入 +1；失败 → 入队 park；释放：`tryRelease` 减到 0 唤醒后继。

## 两种模式

| 模式 | 代表 | 关键方法 |
|------|------|----------|
| 独占 | `ReentrantLock` | `tryAcquire` / `tryRelease` |
| 共享 | `Semaphore`、`CountDownLatch` | `tryAcquireShared` / `tryReleaseShared` |

## 子类举例

| 类 | state 含义 |
|----|------------|
| ReentrantLock | 重入次数 |
| Semaphore | 剩余许可 |
| CountDownLatch | 计数 |

## Condition

- 基于 AQS 的 **Condition 队列**，与 Lock 配合 `await`/`signal`。

## 面试一句话

> AQS 用 volatile state 表示锁/许可状态，CLH 队列排队，CAS 竞争；独占/共享两套模板，JUC 锁与同步器多基于它实现。
""")

add("面试题/JUC并发编程/线程池的原理和核心参数.md", r"""# 线程池的原理和核心参数

基于 **`ThreadPoolExecutor`**，不要用 `Executors` 无界队列工厂掩盖 OOM 风险。

## 执行流程

```
任务提交
  → 线程数 < core？新建核心线程
  → 否则入队
  → 队列满且线程 < max？新建非核心线程
  → 否则拒绝策略
```

## 七大参数

| 参数 | 含义 |
|------|------|
| corePoolSize | 核心线程数 |
| maximumPoolSize | 最大线程数 |
| keepAliveTime + unit | 非核心线程空闲存活时间 |
| workQueue | **有界队列优先**（ArrayBlockingQueue 等） |
| threadFactory | 命名、守护线程等 |
| handler | 拒绝策略 |

## 常用队列

| 队列 | 特点 |
|------|------|
| ArrayBlockingQueue | 有界数组，需指定容量 |
| LinkedBlockingQueue | 可指定容量；默认 `Integer.MAX_VALUE` 近似无界 |
| SynchronousQueue | 不存元素，直接交接 |
| DelayQueue / PriorityBlockingQueue | 定时、优先级 |

> `Executors.newFixedThreadPool` / `newSingleThreadExecutor` 使用**无界** `LinkedBlockingQueue`，高负载易 **OOM**——阿里规范建议显式 `ThreadPoolExecutor`。

## 拒绝策略

| 策略 | 行为 |
|------|------|
| AbortPolicy | 抛异常（默认） |
| CallerRunsPolicy | 调用线程执行 |
| DiscardPolicy | 丢弃 |
| DiscardOldestPolicy | 丢最老任务 |

## submit vs execute

| | execute | submit |
|---|---------|--------|
| 返回值 | void | Future |
| 异常 | 线程未捕获则打出 | 封装在 Future.get() |

## 面试一句话

> 任务先填满核心线程再入队，队满扩到 max 再拒绝；生产用 ThreadPoolExecutor + 有界队列，慎用 Executors 无界工厂。
""")

add("面试题/JUC并发编程/Synchronized锁及其原理.md", r"""# Synchronized 锁及其原理

`synchronized` 保证**互斥**与 JMM 下的**可见性、有序性**（释放-获取锁的 happens-before）。

## 使用方式

| 写法 | 锁对象 |
|------|--------|
| 实例方法 | `this` |
| 静态方法 | 类的 Class 对象 |
| 同步块 | 指定对象 |

## 底层

- 基于 **Monitor**（对象头 Mark Word + 重量级 Monitor）。
- 字节码：`monitorenter` / `monitorexit`（异常路径也需释放）。

## 锁优化（JDK 6+，了解）

| 阶段 | 场景 |
|------|------|
| 偏向锁 | 单线程反复获取（新 JDK 默认策略有调整） |
| 轻量级锁 | 低竞争，CAS |
| 重量级锁 | 竞争激烈，阻塞入队 |

## 与 ReentrantLock

| | synchronized | ReentrantLock |
|---|--------------|---------------|
| 释放 | 自动 | 需 unlock |
| 尝试/超时/中断 | 不支持 | 支持 |
| 公平锁 | 非公平 | 可选公平 |

## 面试一句话

> synchronized 基于 Monitor 与对象头，自动释放；JDK 6+ 有锁升级优化，高阶功能用 ReentrantLock（AQS）。
""")

# ... more JUC entries generated by helper below

def juc_rest():
    items = {
        "面试题/JUC并发编程/CAS原理.md": """# CAS 原理

**CAS（Compare And Swap）** 比较内存值与期望值，相等则更新，硬件保证**单条指令**原子性。

## 三要素

| 要素 | 说明 |
|------|------|
| 内存地址 V | 要更新的变量 |
| 期望值 A | 认为当前应是 A |
| 新值 B | 成功则写 B |

## 与 AQS / 原子类

- `AtomicInteger` 等基于 CAS；AQS 用 CAS 改 `state`、入队。

## 问题

| 问题 | 解决思路 |
|------|----------|
| ABA | `AtomicStampedReference` 版本号 |
| 自旋开销 | 限制次数、改锁 |
| 只能保证一个变量 | 组合用锁或 `AtomicReference` |

## 面试一句话

> CAS 是 CPU 级比较交换，原子类与 AQS 的基础；有 ABA 与自旋开销，复合逻辑仍需锁。
""",
        "面试题/JUC并发编程/CyclicBarrier和CountDownLatch的区别.md": """# CyclicBarrier 和 CountDownLatch 的区别

| 维度 | CountDownLatch | CyclicBarrier |
|------|----------------|---------------|
| 复用 | 一次性 | **可循环** reset |
| 等待方 | 一个或多个线程等计数归零 | 多个线程互相等到屏障点 |
| 实现 | AQS 共享，state=计数 | ReentrantLock + Condition |
| 典型场景 | 主线程等子任务完成 | 分阶段并行计算 |

## 面试一句话

> CountDownLatch 减到 0 放行且一般用一次；CyclicBarrier 多线程到齐再一起走，可重复使用。
""",
        "面试题/JUC并发编程/synchronized锁和ReentrantLock锁有什么区别.md": """# synchronized 和 ReentrantLock 的区别

| 维度 | synchronized | ReentrantLock |
|------|--------------|---------------|
| 层面 | JVM 关键字 | API（基于 AQS） |
| 释放 | 自动 | 必须 unlock，常配合 try-finally |
| 公平 | 非公平 | 可选公平/非公平 |
| 尝试/超时/可中断 | 无 | lock/tryLock/lockInterruptibly |
| 条件队列 | 单个 wait/notify | 多个 Condition |
| 性能 | JDK 6+ 优化后相近 | 高竞争下灵活 |

## 选型

- 简单同步：`synchronized`。
- 需要超时、可中断、公平或多条件队列：`ReentrantLock`。

## 面试一句话

> synchronized 简单自动；ReentrantLock 基于 AQS，支持公平、可中断、多 Condition，需手动释放。
""",
        "面试题/JUC并发编程/锁的优化机制.md": """# 锁的优化机制

## synchronized 侧（JVM）

| 机制 | 说明 |
|------|------|
| 偏向锁 | 单线程无竞争时减少 CAS |
| 轻量级锁 | CAS 自旋，避免阻塞 |
| 重量级锁 | Monitor 阻塞 |
| 锁消除 | 逃逸分析证明仅单线程使用 |
| 锁粗化 | 连续加锁合并 |

## volatile / 其他

- 轻量同步用 volatile（可见+有序，不保证 i++）。
- `LongAdder` 分段减少热点 CAS。

## 面试一句话

> JVM 对 synchronized 有偏向/轻量/重量升级与锁消除；高并发计数用 LongAdder 而非 volatile++。
""",
        "面试题/JUC并发编程/什么是Semaphore.md": """# 什么是 Semaphore

计数信号量，控制同时访问资源的**线程数**（或许可数），基于 **AQS 共享模式**。

## 常用 API

| 方法 | 作用 |
|------|------|
| `acquire()` | 获取 1 许可，不足则阻塞 |
| `acquire(n)` | 获取 n 个 |
| `release()` | 释放许可 |

## 与 synchronized

| | Semaphore | synchronized |
|---|-----------|--------------|
| 同时持有者 | 多个（≤许可数） | 一个 |
| 用途 | 限流、连接池 | 互斥 |

## 面试一句话

> Semaphore 是共享 AQS，state 表示许可数，用于限流与资源池，非互斥锁。
""",
        "面试题/JUC并发编程/线程池的核心线程数怎么设置.md": """# 线程池的核心线程数怎么设置

无万能公式，需结合 **CPU/IO 比例** 与压测。

## 经验起点

| 类型 | 参考 |
|------|------|
| CPU 密集 | `N` 或 `N+1`（N=核数） |
| IO 密集 | `2N` 或 `N/(1-阻塞系数)` |
| 混合型 | 拆分线程池 |

## 注意

- 队列有界 + 拒绝策略，避免 `Executors` 无界队列 OOM。
- 业务线程池与定时/IO 池隔离。

## 面试一句话

> CPU 密集接近核数，IO 密集可更大；最终以压测为准，并配有限队列与拒绝策略。
""",
        "面试题/JUC并发编程/线程池中的submit方法和execute方法的区别.md": """# 线程池中 submit 和 execute 的区别

| | execute | submit |
|---|---------|--------|
| 接口 | Executor | ExecutorService |
| 参数 | Runnable | Runnable / Callable |
| 返回值 | void | Future |
| 异常 | 未捕获则线程组处理 | 封装进 Future，get 时 ExecutionException |

## 面试一句话

> execute 无返回；submit 返回 Future，异常在 get 时抛出，适合需要结果或 Callable 的场景。
""",
        "面试题/JUC并发编程/Java线程池中队列常用类型.md": """# Java 线程池中队列常用类型

| 队列 | 有界 | 说明 |
|------|------|------|
| ArrayBlockingQueue | ✅ 需指定 | 数组，一把锁 |
| LinkedBlockingQueue | 可指定；默认很大 | 两把锁，生产慎用默认容量 |
| SynchronousQueue | 容量 0 | 直接交付，Cached 线程池用 |
| PriorityBlockingQueue | 无界 | 优先级 |
| DelayQueue | 无界 | 延迟到期才可取 |

> 生产推荐 **显式有界** `ArrayBlockingQueue` 或指定容量的 `LinkedBlockingQueue`。

## 面试一句话

> 线程池队列优先有界 ArrayBlockingQueue；Linked 默认近似无界，Executors 工厂易埋 OOM 隐患。
""",
    }
    for k, v in items.items():
        add(k, v)

juc_rest()

# Auto-generate remaining JUC/JVM files with template if not in CONTENT
TEMPLATES = {
    "java创建线程的三种方式": ("# Java 创建线程的三种方式", [
        ("继承 Thread", "重写 run，不推荐（单继承）"),
        ("实现 Runnable", "任务与线程分离，推荐"),
        ("实现 Callable + Future", "有返回值，可抛异常"),
        ("线程池", "生产首选，复用线程"),
    ], "创建线程优先线程池；Runnable/Callable 解耦任务，Callable 用 Future 取结果。"),
}

def generic_juc(filename: str) -> str | None:
    base = filename.replace(".md", "")
    mapping = {
        "interrupted和isInterrupted方法区别": (
            "# interrupted 和 isInterrupted 的区别",
            [("interrupted()", "静态，清除中断标志，当前线程是否被中断"),
             ("isInterrupted()", "实例，不清除标志")],
            "interrupted 清标志测当前线程；isInterrupted 只查询不清除。"
        ),
        "yield方法的作用": (
            "# yield 方法的作用",
            [("作用", "提示调度器让出 CPU，进入就绪"),
             ("注意", "不释放锁，不保证一定切换")],
            "yield 仅让出 CPU 机会，不释放锁，语义弱于 sleep/wait。"
        ),
        "Vector是线程安全的": (
            "# Vector 是线程安全的吗",
            [("结论", "方法 synchronized，但复合操作非原子"),
             ("替代", "Collections.synchronizedList 或 CopyOnWriteArrayList / Concurrent 包")],
            "Vector 单方法同步，if-then-act 仍不安全；高并发用 JUC 容器。"
        ),
        "什么是线程安全": (
            "# 什么是线程安全",
            [("定义", "多线程下结果与单线程一致"),
             ("手段", "不可变、锁、CAS、线程封闭、ThreadLocal")],
            "线程安全靠互斥、不可变或隔离；volatile 不保证 i++ 原子。"
        ),
        "线程安全要保证几个基本特征": (
            "# 线程安全要保证几个基本特征",
            [("原子性", "不可分割"),
             ("可见性", "修改对其他线程可见"),
             ("有序性", "hb 与 volatile/synchronized")],
            "并发三性：原子性、可见性、有序性；volatile 只管后两者。"
        ),
        "线程和进程": (
            "# 线程和进程",
            [("进程", "资源分配单位，独立内存"),
             ("线程", "调度单位，共享进程堆和方法区")],
            "进程隔离资源，线程共享进程空间，切换更轻。"
        ),
        "多线程的作用": (
            "# 多线程的作用",
            [("优点", "提高 CPU 利用、IO 并发、响应"),
             ("代价", "上下文切换、同步、调试难度")],
            "多线程提升吞吐与响应，需权衡同步开销与复杂度。"
        ),
        "java程序是如何运行的": (
            "# Java 程序是如何运行的",
            [("编译", "javac → 字节码"),
             ("运行", "JVM 加载、解释 + JIT"),
             ("线程", "main 线程启动，可再起工作线程")],
            "源码编译为字节码，由 JVM 加载执行，JIT 热点编译；并发受 JMM 约束。"
        ),
        "Thread类中的start方法和run方法有什么区别": (
            "# start 和 run 的区别",
            [("start", "启动新线程，JVM 调用 run"),
             ("run", "普通方法，直接调用不建新线程")],
            "start 异步新线程；直接 run 仍在当前线程同步执行。"
        ),
        "sleep方法和wait方法有什么区别": (
            "# sleep 和 wait 的区别",
            [("所属", "Thread.sleep vs Object.wait"),
             ("锁", "sleep 不释放；wait 释放"),
             ("唤醒", "sleep 时间到；wait 需 notify")],
            "sleep 不释放锁且属 Thread；wait 释放锁须在同步块且属 Object。"
        ),
        "notify方法和notifyall方法的区别": (
            "# notify 和 notifyAll",
            [("notify", "唤醒一个等待线程"),
             ("notifyAll", "唤醒全部，竞争锁")],
            "notify 随机唤醒一个；notifyAll 全部唤醒再抢锁，更安全但开销大。"
        ),
        "为什么wait和notofy要在同步块中调用": (
            "# 为什么 wait/notify 要在同步块中",
            [("原因", "依赖 Monitor，wait 释放锁前必须持有"),
             ("否则", "IllegalMonitorStateException")],
            "wait/notify 操作 Monitor，必须先持有对象锁，故在 synchronized 内。"
        ),
        "为什么wait方法和notify方法不在Thread类中": (
            "# 为什么 wait/notify 不在 Thread 类",
            [("设计", "任意对象可作锁，wait 在 Object"),
             ("模型", "每个对象关联 Monitor")],
            "等待/通知针对锁对象，Object 才有 Monitor，故在 Object 非 Thread。"
        ),
        "产生死锁的四个必要条件及其避免方式": (
            "# 死锁四个必要条件与避免",
            [("互斥", "资源独占"),
             ("占有且等待", "持有并等待其他"),
             ("不可剥夺", "只能自愿释放"),
             ("循环等待", "成环等待链")],
            "死锁需四条件同时成立；破坏任一即可，如固定加锁顺序、tryLock 超时。"
        ),
        "停止正在运行的线程": (
            "# 停止正在运行的线程",
            [("推荐", "协作式：volatile 标志 + 中断"),
             ("不推荐", "stop/suspend 已废弃"),
             ("中断", "interrupt + 检查 interrupted 状态")],
            "用中断或标志位协作停止；勿用 stop，线程池任务要响应 interrupt。"
        ),
        "什么是多线程的上下文切换": (
            "# 什么是多线程上下文切换",
            [("含义", "保存/恢复线程 PC、栈、寄存器"),
             ("开销", "频繁切换降低有效 CPU")],
            "切换保存线程状态有开销；减少竞争、合理线程数可降低切换。"
        ),
        "什么是阻塞队列,阻塞队列的实现原理是什么": (
            "# 阻塞队列及原理",
            [("特点", "队满 put 阻塞，队空 take 阻塞"),
             ("实现", "ReentrantLock + Condition await/signal"),
             ("应用", "线程池、生产者消费者")],
            "阻塞队列用锁与 Condition 实现满/空等待，是线程池与生产者消费者基础。"
        ),
        "使用阻塞队列实现生产者消费者模型": (
            "# 阻塞队列实现生产者消费者",
            [("方案", "ArrayBlockingQueue put/take"),
             ("优点", "无需手写 wait/notify")],
            "用 BlockingQueue 的 put/take 自动阻塞，比手写 wait/notify 简洁安全。"
        ),
        "如何保证线程顺序执行": (
            "# 如何保证线程顺序执行",
            [("单线程池", "同一 Executor 顺序"),
             ("join", "等待前一线程结束"),
             ("CompletableFuture", "thenApply 链式")],
            "同一线程池单线程、join 或 CompletableFuture 链保证顺序。"
        ),
        "线程间的通信": (
            "# 线程间的通信",
            [("wait/notify", "配合 synchronized"),
             ("Condition", "Lock 多条件队列"),
             ("阻塞队列", "生产者消费者")],
            "通信可用 wait/notify、Condition 或 BlockingQueue，注意在锁内 wait。"
        ),
        "引用类型有哪些有什么区别": (
            "# 引用类型有哪些",
            [("强", "默认，不回收"),
             ("软", "OOM 前回收，缓存"),
             ("弱", "下次 GC，WeakHashMap"),
             ("虚", "跟踪回收，PhantomReference")],
            "强软弱虚回收时机递增强；软做缓存，弱做关联映射，虚做堆外清理通知。"
        ),
        "什么是Daemon线程,有什么用": (
            "# Daemon 线程",
            [("定义", "守护线程，JVM 退出时不等待"),
             ("用途", "后台服务如 GC 辅助"),
             ("设置", "start 前 setDaemon(true)")],
            "守护线程随 JVM 结束而终止，不能用于必须执行完的业务逻辑。"
        ),
        "Synchronized关键字的使用": (
            "# Synchronized 关键字的使用",
            [("实例方法", "锁 this"),
             ("静态方法", "锁 Class"),
             ("同步块", "锁指定对象")],
            "synchronized 可修饰方法或块，锁对象分别为实例、Class 或指定对象。"
        ),
    }
    if base not in mapping:
        return None
    title, rows, one = mapping[base]
    lines = [title, "", "## 要点", "", "| 项 | 说明 |", "|---|---|"]
    for a, b in rows:
        lines.append(f"| {a} | {b} |")
    lines.extend(["", "## 面试一句话", "", f"> {one}"])
    return "\n".join(lines) + "\n"


def main():
    modified = []
    for d in [ROOT / "面试题" / "JVM", ROOT / "面试题" / "JUC并发编程"]:
        for f in sorted(d.glob("*.md")):
            rel = str(f.relative_to(ROOT)).replace("\\", "/")
            if rel in SKIP or rel in PROTECTED:
                continue
            ql = sum(1 for ln in f.read_text(encoding="utf-8").splitlines() if ln.strip())
            has = "面试一句话" in f.read_text(encoding="utf-8")
            if has and ql > 55:
                continue
            body = CONTENT.get(rel)
            if not body:
                body = generic_juc(f.name)
            if not body:
                print("MISSING", rel)
                continue
            f.write_text(body, encoding="utf-8")
            modified.append(rel)
    print("MODIFIED", len(modified))
    for m in modified:
        print(m)


if __name__ == "__main__":
    main()
