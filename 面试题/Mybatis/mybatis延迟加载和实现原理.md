# mybatis延迟加载和实现原理

## 什么是延迟加载

查询主对象时**不立即**查询关联对象，在**第一次访问**关联属性时才执行第二条 SQL（懒加载）。

## 配置（常用）

```xml
<settings>
  <setting name="lazyLoadingEnabled" value="true"/>
  <setting name="aggressiveLazyLoading" value="false"/>
</settings>
```

或在 association/collection 上设置 `fetchType="lazy"`。

## 实现原理

1. MyBatis 为包含关联属性的对象创建 **代理对象**（CGLIB 或 Javassist）。
2. 访问关联属性时，代理拦截 getter，触发嵌套 `select`。
3. 通过 **插件 + 反射** 完成二次查询并填充属性。

```
查询 User → 返回 User 代理
调用 getOrders() → 执行 OrderMapper.selectByUserId
```

## 注意

- 仅对 **嵌套查询**（`select` 属性）的 association/collection 生效，联表查询本身是一次 SQL。
- 在代理对象外关闭 `SqlSession` 可能报 `LazyInitializationException`（类似 Hibernate）。
- 注意 **N+1** 问题，列表查询慎用全局懒加载。

## 面试要点

- 懒加载 = 代理 + 嵌套查询延迟执行。
- 联表一次查出不存在“延迟”第二条 SQL 的问题。

## 面试一句话

> MyBatis 延迟加载用代理包装实体，首次访问关联属性时才执行嵌套 SQL，需开启 lazyLoadingEnabled。
