# SpringMVC常用注解有哪些

Spring MVC 通过注解简化控制器开发（Boot 默认 `DispatcherServlet` + 注解驱动）。

## 控制器类

| 注解 | 作用 |
|------|------|
| `@Controller` | 标记 MVC 控制器，返回视图名 |
| `@RestController` | `@Controller` + `@ResponseBody`，直接返回 JSON 等 |

## 请求映射

| 注解 | 作用 |
|------|------|
| `@RequestMapping` | 映射 URL（可限定 method、params、headers） |
| `@GetMapping` / `@PostMapping` 等 | `@RequestMapping` 的 HTTP 方法快捷方式 |

## 参数绑定

| 注解 | 作用 |
|------|------|
| `@RequestParam` | 查询参数 / 表单字段 |
| `@PathVariable` | REST 路径变量 |
| `@RequestBody` | 请求体 JSON → 对象（Jackson） |
| `@RequestHeader` | 请求头 |
| `@CookieValue` | Cookie |
| `@ModelAttribute` | 绑定模型属性（表单、复用对象） |

## 响应与视图

| 注解 | 作用 |
|------|------|
| `@ResponseBody` | 返回值写入响应体（非视图） |
| `@SessionAttributes` | 将模型属性存入 Session |

## 其他常用

| 注解 | 作用 |
|------|------|
| `@Valid` + `@Validated` | 参数校验（JSR-303） |
| `@ExceptionHandler` | 控制器内异常处理 |
| `@ControllerAdvice` | 全局异常/模型增强 |

## 面试要点

- `@RestController` = 类级别 `@ResponseBody`，前后端分离常用。
- `@RequestBody` 依赖 `HttpMessageConverter`（默认 Jackson）。
- 路径变量用 `@PathVariable`，表单/查询用 `@RequestParam`。

## 面试一句话

> SpringMVC 用 @RestController、@RequestMapping 映射请求，@RequestParam/@PathVariable/@RequestBody 绑定参数，@ResponseBody 返回 JSON。
