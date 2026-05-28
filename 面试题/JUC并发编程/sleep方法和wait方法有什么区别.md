# sleep 和 wait 的区别

## 要点

| 项 | 说明 |
|---|---|
| 所属 | Thread.sleep vs Object.wait |
| 锁 | sleep 不释放；wait 释放 |
| 唤醒 | sleep 时间到；wait 需 notify |

## 面试一句话

> sleep 不释放锁且属 Thread；wait 释放锁须在同步块且属 Object。
