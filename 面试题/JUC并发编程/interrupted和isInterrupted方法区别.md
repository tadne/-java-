# interrupted 和 isInterrupted 的区别

## 要点

| 项 | 说明 |
|---|---|
| interrupted() | 静态，清除中断标志，当前线程是否被中断 |
| isInterrupted() | 实例，不清除标志 |

## 面试一句话

> interrupted 清标志测当前线程；isInterrupted 只查询不清除。
