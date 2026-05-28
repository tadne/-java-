# CyclicBarrier 和 CountDownLatch 的区别

| 维度 | CountDownLatch | CyclicBarrier |
|------|----------------|---------------|
| 复用 | 一次性 | **可循环** reset |
| 等待方 | 一个或多个线程等计数归零 | 多个线程互相等到屏障点 |
| 实现 | AQS 共享，state=计数 | ReentrantLock + Condition |
| 典型场景 | 主线程等子任务完成 | 分阶段并行计算 |

## 面试一句话

> CountDownLatch 减到 0 放行且一般用一次；CyclicBarrier 多线程到齐再一起走，可重复使用。
