# SpringBoot集成RabbitMQ步骤

## 1. 添加依赖

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-amqp</artifactId>
</dependency>
```

自动引入 Spring AMQP 与 RabbitMQ 客户端。

## 2. 配置连接

```yaml
spring:
  rabbitmq:
    host: localhost
    port: 5672
    username: guest
    password: guest
    virtual-host: /
```

## 3. 声明队列、交换机、绑定（可选）

```java
@Configuration
public class RabbitConfig {
    @Bean
    public Queue queue() {
        return new Queue("order.queue", true);
    }

    @Bean
    public DirectExchange exchange() {
        return new DirectExchange("order.exchange");
    }

    @Bean
    public Binding binding(Queue queue, DirectExchange exchange) {
        return BindingBuilder.bind(queue).to(exchange).with("order.routing");
    }
}
```

## 4. 发送消息

```java
@Autowired
private RabbitTemplate rabbitTemplate;

public void send(String msg) {
    rabbitTemplate.convertAndSend("order.exchange", "order.routing", msg);
}
```

## 5. 消费消息

```java
@RabbitListener(queues = "order.queue")
public void onMessage(String body) {
    // 处理消息
}
```

## Boot 自动配置了什么

- `CachingConnectionFactory`
- `RabbitTemplate`
- `@EnableRabbit` 支持 `@RabbitListener`

## 面试要点

- Starter 自动配置连接工厂和模板，业务只需声明队列和监听。
- 生产注意：消息确认、幂等、死信队列。

## 面试一句话

> 引入 spring-boot-starter-amqp 配置 rabbitmq 属性，用 RabbitTemplate 发送、@RabbitListener 消费即可。
