# 线程池中 submit 和 execute 的区别

| | execute | submit |
|---|---------|--------|
| 接口 | Executor | ExecutorService |
| 参数 | Runnable | Runnable / Callable |
| 返回值 | void | Future |
| 异常 | 未捕获则线程组处理 | 封装进 Future，get 时 ExecutionException |

## 面试一句话

> execute 无返回；submit 返回 Future，异常在 get 时抛出，适合需要结果或 Callable 的场景。
