# SpringMVC怎么设定重定向和转发的

## 重定向 vs 转发

| 对比项 | 转发（Forward） | 重定向（Redirect） |
|--------|-----------------|-------------------|
| 请求次数 | 1 次 | 2 次（302 + 新请求） |
| 浏览器 URL | 不变 | 变为目标 URL |
| 共享 request 属性 | ✅ | ❌（新请求） |
| 跨域/跨服务器 | 仅当前应用内 | 可跳外部 URL |
| 重复提交 | 刷新可能重复提交 | POST-Redirect-GET 可缓解 |

## 方式一：视图名前缀（推荐）

```java
return "forward:/user/list";   // 转发
return "redirect:/user/list";  // 重定向
```

## 方式二：Servlet API

```java
request.getRequestDispatcher("/user/list").forward(request, response);
response.sendRedirect("/user/list");
```

## 方式三：ModelAndView

```java
return new ModelAndView("redirect:/success");
return new ModelAndView("forward:/detail");
```

## REST 接口注意

- 前后端分离时，重定向/转发多用于**服务端渲染**（JSP、Thymeleaf）。
- API 通常直接返回 JSON 状态码，由前端路由跳转。

## 面试要点

- `redirect:` 发 302，客户端再请求；`forward:` 服务器内部跳转。
- 转发可带 request 属性；重定向不能。
- 表单提交成功常用 redirect 防止重复提交。

## 面试一句话

> 转发用 forward: 一次请求共享域属性，重定向用 redirect: 两次请求改浏览器地址，表单成功常用重定向防重复提交。
