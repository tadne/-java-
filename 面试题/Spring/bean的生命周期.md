# Bean 的生命周期

Bean 从创建到销毁由 **IoC 容器**管理，扩展点通过 `BeanPostProcessor` 等接口织入。

## 单例 Bean 主要阶段

| 顺序 | 阶段 | 说明 |
|------|------|------|
| 1 | 实例化 | 反射创建对象（构造器） |
| 2 | 属性填充 | 依赖注入（@Autowired 等） |
| 3 | Aware 回调 | `BeanNameAware`、`BeanFactoryAware` 等 |
| 4 | 初始化前 | `BeanPostProcessor.postProcessBeforeInitialization` |
| 5 | 初始化 | `@PostConstruct`、`InitializingBean.afterPropertiesSet`、自定义 init-method |
| 6 | 初始化后 | `BeanPostProcessor.postProcessAfterInitialization`（**AOP 代理常在此生成**） |
| 7 | 使用中 | 业务调用 |
| 8 | 销毁 | `@PreDestroy`、`DisposableBean.destroy`、destroy-method |

## 容器级扩展（更早执行）

| 接口 | 时机 |
|------|------|
| `BeanFactoryPostProcessor` | BeanDefinition 加载后、实例化前（改定义） |
| `BeanDefinitionRegistryPostProcessor` | 注册 BeanDefinition 之前 |

## prototype 与 singleton

| 作用域 | 创建 | 销毁 |
|--------|------|------|
| singleton | 容器启动时（非懒加载） | 容器关闭 |
| prototype | 每次 getBean | **容器不管理销毁**，需自行释放资源 |

## 与循环依赖

- 实例化后、完成初始化前可暴露早期引用（三级缓存）
- 仅 **单例 + 字段/setter** 循环依赖可解决

## 面试一句话

> 实例化 → 注入 → Aware → BPP 前后置 → 初始化 → 使用 → 销毁；AOP 代理多在初始化阶段的 BPP 之后完成。
