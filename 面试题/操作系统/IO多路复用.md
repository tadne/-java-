# IO 多路复用

## 概念

单线程/少线程通过 **`select` / `poll` / `epoll`** 监听多个 fd，哪个就绪就处理哪个，避免为每个连接阻塞一个线程。

## 对比

| 机制 | 特点 |
|------|------|
| select | fd 上限小（常 1024），每次拷贝 fd 集合，O(n) 扫描 |
| poll | 无 1024 限制，仍 O(n) 扫描 |
| epoll | 事件驱动，O(1) 就绪通知，适合高并发（Linux） |

## 与 Java

- NIO `Selector` 底层在各 OS 上映射为上述机制
- Netty 默认使用 epoll（Linux）优化

## 面试一句话

> IO 多路复用让一个线程监听多路 IO；epoll 事件驱动、高并发场景优于 select/poll。
