# 为什么 wait/notify 不在 Thread 类

## 要点

| 项 | 说明 |
|---|---|
| 设计 | 任意对象可作锁，wait 在 Object |
| 模型 | 每个对象关联 Monitor |

## 面试一句话

> 等待/通知针对锁对象，Object 才有 Monitor，故在 Object 非 Thread。
