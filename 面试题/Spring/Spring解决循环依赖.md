# Spring 解决循环依赖

## 什么是循环依赖

两个或多个 Bean 相互依赖，形成闭环，例如：`A → B → A`。

## 能解决的前提（重要）

| 条件 | 能否解决 |
|------|----------|
| 单例 + 字段注入 / setter 注入 | ✅ 三级缓存 |
| **构造器注入** 循环 | ❌ 启动失败 |
| **prototype** 作用域循环 | ❌ 不支持 |
| `@Async` 等导致代理时机特殊 | 可能失败 |

> 面试必答：**构造器循环依赖 Spring 无法解决**，需改 setter/字段注入或 `@Lazy`。

## 三级缓存

| 缓存 | 名称 | 内容 |
|------|------|------|
| 一级 | `singletonObjects` | 完全初始化好的单例 |
| 二级 | `earlySingletonObjects` | 早期暴露的半成品（已实例化） |
| 三级 | `singletonFactories` | `ObjectFactory`，用于生成早期引用（**含 AOP 代理**） |

## 流程（A 依赖 B，B 依赖 A）

1. 创建 A，实例化后放入**三级**缓存（工厂）
2. 填充 A 的属性，需要 B → 去创建 B
3. 创建 B，实例化后放入三级，填充属性需要 A
4. 从三级工厂取 A 的早期引用（可能是**代理对象**）注入 B
5. B 完成初始化，进入一级缓存
6. A 拿到 B，完成初始化，进入一级缓存

## 为什么需要三级缓存

- 若只有二级：无法处理 **AOP 代理** 场景
- 三级 `ObjectFactory` 在需要时才调用 `getEarlyBeanReference()` 生成代理，保证注入的是最终代理对象

## 无法解决的例子

```java
@Service
public class A {
    public A(B b) { }  // 构造器注入 B
}
@Service
public class B {
    public B(A a) { }  // 构造器注入 A → 启动报错
}
```

**解决**：`@Lazy` 延迟注入、`@Autowired` 字段/setter、重构设计。

## 面试一句话

> 单例 Bean 的字段/setter 循环依赖靠三级缓存提前暴露早期引用；构造器和 prototype 循环依赖无法解决。
