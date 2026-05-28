# 几种基于xml注入bean的方式

Spring 可通过 XML 配置 Bean 的定义与依赖注入（现代项目多用注解，但面试常考 XML 方式）。

## 四种方式

| 方式 | XML 要点 | 适用场景 |
|------|----------|----------|
| **构造器注入** | `<constructor-arg>` | 强制依赖、不可变对象 |
| **Setter 注入** | 无参构造 + `<property>` | 可选依赖、JavaBean 规范 |
| **静态工厂** | `factory-method` + class | 工厂类静态方法创建 Bean |
| **实例工厂** | `factory-bean` + `factory-method` | 由另一个 Bean 的实例方法创建 |

## 构造器注入示例

```xml
<bean id="car" class="com.example.Car">
    <constructor-arg name="speed" value="100"/>
    <constructor-arg name="engine" ref="engineBean"/>
</bean>
```

## Setter 注入示例

```xml
<bean id="car" class="com.example.Car">
    <property name="speed" value="100"/>
    <property name="engine" ref="engineBean"/>
</bean>
```

## 工厂方法示例

```xml
<!-- 静态工厂 -->
<bean id="userService" class="com.example.UserFactory"
      factory-method="createUserService"/>

<!-- 实例工厂 -->
<bean id="userService" factory-bean="userFactory" factory-method="create"/>
```

## 对比

| | 构造器 | Setter |
|---|--------|--------|
| 对象创建 | 有参构造，依赖必填 | 无参构造后设值 |
| 不可变字段 | 适合 | 需额外 setter |
| 循环依赖（单例） | 难 | 字段/setter 可配合三级缓存 |

## 面试要点

- 四种：构造器、setter、静态工厂、实例工厂。
- `constructor-arg` 的 name 对应构造器参数名（需编译保留参数名或 index/type）。
- 生产环境更常用 `@Configuration` + `@Bean` 或组件扫描。

## 面试一句话

> XML 注入 Bean 有构造器、setter、静态工厂、实例工厂四种，分别用 constructor-arg、property 和 factory-method 配置。
