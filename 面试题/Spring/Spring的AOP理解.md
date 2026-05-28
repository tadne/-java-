# Spring的AOP理解

AOP（Aspect-Oriented Programming）面向切面编程：在不修改业务代码的前提下，把日志、事务、权限等横切逻辑织入目标方法。

## 核心术语

| 术语 | 含义 |
|------|------|
| Join Point（连接点） | 可插入切面的位置；Spring AOP 仅支持**方法级别** |
| Pointcut（切点） | 真正要拦截的连接点集合，常用 `execution(...)` 表达式 |
| Advice（通知） | 切面逻辑：@Before、@After、@AfterReturning、@AfterThrowing、@Around |
| Aspect（切面） | 通知 + 切点，用 `@Aspect` 标记类 |
| Weaving（织入） | 把切面应用到目标对象；Spring 在**运行时**织入 |

## 通知类型

| 注解 | 时机 |
|------|------|
| @Before | 方法执行前 |
| @After | 方法执行后（含异常） |
| @AfterReturning | 正常返回后 |
| @AfterThrowing | 抛出异常后 |
| @Around | 环绕，可控制是否执行目标方法 |

## 代理方式（JDK vs CGLIB）

| 条件 | 代理实现 |
|------|----------|
| 目标类**实现了接口** | 默认 **JDK 动态代理**（基于接口） |
| 目标类**无接口** | **CGLIB** 子类代理 |
| `spring.aop.proxy-target-class=true` | 强制 CGLIB（Boot 2.x+ 常默认 true） |

> CGLIB 通过生成目标类的子类代理，不能代理 `final` 类/方法。

## 与 AspectJ 区别

| | Spring AOP | AspectJ |
|---|------------|---------|
| 织入时机 | 运行时代理 | 编译期/类加载期织入 |
| 能力 | 主要是方法拦截 | 字段、构造器等更全面 |

## 常见应用

- `@Transactional` 事务
- `@Cacheable` 缓存
- 自定义日志、权限、性能监控

## 面试要点

- Spring AOP 基于**动态代理**，默认只拦截**方法**。
- 有接口用 JDK Proxy，无接口用 CGLIB；可配置强制 CGLIB。
- `@Around` 功能最强，可决定是否调用 `proceed()`。

## 面试一句话

> Spring AOP 用 JDK 或 CGLIB 在运行时织入切面，只支持方法级连接点；有接口走 JDK 代理，否则 CGLIB 子类代理。
