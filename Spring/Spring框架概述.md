# Spring 框架概述

## Spring 概述和入门

- Spring 是一个开源的轻量级框架，简化企业级应用开发，解决了开发者在 Java EE 开发中遇到的常见问题。
- 提供了 IOC、AOP、Web MVC 等功能，生态完善。

### 历史演进

- JSP 开发
- MVC + 三层架构
- EJB 重量级框架
- Spring + SSH（Spring + Struts + Hibernate）
- Spring + SSM（Spring + SpringMVC + MyBatis）
- Spring Boot
- Spring Cloud

## BeanFactory

- 一个工厂类（接口），用于管理 Bean 的生产和管理。
- IOC 容器的核心接口，负责实例化、定位、配置应用程序中的对象及建立这些对象间的依赖。
- 除被容器管理外，Bean 在应用程序中没有任何特殊之处。
- IOC 负责实例化、配置、组装 Bean，通过读取为应用程序定义的配置元数据获取有关实例化、配置和管理对象的信息。

### BeanFactory 快速入门

流程：程序代码 → 第三方 → 配置清单 → Bean

1. 导入 Spring 的 jar 包（Maven）
2. 定义接口和实现类
3. 创建 `beans.xml` 配置文件，将实现类信息配置到 XML 中
4. 编写测试类，创建 BeanFactory，加载配置文件，获取实例对象

### 测试类代码

```java
// 创建工厂对象
DefaultListableBeanFactory beanFactory = new DefaultListableBeanFactory();
// 创建读取器
XmlBeanDefinitionReader reader = new XmlBeanDefinitionReader(beanFactory);
// 读取器读取配置文件给工厂
reader.loadBeanDefinitions("beans.xml");
// 根据 id 获取 bean 实例
UserService userService = (UserService) beanFactory.getBean("userService");
```

### DI（依赖注入）

- Bean 间调用
- 创建一个 bean：比如叫 `empDao`
- 在 `UserServiceImpl` 中写方法：

```java
private EmpDao empDao;

public void setEmpDao(EmpDao empDao) {
    System.out.println("BeanFactory 调用方法获取 userDao 设置到此：" + empDao);
    this.empDao = empDao;
}
```

- 在 `beans.xml` 中配置该 bean：

```xml
<bean id="userService" class="org.example.UserServiceImpl">
    <property name="empDao" ref="empDao"></property>
</bean>
```

- `ref` 是引用的意思，这里就是引用的 bean 的 id
- `name` 是 set 方法后面的 Xxx，和参数名相同，注意：这个方法的名字不能改，改了会导致找不到方法
- 这样实现了 DI 依赖注入，底层会在获取 `userService` 时，执行好 `setEmpDao` 方法，一次提供好需要的 bean

### IOC（控制反转）

- **反转的是什么？** 反转的是 Bean 的创建权，将 Bean 的创建交给 BeanFactory。

### DI（依赖注入）

- **注入的是什么？** 注入的是 bean，实现不同 bean 之间的调用，目标是在 service 层就实现业务逻辑。

### 总结流程

1. 定义接口和实现类
2. 修改实现类代码，添加 `setXxx(Xxx xxx)` 方法，用于接收注入的对象
3. 修改 `beans.xml` 文件，在要被注入的实现类 bean 中嵌入 `<property>`
4. 创建测试代码，获取实现类对象，在获取对象时，`setXxx` 方法就被执行了

> 虽然开发中不怎么使用 BeanFactory，但是 BeanFactory 是底层核心。

## ApplicationContext 快速入门

- `ApplicationContext` 称为 Spring 容器，内部封装 `BeanFactory`，比 `BeanFactory` 更强大。
- 用 Spring 容器开发，配置文件习惯写成：`applicationContext.xml`

### Service 代码

```java
ApplicationContext applicationContext =
    new ClassPathXmlApplicationContext("applicationContext.xml");

UserService userService =
    (UserService) applicationContext.getBean("userService");

System.out.println(userService);
// 其他代码不变，业务中创建对象代码一下子少了很多，简化开发
```

### BeanFactory 和 ApplicationContext 关系

| 对比项 | BeanFactory | ApplicationContext |
|--------|-------------|--------------------|
| 定位 | Spring 的早期接口，称为 Bean 工厂 | 后期更高级接口，称为 Spring 容器 |
| 功能 | API 更底层 | 在 BeanFactory 基础上扩展了监听、国际化、资源加载、AOP 配置等功能 |
| 关系 | 主要逻辑和功能被封装在 ApplicationContext 中 | 内部维护着 BeanFactory 的引用，既有继承关系，还有融合关系 |
| Bean 初始化时机 | 首次调用 `getBean()` 时才创建 Bean | 配置文件加载、容器创建时就将 Bean 实例化并初始化 |

## 面试要点

- **BeanFactory**：IOC 容器的核心接口，负责 Bean 的实例化、配置和组装
- **ApplicationContext**：Spring 容器，封装 BeanFactory，功能更强大，Bean 初始化时机更早
- **IOC**：控制反转，反转的是 Bean 的创建权
- **DI**：依赖注入，注入的是 Bean，实现 Bean 间的调用
- **BeanFactory vs ApplicationContext**：前者延迟初始化，后者预初始化；前者底层，后者功能丰富
