# 如何用SpringBoot实现异常处理

## 方式对比

| 方式 | 范围 | 返回格式 | 推荐 |
|------|------|----------|------|
| 默认 `/error` | 全局 | Whitelabel / 自定义 error 页 | 不推荐生产 |
| `@ExceptionHandler` | 当前 Controller | 自定义 | 局部异常 |
| `@ControllerAdvice` + `@ExceptionHandler` | 全局 | 自定义 | ✅ 常用 |
| `@RestControllerAdvice` | 全局 | JSON | ✅ REST 项目 |
| `ErrorController` / `BasicErrorController` | 全局 | 统一错误页/JSON | 定制默认错误 |

## REST 全局异常（推荐）

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(BusinessException.class)
    public Result<?> handleBusiness(BusinessException e) {
        return Result.fail(e.getCode(), e.getMessage());
    }

    @ExceptionHandler(Exception.class)
    public Result<?> handleOther(Exception e) {
        return Result.fail(500, "系统繁忙");
    }
}
```

## 与 Spring MVC 关系

- `@ControllerAdvice` 可配合 `@ResponseBody` 或直接用 `@RestControllerAdvice`。
- 异常解析器：`HandlerExceptionResolver` 链，Advice 是高层封装。

## 自定义错误页

- `src/main/resources/templates/error.html`（Thymeleaf）
- 或实现 `ErrorController` 返回 JSON

## 面试要点

- REST 用 `@RestControllerAdvice` 统一返回错误码和消息。
- 区分业务异常与系统异常，避免把堆栈直接返回客户端。

## 面试一句话

> Spring Boot 全局异常用 @RestControllerAdvice + @ExceptionHandler 统一返回 JSON，REST 项目标准做法。
