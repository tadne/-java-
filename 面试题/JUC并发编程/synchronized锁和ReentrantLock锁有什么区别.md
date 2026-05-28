# synchronized 和 ReentrantLock 的区别

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
