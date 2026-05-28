# SpringMVC 流程

Spring MVC 基于 **DispatcherServlet** 前端控制器，实现 MVC 分层与请求分发。

## 完整请求链路

```
浏览器
  → Filter 链（编码、安全等）
  → DispatcherServlet
  → HandlerMapping（找 Handler）
  → HandlerAdapter（执行 Handler）
  → Controller 返回 ModelAndView / @ResponseBody
  → ViewResolver（视图）或 HttpMessageConverter（JSON）
  → 响应
```

## 核心组件

| 组件 | 作用 |
|------|------|
| DispatcherServlet | 前端控制器，统一入口 |
| HandlerMapping | 根据 URL 映射到 Handler（Controller 方法） |
| HandlerAdapter | 适配不同 Handler 类型并调用 |
| HandlerInterceptor | 前置/后置/完成拦截 |
| ViewResolver | 解析逻辑视图名 → View（JSP、Thymeleaf） |
| HttpMessageConverter | `@ResponseBody` 序列化 JSON 等 |

## 步骤说明

1. **请求进入** `DispatcherServlet`
2. **HandlerMapping** 找到 Handler 及 Interceptor 链
3. **HandlerAdapter** 执行 Controller 方法
4. 返回类型分支：
   - **视图**：`ModelAndView` → ViewResolver → 渲染 HTML
   - **REST**：`@ResponseBody` → MessageConverter → JSON/XML
5. **异常**：`HandlerExceptionResolver` 处理
6. 写回响应

## 与 Spring Boot 关系

- Boot 自动配置 `DispatcherServlet`、`RequestMappingHandlerMapping` 等
- 默认 JSON 使用 Jackson

## 面试一句话

> 请求经 Filter 到 DispatcherServlet，Mapping 找 Handler，Adapter 执行，再经 ViewResolver 或 MessageConverter 返回视图/JSON。
