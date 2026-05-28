# Runtime 类

`java.lang.Runtime` 表示 **JVM 运行时环境**，单例：`Runtime.getRuntime()`。

## 常用能力

- `exec(String command)`：执行外部命令（注意安全与权限）
- `availableProcessors()`：CPU 核心数
- `totalMemory()` / `freeMemory()` / `maxMemory()`：堆内存信息（单位字节）
- `gc()`：建议 JVM 进行垃圾回收（仅建议，不保证立即执行）
- `exit(int status)`：终止当前 JVM 进程

## 小结

- 每个 Java 应用对应一个 Runtime 实例
- 生产环境慎用 `exec`；内存调优更常用 JVM 参数与监控工具
