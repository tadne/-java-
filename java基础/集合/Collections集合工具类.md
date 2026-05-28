# Collections 集合工具类

## 说明

`java.util.Collections` **不是集合**，而是操作集合的**静态工具类**。

## 常用 API

| 方法 | 说明 |
|------|------|
| `addAll(Collection<T> c, T... elements)` | 批量添加 |
| `shuffle(List<?> list)` | 随机打乱顺序 |
| `sort(List<T> list)` | 自然排序 |
| `sort(List<T> list, Comparator<? super T> c)` | 指定比较器排序 |
| `binarySearch(List<? extends Comparable> list, T key)` | 二分查找（列表须已排序） |
| `copy(List<? super T> dest, List<? extends T> src)` | 复制元素 |
| `fill(List<? super T> list, T obj)` | 用指定值填充 |
| `max / min(Collection<T> coll)` | 最大/最小（自然序） |
| `swap(List<?> list, int i, int j)` | 交换两索引元素 |

## 面试要点

- 工具类，方法均为 `static`
- `sort` + `binarySearch` 需先保证有序
- 与 `Collection` 接口、集合实现类区分
