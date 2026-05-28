# Lock 锁

## Lock 接口

`java.util.concurrent.locks.Lock` 是显式锁抽象，常用实现类 **`ReentrantLock`**（可重入）。

| 方法 | 说明 |
|------|------|
| `void lock()` | 获取锁（阻塞直到成功） |
| `void unlock()` | 释放锁，**必须在 `finally` 中调用** |

`Lock` 不能 `new`，需使用实现类：

```java
private static final Lock lock = new ReentrantLock();

public void method() {
    lock.lock();
    try {
        // 临界区
    } finally {
        lock.unlock();
    }
}
```

## 与 synchronized 对比（简述）

- `Lock`：可中断获取、尝试锁、公平锁、多条件 `Condition`
- `synchronized`：JVM 内置，语法简单，自动释放

## 面试要点

- 实现类常用 `ReentrantLock`
- `unlock()` 放 `finally`，避免异常导致死锁
- 多线程共享锁时可用 `static final Lock` 保证同一把锁
