# Java 线程池中队列常用类型

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
