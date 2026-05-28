# cookie 和 session 的区别

## 对比表

| 维度 | Cookie | Session |
|------|--------|---------|
| 存储位置 | 客户端浏览器 | 服务端（或分布式缓存） |
| 安全性 | 较低，可被窃取/篡改 | 较高，敏感数据在服务端 |
| 大小 | 约 4KB/条 | 服务端可较大 |
| 生命周期 | 可设过期时间 | 会话结束或超时失效 |
| 跨域 | 受同源策略限制 | 依赖 SessionId（常放 Cookie） |

## 典型流程

1. 登录成功，服务端创建 Session，返回 `JSESSIONID` 等 Cookie
2. 后续请求携带 Cookie，服务端查 Session

## 面试一句话

> Cookie 存客户端；Session 状态在服务端，靠 SessionId（多在 Cookie）关联。
