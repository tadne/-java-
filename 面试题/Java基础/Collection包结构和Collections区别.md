# Collection 包结构和 Collections 区别

## 包结构（JDK 集合框架）

```
Collection
├── List    → ArrayList, LinkedList, Vector
├── Set     → HashSet, LinkedHashSet, TreeSet
└── Queue   → PriorityQueue, ArrayDeque

Map（独立接口）
→ HashMap, LinkedHashMap, TreeMap, Hashtable, ConcurrentHashMap
```

## Collection vs Collections

| | `Collection` | `Collections` |
|---|--------------|---------------|
| 类型 | **接口**（单列集合根） | **工具类**（静态方法） |
| 作用 | 定义 add/remove/size 等 | 排序、二分查找、同步包装、空集合等 |
| 实例化 | 不能 `new Collection()` | 不能实例化 |

## Collections 常用方法

- `sort`、`reverse`、`binarySearch`
- `synchronizedList/Map` 包装
- `emptyList`、`singletonList`

## 面试一句话

> Collection 是单列集合接口；Collections 是操作集合的静态工具类，二者完全不同。
