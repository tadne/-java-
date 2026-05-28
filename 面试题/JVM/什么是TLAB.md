# 什么是 TLAB

**TLAB（Thread Local Allocation Buffer）** 是堆 Eden 中为**每个线程**划出的一小块私有缓冲区，用于**无锁**快速分配对象。

## 原理

| 要点 | 说明 |
|------|------|
| 位置 | 仍在 **Eden**（堆的一部分） |
| 流程 | 线程在自有 TLAB 内指针碰撞分配；用尽再申请新 TLAB（可能 CAS） |
| 目的 | 减少多线程竞争 Eden 全局指针 |

## 相关参数（了解）

- `-XX:+UseTLAB`（默认开启）
- `-XX:TLABSize`、`-XX:ResizeTLAB` 等

## 面试一句话

> TLAB 是线程在 Eden 的私有分配缓冲，多数对象先在 TLAB 里分配，降低同步开销。
