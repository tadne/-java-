# Java 创建线程的方式

面试常答 **三种**（Thread / Runnable / Callable），并补充 **线程池** 为生产推荐方式。

## 方式对比

| 方式 | 特点 | 推荐度 |
|------|------|--------|
| 继承 `Thread` | 单继承受限，任务与线程耦合 | 了解即可 |
| 实现 `Runnable` | 任务与执行分离，可复用 | 常用 |
| `Callable` + `FutureTask` | 有返回值、可抛检查异常 | 需要结果时 |
| **线程池** | 复用线程、控并发 | **生产首选** |

## 1. 继承 Thread

```java
class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Hello, Thread");
    }
}
new MyThread().start();  // 必须 start，不能直接 run
```

## 2. 实现 Runnable

```java
Runnable task = () -> System.out.println("Hello, Runnable");
new Thread(task).start();
```

## 3. Callable + Future

```java
Callable<Integer> c = () -> {
    int sum = 0;
    for (int i = 1; i <= 100; i++) sum += i;
    return sum;
};
FutureTask<Integer> ft = new FutureTask<>(c);
new Thread(ft).start();
Integer result = ft.get();  // 阻塞获取结果
```

## 4. 线程池（推荐）

```java
ThreadPoolExecutor pool = new ThreadPoolExecutor(
    4, 8, 60L, TimeUnit.SECONDS,
    new ArrayBlockingQueue<>(100),
    Executors.defaultThreadFactory(),
    new ThreadPoolExecutor.CallerRunsPolicy()
);
pool.execute(() -> System.out.println(Thread.currentThread().getName()));
pool.shutdown();
```

> **勿在生产用 `Executors.newFixedThreadPool` 等**：内部常为**无界队列**，任务堆积会导致 **OOM**。应显式 `ThreadPoolExecutor` + **有界队列**。

## start 与 run

| 调用 | 行为 |
|------|------|
| `start()` | 启动新线程，JVM 调用 `run` |
| `run()` | 普通方法，**当前线程**同步执行 |

## 面试一句话

> 创建线程答 Thread、Runnable、Callable；生产用 ThreadPoolExecutor 有界线程池，慎用 Executors 无界工厂，且必须 start 而非直接 run。
