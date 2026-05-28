# Exception 类和 Error 类

## 类层次

```
Throwable
├── Error      （JVM 严重错误，一般不捕获）
└── Exception
    ├── RuntimeException（非受检）
    └── 其他 Exception（受检，必须处理或声明）
```

## 对比

| | Error | Exception |
|---|-------|-----------|
| 典型 | OOM、StackOverflow、NoClassDefFoundError | IOException、NPE |
| 是否应捕获 | 一般不 | 受检必须处理 |
| 程序可恢复 | 通常不可 | 常可 |

## 受检 vs 非受检

- **受检**：编译期检查，`try-catch` 或 `throws`
- **非受检**：`RuntimeException` 及其子类，如 NPE、IAE

## 面试一句话

> Error 是 JVM 级严重问题一般不抓；Exception 分受检与运行时异常，业务多处理后者。
