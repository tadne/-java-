# Synchronized 锁及其原理

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
