# CAS 原理

**CAS（Compare And Swap）** 比较内存值与期望值，相等则更新，硬件保证**单条指令**原子性。

## 三要素

| 要素 | 说明 |
|------|------|
| 内存地址 V | 要更新的变量 |
| 期望值 A | 认为当前应是 A |
| 新值 B | 成功则写 B |

## 与 AQS / 原子类

- `AtomicInteger` 等基于 CAS；AQS 用 CAS 改 `state`、入队。

## 问题

| 问题 | 解决思路 |
|------|----------|
| ABA | `AtomicStampedReference` 版本号 |
| 自旋开销 | 限制次数、改锁 |
| 只能保证一个变量 | 组合用锁或 `AtomicReference` |

## 面试一句话

> CAS 是 CPU 级比较交换，原子类与 AQS 的基础；有 ABA 与自旋开销，复合逻辑仍需锁。
