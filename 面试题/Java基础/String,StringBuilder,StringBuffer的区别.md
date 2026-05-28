# String、StringBuilder、StringBuffer 的区别

## 对比表

| | String | StringBuilder | StringBuffer |
|---|--------|---------------|--------------|
| 可变性 | **不可变** | 可变 | 可变 |
| 线程安全 | 天然不可变即安全 | 否 | 是（方法 synchronized） |
| 性能 | 拼接产生新对象 | 单线程快 | 多线程安全但慢 |
| 使用场景 | 常量、少量拼接 | 单线程大量拼接 | 已少用，优先 Builder |

## 常量池

- 字面量进字符串池；`intern()` 可复用池中引用

## 面试一句话

> String 不可变；StringBuilder 可变非线程安全；StringBuffer 可变且同步，高并发拼接用 Builder+外部同步或别的方式。
