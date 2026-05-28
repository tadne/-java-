# 什么是 AQS

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
