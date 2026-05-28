# notify 和 notifyAll

## 要点

| 项 | 说明 |
|---|---|
| notify | 唤醒一个等待线程 |
| notifyAll | 唤醒全部，竞争锁 |

## 面试一句话

> notify 随机唤醒一个；notifyAll 全部唤醒再抢锁，更安全但开销大。
