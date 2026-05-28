# 说说 ThreadLocal 原理

`ThreadLocal` 为**每个线程**提供独立的变量副本，实现线程间数据隔离，常用于无状态服务中传递用户上下文、数据库连接等。

## 核心结构

```
Thread
  └── threadLocals (ThreadLocalMap)
        └── Entry[] table
              Entry extends WeakReference<ThreadLocal<?>>
                key   → ThreadLocal 对象（弱引用）
                value → 业务数据（强引用）
```

- `ThreadLocalMap` 是 `Thread` 的成员，**以 Thread 为维度**存储数据
- 每个 `ThreadLocal` 对象作为 key，对应一个 value

## 常用方法

| 方法 | 行为 |
|------|------|
| `set(v)` | 当前线程的 Map 中放入 (this, v) |
| `get()` | 取当前线程 Map 中 key 为 this 的值；无则 `initialValue()` |
| `remove()` | 删除当前线程中该 ThreadLocal 的 Entry |

## 哈希与冲突

- 开放定址法，线性探测解决冲突
- 容量为 2 的幂，索引：`threadLocalHashCode & (len-1)`

## 内存泄漏（面试必考）

### 原因

- Entry 的 **key（ThreadLocal）是弱引用**，GC 后 key 可能为 null
- **value 是强引用**，若线程长期存活（如线程池），value 无法回收 → 泄漏

### 典型场景

```java
// 线程池 + ThreadLocal 未 remove
executor.execute(() -> {
    threadLocal.set(largeObject);
    // 任务结束未 remove，线程复用导致 largeObject 无法回收
});
```

### 解决

1. 使用完务必 `threadLocal.remove()`
2. 线程池场景用 `try-finally` 包裹
3. 避免在 ThreadLocal 中存大对象

## InheritableThreadLocal

- 子线程可继承父线程在创建时刻的副本
- **线程池下无效**（复用线程不会重新 inherit），需用 `TransmittableThreadLocal`（TTL）等方案

## 应用场景

| 场景 | 说明 |
|------|------|
| 用户上下文 | 拦截器 set，Controller/Service get |
| SimpleDateFormat | 每线程一份（更推荐 `DateTimeFormatter`） |
| 数据库连接（旧式） | 现代框架多用连接池，较少直接放 TL |

## 与 synchronized 对比

| | ThreadLocal | synchronized |
|---|-------------|--------------|
| 思路 | 空间换时间，各线程各一份 | 时间换空间，互斥访问 |
| 适用 | 线程隔离的上下文 | 共享资源互斥 |

## 面试一句话

> ThreadLocal 数据存在 Thread 的 ThreadLocalMap 中；key 弱引用、value 强引用，线程池必须 `remove()` 防内存泄漏。
