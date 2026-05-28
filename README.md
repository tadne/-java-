# Java 学习笔记

> 2023 年 3 月起整理的 Java 全栈学习笔记，持续更新。
> 原文多为手敲速记，已统一整理为 Markdown 格式，便于检索与阅读。

## 使用说明

- 按目录主题浏览，面试题目录按技术栈分类
- 计算机网络部分参考 [小林 coding](https://xiaolincoding.com/) 整理
- 文件按创建时间排序阅读时，可在 IDE 中按修改/创建时间查看
- **内容优化记录**：见 [学习变更说明.md](学习变更说明.md)（纠错、补充与推荐学习顺序）

## 目录总览

### [java基础](java基础/)（51 篇）

- **IO流/**（9 篇）
- **java代码基础/**
  - **java8特性/**
    - [jdk8新特性](java基础/java代码基础/java8特性/jdk8新特性.md)
    - [Lambda表达式](java基础/java代码基础/java8特性/Lambda表达式.md)
    - [Stream流](java基础/java代码基础/java8特性/Stream流.md)
    - [方法引用(不咋用,用多了记得几个就好了)](java基础/java代码基础/java8特性/方法引用(不咋用,用多了记得几个就好了).md)
  - **代码基础/**
    - [包装类](java基础/java代码基础/代码基础/包装类.md)
    - [基本数据类型和引用数据类型的区别](java基础/java代码基础/代码基础/基本数据类型和引用数据类型的区别.md)
    - [基本数据结构](java基础/java代码基础/代码基础/基本数据结构.md)
    - [字符集](java基础/java代码基础/代码基础/字符集.md)
    - [异常处理](java基础/java代码基础/代码基础/异常处理.md)
  - **字符串/**
    - [字符串API](java基础/java代码基础/字符串/字符串API.md)
    - [字符串内存分析](java基础/java代码基础/字符串/字符串内存分析.md)
    - [字符串基本](java基础/java代码基础/字符串/字符串基本.md)
  - **常用操作/**
    - [不可变集合](java基础/java代码基础/常用操作/不可变集合.md)
    - [可变参数](java基础/java代码基础/常用操作/可变参数.md)
    - [深浅克隆](java基础/java代码基础/常用操作/深浅克隆.md)
  - **常见修饰符/**
    - [final关键字](java基础/java代码基础/常见修饰符/final关键字.md)
    - [static关键字](java基础/java代码基础/常见修饰符/static关键字.md)
    - [this关键字的内存](java基础/java代码基础/常见修饰符/this关键字的内存.md)
    - [包](java基础/java代码基础/常见修饰符/包.md)
    - [权限修饰符](java基础/java代码基础/常见修饰符/权限修饰符.md)
  - **常见原理思想/**
    - [动态代理思想](java基础/java代码基础/常见原理思想/动态代理思想.md)
    - [反射原理](java基础/java代码基础/常见原理思想/反射原理.md)
- **jvm基础/**
  - [java内存分配](java基础/jvm基础/java内存分配.md)
  - [对象内存](java基础/jvm基础/对象内存.md)
  - [方法的基本内存原理](java基础/jvm基础/方法的基本内存原理.md)
- **内部类/**
  - [代码块](java基础/内部类/代码块.md)
  - [内部类](java基础/内部类/内部类.md)
- **爬虫/**
  - [正则表达式](java基础/爬虫/正则表达式.md)
  - [爬虫](java基础/爬虫/爬虫.md)
- **集合/**
  - [Collections集合工具类](java基础/集合/Collections集合工具类.md)
  - [Collection单列集合](java基础/集合/Collection单列集合.md)
  - [List系列](java基础/集合/List系列.md)
  - [Map双列集合](java基础/集合/Map双列集合.md)
  - [Queue系列集合](java基础/集合/Queue系列集合.md)
  - [Set系列](java基础/集合/Set系列.md)
- **面向对象/**
  - [多态](java基础/面向对象/多态.md)
  - [抽象类](java基础/面向对象/抽象类.md)
  - [接口](java基础/面向对象/接口.md)
  - [泛型](java基础/面向对象/泛型.md)
  - [继承](java基础/面向对象/继承.md)
  - [继承的内存](java基础/面向对象/继承的内存.md)
  - [面向对象基本](java基础/面向对象/面向对象基本.md)

### [常用API类](常用API类/)（8 篇）

- [BigDecimal](常用API类/BigDecimal.md)
- [BigInteger](常用API类/BigInteger.md)
- [jdk7_时间类](常用API类/jdk7_时间类.md)
- [jdk8_时间类](常用API类/jdk8_时间类.md)
- [Math类](常用API类/Math类.md)
- [Object类](常用API类/Object类.md)
- [Runtime类](常用API类/Runtime类.md)
- [System类](常用API类/System类.md)

### [多线程](多线程/)（17 篇）

- [Lock锁](多线程/Lock锁.md)
- [volatile关键字](多线程/volatile关键字.md)
- [串行并发与并行](多线程/串行并发与并行.md)
- [原子类](多线程/原子类.md)
- [多线程的优势与风险](多线程/多线程的优势与风险.md)
- [常用方法](多线程/常用方法.md)
- [并发工具类-ConcurrentHashMap](多线程/并发工具类-ConcurrentHashMap.md)
- [并发工具类-CountDownLatch](多线程/并发工具类-CountDownLatch.md)
- [并发工具类-CyclicBarrier](多线程/并发工具类-CyclicBarrier.md)
- [并发工具类-Exchanger](多线程/并发工具类-Exchanger.md)
- [并发工具类-Semaphore](多线程/并发工具类-Semaphore.md)
- [等待唤醒机制](多线程/等待唤醒机制.md)
- [线程安全问题](多线程/线程安全问题.md)
- [线程池](多线程/线程池.md)
- [线程的创建与启动](多线程/线程的创建与启动.md)
- [线程的生命周期](多线程/线程的生命周期.md)
- [进程线程与主线程概念](多线程/进程线程与主线程概念.md)

### [JVM](JVM/)（25 篇）

- **jvm优化/**
  - [语法糖](JVM/jvm优化/语法糖.md)
  - [运行期优化](JVM/jvm优化/运行期优化.md)
- **jvm周期阶段/**
  - [类加载器](JVM/jvm周期阶段/类加载器.md)
  - [类加载阶段](JVM/jvm周期阶段/类加载阶段.md)
- **jvm基础/**
  - [什么是JVM](JVM/jvm基础/什么是JVM.md)
- **内存管理/**（9 篇）
- **垃圾回收/**
  - [G1垃圾回收器](JVM/垃圾回收/G1垃圾回收器.md)
  - [java中的5种引用](JVM/垃圾回收/java中的5种引用.md)
  - [分代垃圾回收](JVM/垃圾回收/分代垃圾回收.md)
  - [垃圾回收器](JVM/垃圾回收/垃圾回收器.md)
  - [垃圾回收器调优](JVM/垃圾回收/垃圾回收器调优.md)
  - [垃圾回收算法](JVM/垃圾回收/垃圾回收算法.md)
  - [如何判断对象可以回收](JVM/垃圾回收/如何判断对象可以回收.md)
- **字节码/**
  - [字节码指令](JVM/字节码/字节码指令.md)
  - [类文件结构](JVM/字节码/类文件结构.md)
- **锁/**
  - [CAS与原子类](JVM/锁/CAS与原子类.md)
  - [jvm锁优化](JVM/锁/jvm锁优化.md)

### [23种设计模式](23种设计模式/)（5 篇）

- [代理模式](23种设计模式/代理模式.md)
- [单例模式](23种设计模式/单例模式.md)
- [工厂模式](23种设计模式/工厂模式.md)
- [适配器模式](23种设计模式/适配器模式.md)
- [面向对象设计原则](23种设计模式/面向对象设计原则.md)

### [Spring](Spring/)（42 篇）

- **mybatis/**
  - [lombook类库](Spring/mybatis/lombook类库.md)
  - [Mybatis简介](Spring/mybatis/Mybatis简介.md)
  - [xml映射文件](Spring/mybatis/xml映射文件.md)
  - [数据库连接池](Spring/mybatis/数据库连接池.md)
- [Aop概念](Spring/Aop概念.md)
- [AOP配置详情](Spring/AOP配置详情.md)
- [Bean依赖注入注解开发](Spring/Bean依赖注入注解开发.md)
- [Bean基本注解开发](Spring/Bean基本注解开发.md)
- [Bean实例化的基本流程](Spring/Bean实例化的基本流程.md)
- [Bean的生命周期](Spring/Bean的生命周期.md)
- [Bean配置类的注解开发](Spring/Bean配置类的注解开发.md)
- [IOC,DI,AOP基本思想](Spring/IOC,DI,AOP基本思想.md)
- [Spring IOC整体流程总结](Spring/Spring IOC整体流程总结.md)
- [Spring xml方式整合第三方框架](Spring/Spring xml方式整合第三方框架.md)
- [SpringMVC拦截器](Spring/SpringMVC拦截器.md)
- [SpringMVC的响应处理](Spring/SpringMVC的响应处理.md)
- [SpringMVC的请求处理](Spring/SpringMVC的请求处理.md)
- [SpringMVC简介](Spring/SpringMVC简介.md)
- [Spring事务失效问题](Spring/Spring事务失效问题.md)
- [Spring整合web](Spring/Spring整合web.md)
- [Spring框架概述](Spring/Spring框架概述.md)
- [Spring注解方式整合第三方框架](Spring/Spring注解方式整合第三方框架.md)
- [Spring注解的解析原理](Spring/Spring注解的解析原理.md)
- [Spring的get方法](Spring/Spring的get方法.md)
- [Spring的后处理器](Spring/Spring的后处理器.md)
- [spring继承体系](Spring/spring继承体系.md)
- [Spring配置其他注解](Spring/Spring配置其他注解.md)
- [Spring配置非自定义Bean](Spring/Spring配置非自定义Bean.md)
- [传统web开发缺点](Spring/传统web开发缺点.md)
- [全注解开发](Spring/全注解开发.md)
- [前端控制器初始化](Spring/前端控制器初始化.md)
- [基于AOP的声明式事务控制](Spring/基于AOP的声明式事务控制.md)
- [基于xml实现声明式事务](Spring/基于xml实现声明式事务.md)
- [基于xml的spring应用](Spring/基于xml的spring应用.md)
- [基于xml配置AOP入门](Spring/基于xml配置AOP入门.md)
- [基于XML配置的AOP原理](Spring/基于XML配置的AOP原理.md)
- [基于注解实现声明式事务](Spring/基于注解实现声明式事务.md)
- [异常处理机制](Spring/异常处理机制.md)
- [注解配置AOP基本使用](Spring/注解配置AOP基本使用.md)
- [注解驱动](Spring/注解驱动.md)
- [静态资源请求](Spring/静态资源请求.md)
- [非自定义Bean注解开发](Spring/非自定义Bean注解开发.md)

### [springBoot](springBoot/)（9 篇）

- [Bean的属性依赖配置](springBoot/Bean的属性依赖配置.md)
- [SpringBoot核心原理_SpringBoot启动流程](springBoot/SpringBoot核心原理_SpringBoot启动流程.md)
- [SQL数据持久](springBoot/SQL数据持久.md)
- [yml语法规则](springBoot/yml语法规则.md)
- [数据校验](springBoot/数据校验.md)
- [测试类规则](springBoot/测试类规则.md)
- [热部署](springBoot/热部署.md)
- [自动配置原理](springBoot/自动配置原理.md)
- [配置文件优先级](springBoot/配置文件优先级.md)

### [SpringCloud](SpringCloud/)（18 篇）

- [AT模式](SpringCloud/AT模式.md)
- [Nacos注册中心](SpringCloud/Nacos注册中心.md)
- [OpenFeign](SpringCloud/OpenFeign.md)
- [OpenFeign传递用户](SpringCloud/OpenFeign传递用户.md)
- [Seata](SpringCloud/Seata.md)
- [Sentinel](SpringCloud/Sentinel.md)
- [XA模式](SpringCloud/XA模式.md)
- [分布式事务](SpringCloud/分布式事务.md)
- [微服务与单体架构](SpringCloud/微服务与单体架构.md)
- [微服务保护](SpringCloud/微服务保护.md)
- [微服务拆分](SpringCloud/微服务拆分.md)
- [微服务获取用户](SpringCloud/微服务获取用户.md)
- [微服务远程调用的进一步问题](SpringCloud/微服务远程调用的进一步问题.md)
- [服务注册与发现](SpringCloud/服务注册与发现.md)
- [网关登录校验](SpringCloud/网关登录校验.md)
- [网关路由](SpringCloud/网关路由.md)
- [网关过滤器](SpringCloud/网关过滤器.md)
- [配置管理](SpringCloud/配置管理.md)

### [MySQL](MySQL/)（16 篇）

- **SQL语法/**
  - [SQL优化](MySQL/SQL语法/SQL优化.md)
  - [SQL通用语法和分类](MySQL/SQL语法/SQL通用语法和分类.md)
  - [存储过程](MySQL/SQL语法/存储过程.md)
- **事务安全/**
  - [InnoDb_MVCC](MySQL/事务安全/InnoDb_MVCC.md)
  - [InnoDB事务原理](MySQL/事务安全/InnoDB事务原理.md)
  - [事务](MySQL/事务安全/事务.md)
  - [锁](MySQL/事务安全/锁.md)
- **内存结构/**
  - [InnoDB逻辑存储结构](MySQL/内存结构/InnoDB逻辑存储结构.md)
  - [MySQL体系结构](MySQL/内存结构/MySQL体系结构.md)
  - [存储引擎](MySQL/内存结构/存储引擎.md)
- **索引视图组件/**
  - [索引](MySQL/索引视图组件/索引.md)
  - [视图](MySQL/索引视图组件/视图.md)
  - [触发器](MySQL/索引视图组件/触发器.md)
- [MySQL管理工具](MySQL/MySQL管理工具.md)
- [MySQL面试题](MySQL/MySQL面试题.md)
- [数据库设计原则](MySQL/数据库设计原则.md)

### [redis](redis/)（39 篇）

- **java客户端/**
  - [redis的java客户端](redis/java客户端/redis的java客户端.md)
  - [SpringDataRedis](redis/java客户端/SpringDataRedis.md)
- **redis基础/**
  - [Redis通用命令](redis/redis基础/Redis通用命令.md)
  - [认识redis](redis/redis基础/认识redis.md)
- **redis数据结构/**
  - [BitMap结构](redis/redis数据结构/BitMap结构.md)
  - [GEO结构](redis/redis数据结构/GEO结构.md)
  - [Hash类型](redis/redis数据结构/Hash类型.md)
  - [HyperLogLog结构](redis/redis数据结构/HyperLogLog结构.md)
  - [List类型](redis/redis数据结构/List类型.md)
  - [Set类型](redis/redis数据结构/Set类型.md)
  - [SortedSet](redis/redis数据结构/SortedSet.md)
  - [String类型](redis/redis数据结构/String类型.md)
- **常见缓存问题/**
  - [什么是缓存](redis/常见缓存问题/什么是缓存.md)
  - [以下总结](redis/常见缓存问题/以下总结.md)
  - [添加redis缓存](redis/常见缓存问题/添加redis缓存.md)
  - [缓存击穿](redis/常见缓存问题/缓存击穿.md)
  - [缓存更新策略](redis/常见缓存问题/缓存更新策略.md)
  - [缓存穿透](redis/常见缓存问题/缓存穿透.md)
  - [缓存雪崩](redis/常见缓存问题/缓存雪崩.md)
- **应用/**
  - **其他功能/**
    - **登录校验/**
      - [基于redis实现共享session登录](redis/应用/其他功能/登录校验/基于redis实现共享session登录.md)
      - [基于Session实现登录](redis/应用/其他功能/登录校验/基于Session实现登录.md)
    - **网购秒杀/**
      - [redis优化秒杀](redis/应用/其他功能/网购秒杀/redis优化秒杀.md)
      - [实现秒杀](redis/应用/其他功能/网购秒杀/实现秒杀.md)
    - [redis实现消息队列](redis/应用/其他功能/redis实现消息队列.md)
    - [全局id生成器](redis/应用/其他功能/全局id生成器.md)
    - [短视频Feed流](redis/应用/其他功能/短视频Feed流.md)
  - **分布式锁/**
    - [Redisson介绍](redis/应用/分布式锁/Redisson介绍.md)
    - [redis分布式锁总结](redis/应用/分布式锁/redis分布式锁总结.md)
    - [分布式事务理论以及redisson分布式锁原理](redis/应用/分布式锁/分布式事务理论以及redisson分布式锁原理.md)
    - [分布式锁](redis/应用/分布式锁/分布式锁.md)
    - [可重入锁](redis/应用/分布式锁/可重入锁.md)
- **持久化/**
  - [RDB的fork原理](redis/持久化/RDB的fork原理.md)
  - [Redis持久化-AOF](redis/持久化/Redis持久化-AOF.md)
  - [Redis持久化-RDB](redis/持久化/Redis持久化-RDB.md)
- **集群/**
  - [Redis集群优势](redis/集群/Redis集群优势.md)
  - [主从数据同步原理](redis/集群/主从数据同步原理.md)
  - [主从集群架构](redis/集群/主从集群架构.md)
  - [哨兵作用和工作原理](redis/集群/哨兵作用和工作原理.md)
- [redis面试题](redis/redis面试题.md)

### [RabbitMq](RabbitMq/)（19 篇）

- **java客户端/**
  - [java客户端AMQP](RabbitMq/java客户端/java客户端AMQP.md)
- **mq可靠性/**
  - **消费者可靠性/**
    - [消费者可靠性--业务幂等性](RabbitMq/mq可靠性/消费者可靠性/消费者可靠性--业务幂等性.md)
    - [消费者可靠性--失败重试机制](RabbitMq/mq可靠性/消费者可靠性/消费者可靠性--失败重试机制.md)
    - [消费者可靠性--消费者确认机制](RabbitMq/mq可靠性/消费者可靠性/消费者可靠性--消费者确认机制.md)
  - **生产者可靠性/**
    - [发送者可靠性--生产者确认](RabbitMq/mq可靠性/生产者可靠性/发送者可靠性--生产者确认.md)
    - [发送者可靠性--生产者重连](RabbitMq/mq可靠性/生产者可靠性/发送者可靠性--生产者重连.md)
  - [MQ可靠性-数据持久化](RabbitMq/mq可靠性/MQ可靠性-数据持久化.md)
  - [消息可靠性问题](RabbitMq/mq可靠性/消息可靠性问题.md)
- **mq基础/**
  - [MQ技术选择](RabbitMq/mq基础/MQ技术选择.md)
  - [RabbitMQ介绍](RabbitMq/mq基础/RabbitMQ介绍.md)
  - [RabbitMQ整体架构和概念](RabbitMq/mq基础/RabbitMQ整体架构和概念.md)
  - [work模型](RabbitMq/mq基础/work模型.md)
  - [同步调用](RabbitMq/mq基础/同步调用.md)
  - [异步调用](RabbitMq/mq基础/异步调用.md)
- **交换机/**
  - [Direct交换机](RabbitMq/交换机/Direct交换机.md)
  - [Fanout交换机](RabbitMq/交换机/Fanout交换机.md)
  - [Topic交换机](RabbitMq/交换机/Topic交换机.md)
  - [声明队列交换机的方式](RabbitMq/交换机/声明队列交换机的方式.md)
- **其他/**
  - [消息转换器](RabbitMq/其他/消息转换器.md)

### [ElasticSearch](ElasticSearch/)（18 篇）

- **es集群/**
  - [ES集群](ElasticSearch/es集群/ES集群.md)
- **java客户端/**
  - [Java客户端操作文档](ElasticSearch/java客户端/Java客户端操作文档.md)
  - [Java客户端操作索引库](ElasticSearch/java客户端/Java客户端操作索引库.md)
  - [RestClient实现DSL和结果处理](ElasticSearch/java客户端/RestClient实现DSL和结果处理.md)
- **分词器/**
  - [ikun分词器](ElasticSearch/分词器/ikun分词器.md)
  - [自定义分词器](ElasticSearch/分词器/自定义分词器.md)
- **方案/**
  - [数据同步](ElasticSearch/方案/数据同步.md)
  - [自动补全](ElasticSearch/方案/自动补全.md)
- **认识es/**
  - [mapping映射属性](ElasticSearch/认识es/mapping映射属性.md)
  - [什么是ElasticSearch](ElasticSearch/认识es/什么是ElasticSearch.md)
  - [倒排索引](ElasticSearch/认识es/倒排索引.md)
  - [文档](ElasticSearch/认识es/文档.md)
- **语法/**
  - [DSL查询语法](ElasticSearch/语法/DSL查询语法.md)
  - [搜索结果处理](ElasticSearch/语法/搜索结果处理.md)
  - [数据聚合](ElasticSearch/语法/数据聚合.md)
  - [文档操作](ElasticSearch/语法/文档操作.md)
  - [索引库操作](ElasticSearch/语法/索引库操作.md)
  - [自动补全](ElasticSearch/语法/自动补全.md)

### [分布式](分布式/)（2 篇）

- **assets/**
- [GFS](分布式/GFS.md)
- [分布式基础理论](分布式/分布式基础理论.md)

### [计算机网络](计算机网络/)（23 篇）

- **HTTP/**
  - **常见面试题/**
    - [GET和POST](计算机网络/HTTP/常见面试题/GET和POST.md)
    - [HTTP3的优势](计算机网络/HTTP/常见面试题/HTTP3的优势.md)
    - [HTTP和HTTPS](计算机网络/HTTP/常见面试题/HTTP和HTTPS.md)
    - [HTTP基本概念](计算机网络/HTTP/常见面试题/HTTP基本概念.md)
    - [HTTP版本演变](计算机网络/HTTP/常见面试题/HTTP版本演变.md)
    - [HTTP特性](计算机网络/HTTP/常见面试题/HTTP特性.md)
    - [HTTP缓存技术](计算机网络/HTTP/常见面试题/HTTP缓存技术.md)
  - [HTTP1的优化](计算机网络/HTTP/HTTP1的优化.md)
  - [HTTP2的优势](计算机网络/HTTP/HTTP2的优势.md)
  - [HTTPS如何优化](计算机网络/HTTP/HTTPS如何优化.md)
  - [HTTPS的ECDHE握手解析](计算机网络/HTTP/HTTPS的ECDHE握手解析.md)
  - [HTTP协议和RPC协议](计算机网络/HTTP/HTTP协议和RPC协议.md)
  - [HTTP和WebSocket](计算机网络/HTTP/HTTP和WebSocket.md)
  - [TLS握手过程](计算机网络/HTTP/TLS握手过程.md)
- **TCP/**
  - **TCP面试/**
    - [Socket编程](计算机网络/TCP/TCP面试/Socket编程.md)
    - [TCP基本认识](计算机网络/TCP/TCP面试/TCP基本认识.md)
    - [TCP连接建立](计算机网络/TCP/TCP面试/TCP连接建立.md)
    - [TCP连接断开](计算机网络/TCP/TCP面试/TCP连接断开.md)
  - [tcp特性](计算机网络/TCP/tcp特性.md)
- **网络基础/**
  - [Linux收发网络包](计算机网络/网络基础/Linux收发网络包.md)
  - [总结](计算机网络/网络基础/总结.md)
  - [网络基础](计算机网络/网络基础/网络基础.md)
  - [键入网址到页面显示发生了什么](计算机网络/网络基础/键入网址到页面显示发生了什么.md)

### [面试题](面试题/)（187 篇）

- **Java基础/**（36 篇）
- **JUC并发编程/**（40 篇）
- **JVM/**（23 篇）
- **Mybatis/**（15 篇）
- **Spring/**（16 篇）
- **SpringBoot/**（11 篇）
- **操作系统/**（22 篇）
- **计算机网络/**（20 篇）
- **面经/**
  - [招银二面](面试题/面经/招银二面.md)
  - [招银网络一面](面试题/面经/招银网络一面.md)
  - [神州租车2面](面试题/面经/神州租车2面.md)
- **项目/**
  - [项目开发流程](面试题/项目/项目开发流程.md)

### [操作系统](操作系统/)（0 篇）

## 文档格式说明

| 元素 | 说明 |
|------|------|
| `# 标题` | 与文件名一致的一级标题 |
| `## 小节` | 章节、概念块标题 |
| `- **关键词**：说明` | 要点对照式笔记 |
| 嵌套列表 | 表示层级与从属关系 |

## 贡献与维护

- 新增笔记请直接使用 `.md` 格式
- 批量转换脚本：`scripts/convert_txt_to_md.py`（历史 txt 已迁移完毕）
