# volatile 关键字：可见性、有序性与原子性

`volatile` 是 Java 提供的轻量级同步机制，主要保证**可见性**和**禁止特定重排序**（从而保证有序性语义），**不能**保证复合操作的原子性。

## 三大特性对照

| 特性 | volatile 能否保证 | 说明 |
|------|-------------------|------|
| 可见性 | ✅ | 写 volatile 后，其他线程读能见到最新值 |
| 有序性 | ✅（有限） | 通过内存屏障禁止部分重排序 |
| 原子性 | ❌（复合操作） | `i++`、`count++` 仍非原子 |

## 可见性

- 对 `volatile` 变量的写，会立即刷新到主内存
- 对 `volatile` 变量的读，会从主内存读取最新值
- 普通变量可能被线程缓存在工作内存，其他线程看不到最新值

## 有序性（happens-before）

JMM 规定：对 volatile 变量的写 happens-before 后续对该变量的读。

典型禁止的重排序：

- 写 volatile 之前的操作，不能重排到写之后
- 读 volatile 之后的操作，不能重排到读之前

## 原子性（易错点）

### volatile 能保证的

- 对 **单个** volatile 变量的**单次读或单次写**具有原子性
- 例如：`volatile boolean flag = true;`

### volatile 不能保证的

```java
volatile int count = 0;
count++;  // 读-改-写三步，多线程仍会丢失更新
```

`long`/`double` 的非 volatile 读写可能非原子（与 JVM 实现有关），用 `volatile` 修饰可保证 64 位读写原子性——这是特例，**不代表** `i++` 变原子。

### 需要原子性时用什么

- `java.util.concurrent.atomic.*`（`AtomicInteger` 等）
- `synchronized` / `Lock`
- `LongAdder`（高并发计数）

## 内存屏障（了解）

编译器/CPU 在 volatile 读写前后插入屏障，实现可见性与有序性，例如：

- **StoreLoad**：写 volatile 后、读 volatile 前的全屏障，开销最大

## 使用场景

| 场景 | 是否适合 volatile |
|------|---------------------|
| 状态标志位（如 `boolean running`） | ✅ |
| 双重检查锁（DCL）单例中的实例引用 | ✅ |
| 多线程计数器 | ❌，用 Atomic 类 |
| 保证多个变量整体一致 | ❌，用锁 |

## 面试一句话

> volatile 保证可见性和有序性，不保证 `i++` 这类复合操作的原子性；需要原子性用 CAS 或锁。
