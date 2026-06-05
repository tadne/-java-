# Collection 单列集合

## 概述

- 一次只能添加一个数据。
- **顶层接口**：`Collection`
- **第二层接口**：`List` 和 `Set`

## 主要实现类

| 接口 | 实现类 |
|------|--------|
| **List** | `ArrayList`、`LinkedList`、`Vector`（已过时） |
| **Set** | `HashSet`、`TreeSet` |
| **HashSet 的子类** | `LinkedHashSet` |

## 常用方法

| 方法 | 说明 |
|------|------|
| `boolean add(E e)` | 添加元素 |
| `void clear()` | 清空所有元素 |
| `boolean remove(E e)` | 删除给定对象 |
| `boolean contains(Object o)` | 判断是否包含给定对象（引用类型需重写 `equals` 和 `hashCode`） |
| `boolean isEmpty()` | 判断集合是否为空 |
| `int size()` | 返回元素个数 |

## Set 系列集合特点

- **无序**：存和取的顺序可能不同
- **不重复**：集合中不同元素的值不能相同
- **无索引**：不能用普通 `for` 循环遍历

## 遍历方式

### 1. 迭代器遍历

```java
Collection<Integer> list = new ArrayList<>();
Iterator<Integer> it = list.iterator();
while (it.hasNext()) {
    Integer next = it.next();
    System.out.println(next);
}
```

**注意事项**：
- 超出集合范围还调用 `next()` 会报 `NoSuchElementException`
- 迭代器遍历完毕，指针不会复位
- 循环中只能用一次 `next()` 方法
- 迭代器遍历时，不能用集合的方法增加或删除元素，否则会报 `ConcurrentModificationException`
- 迭代器遍历不依赖索引

### 2. 增强 for 遍历

- 底层就是迭代器，为简化迭代器书写而出现
- JDK 5 后出现
- 所有单列集合和数组都能使用

```java
for (Integer s : list) {
    System.out.println(s);
}
```

### 3. Lambda 表达式遍历

```java
list.forEach(s -> System.out.println(s));
```

## 面试要点

- **List 的实现类**：`ArrayList`、`LinkedList`、`Vector`（已过时）
- **Set 的实现类**：`HashSet`、`TreeSet`
- **HashSet 的子类**：`LinkedHashSet`
- **Set 特点**：无序、不重复、无索引
- **遍历方式**：迭代器、增强 for、Lambda
