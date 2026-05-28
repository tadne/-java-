# 为什么 wait/notify 要在同步块中

## 要点

| 项 | 说明 |
|---|---|
| 原因 | 依赖 Monitor，wait 释放锁前必须持有 |
| 否则 | IllegalMonitorStateException |

## 面试一句话

> wait/notify 操作 Monitor，必须先持有对象锁，故在 synchronized 内。
