# Vector 是线程安全的吗

## 要点

| 项 | 说明 |
|---|---|
| 结论 | 方法 synchronized，但复合操作非原子 |
| 替代 | Collections.synchronizedList 或 CopyOnWriteArrayList / Concurrent 包 |

## 面试一句话

> Vector 单方法同步，if-then-act 仍不安全；高并发用 JUC 容器。
