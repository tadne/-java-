# Math 类

`java.lang.Math` 为 **final** 工具类，不能实例化，方法均为 **static**。

## 常用方法

| 方法 | 说明 |
|------|------|
| `abs(x)` | 绝对值 |
| `ceil(double)` | 向上取整 |
| `floor(double)` | 向下取整 |
| `round(float/double)` | 四舍五入 |
| `max(a, b)` / `min(a, b)` | 较大/较小值 |
| `pow(a, b)` | a 的 b 次幂 |
| `random()` | `[0.0, 1.0)` 的 double 随机数 |

## 小结

- 数学运算工具类，全部静态方法
- 需要指定范围的随机数：`random() * n` 或 `ThreadLocalRandom`
