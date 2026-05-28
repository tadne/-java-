# Java 的四种引用（强、软、弱、虚）

> 严格说是 **4 种引用类型** + 终结器引用（FinalReference，与 `finalize` 机制相关，JDK 9+ 已废弃 `finalize`）。

## 对比总览

| 类型 | 类 | GC 行为 | 典型用途 |
|------|-----|---------|----------|
| 强引用 | 普通 `new` | 有引用就不回收 | 日常对象 |
| 软引用 | `SoftReference` | 内存不足前可能回收 | 内存敏感缓存 |
| 弱引用 | `WeakReference` | 下次 GC 即回收 | `ThreadLocal`、WeakHashMap |
| 虚引用 | `PhantomReference` | 无法通过 get 获得对象，用于跟踪回收 | 堆外内存清理、监控对象回收 |

## 强引用（Strong Reference）

```java
Object obj = new Object();  // 强引用
obj = null;                 // 断开引用，对象才可被 GC
```

- GC Roots 可达则绝不回收（除非 OOM 前仍无法满足分配）

## 软引用（SoftReference）

- **内存够**：不回收
- **内存紧张**：回收软引用对象，再不够才抛 OOM

```java
ReferenceQueue<byte[]> queue = new ReferenceQueue<>();
SoftReference<byte[]> softRef = new SoftReference<>(new byte[1024 * 1024], queue);
byte[] data = softRef.get();  // 可能为 null（已被回收）
```

- 适合：图片缓存、网页缓存等**可重建**数据
- 可配合 `ReferenceQueue` 做清理回调

## 弱引用（WeakReference）

- **只要发生 GC**（不论内存是否充足），弱引用对象就会被回收

```java
WeakReference<Object> weak = new WeakReference<>(new Object());
System.out.println(weak.get());  // GC 前可能非 null，GC 后多为 null
```

- `WeakHashMap`：key 为弱引用，key 无强引用时可被回收
- `ThreadLocalMap` 的 key 为弱引用 ThreadLocal

## 虚引用（PhantomReference）

- `get()` **永远返回 null**，不能用来访问对象
- 对象被回收时，虚引用进入 `ReferenceQueue`，用于**跟踪回收事件**

```java
PhantomReference<Object> phantom = new PhantomReference<>(obj, queue);
// 用于 DirectByteBuffer 等：对象回收后清理堆外内存（Cleaner 机制）
```

> **易错**：虚引用不是“发现即回收”的弱引用，而是**无法获取对象、仅用于回收跟踪**。

## 引用队列 ReferenceQueue

- 当引用对象所指向的对象被回收后，引用本身会入队
- 用于：软/弱引用清理、虚引用触发的堆外内存释放

## 终结器引用（了解，不推荐）

- 与已废弃的 `Object.finalize()` 相关
- 对象第一次 GC 时进入队列，由低优先级 `Finalizer` 线程执行 `finalize()`，**第二次 GC** 才可能回收对象
- **JDK 9+**：`finalize` 已废弃，改用 `Cleaner` / `PhantomReference`

## 面试一句话

> 强引用不回收；软引用内存不足才回收；弱引用下次 GC 回收；虚引用不能 get，用于回收跟踪和堆外内存清理。
