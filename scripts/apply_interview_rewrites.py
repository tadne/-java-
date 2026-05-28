#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""将完整重写内容写入指定 Markdown（覆盖）。"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# rel_path -> full markdown (must end with newline)
REWRITES: dict[str, str] = {}

def _load():
    global REWRITES
    if REWRITES:
        return
    # populated by exec below from REWRITE_BLOCKS
    pass

# fmt: off
REWRITE_BLOCKS: dict[str, str] = {
"面试题/Java基础/+=的特别之处.md": """# += 的特别之处

## 复合赋值

`a += b` 等价于 `a = (T)(a + b)`，其中 `T` 为 **a 的类型**（含隐式窄化转换）。

## 与 a = a + b 的区别

| 表达式 | 类型处理 |
|--------|----------|
| `a = a + b` | `a+b` 先提升，再赋值，可能编译错误（如 `byte`） |
| `a += b` | 结果**强制转换**回 a 的类型 |

```java
byte a = 1, b = 2;
// a = a + b;  // 编译错误：int 不能赋给 byte
a += b;        // OK，相当于 a = (byte)(a + b)
```

## 面试一句话

> `+=` 自带对左值类型的强制转换，因此 byte 等可用 `+=` 而不能直接 `a = a + b`。
""",
"面试题/Java基础/Exception类和Error类.md": """# Exception 类和 Error 类

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
""",
"面试题/Java基础/final用法.md": """# final 用法

## 三类用法

| 修饰 | 含义 |
|------|------|
| 类 | 不可被继承 |
| 方法 | 不可被重写（private 隐式 final） |
| 变量 | 只能赋值一次（基本类型值不变；引用地址不变） |

## final 变量

- 成员：声明时、实例块或构造器中赋值
- 局部：使用前赋值一次
- 引用 final：不能改指向，**对象内容可变**

## 面试一句话

> final 修饰类不可继承、方法不可重写、变量只能赋一次值。
""",
"面试题/Java基础/static用法.md": """# static 用法

## 含义

属于**类**而非实例：类加载时初始化，所有实例共享。

## 常见用法

| 用法 | 说明 |
|------|------|
| 静态变量 | 类级共享数据 |
| 静态方法 | 无 `this`，只能直接访问静态成员 |
| 静态块 | 类加载时执行一次 |
| 静态内部类 | 不持有外部类引用 |

## 注意

- 静态方法**不能**重写（可隐藏）
- 多线程下静态变量需考虑可见性与同步

## 面试一句话

> static 表示类级别成员，随类加载而存在，被所有实例共享。
""",
"面试题/Java基础/八种数据类型大小和封装类.md": """# 八种数据类型大小和封装类

## 基本类型

| 类型 | 字节 | 位 | 包装类 |
|------|------|-----|--------|
| byte | 1 | 8 | Byte |
| short | 2 | 16 | Short |
| int | 4 | 32 | Integer |
| long | 8 | 64 | Long |
| float | 4 | 32 | Float |
| double | 8 | 64 | Double |
| char | 2 | 16 | Character |
| boolean | 未严格规定 | — | Boolean |

## 缓存（Integer 等）

- `Integer.valueOf(-128~127)` 使用缓存池（可配置上限）

## 面试一句话

> 8 种基本类型各有固定大小与对应包装类；小整数 Integer 有缓存。
""",
"面试题/Java基础/java的自动装箱与拆箱.md": """# Java 的自动装箱与拆箱

## 概念

- **装箱**：基本类型 → 包装类（如 `int` → `Integer`）
- **拆箱**：包装类 → 基本类型

编译器自动插入 `valueOf` / `xxxValue()`。

## 注意

| 问题 | 说明 |
|------|------|
| NPE | 拆箱时包装类为 null |
| 性能 | 循环中频繁装箱有开销 |
| 比较 | `Integer` 用 `equals`，`==` 对 -128~127 可能为 true（缓存） |

## 面试一句话

> 装箱拆箱是语法糖；注意 null 拆箱 NPE 与 Integer 缓存导致的 == 陷阱。
""",
"面试题/Java基础/String,StringBuilder,StringBuffer的区别.md": """# String、StringBuilder、StringBuffer 的区别

## 对比表

| | String | StringBuilder | StringBuffer |
|---|--------|---------------|--------------|
| 可变性 | **不可变** | 可变 | 可变 |
| 线程安全 | 天然不可变即安全 | 否 | 是（方法 synchronized） |
| 性能 | 拼接产生新对象 | 单线程快 | 多线程安全但慢 |
| 使用场景 | 常量、少量拼接 | 单线程大量拼接 | 已少用，优先 Builder |

## 常量池

- 字面量进字符串池；`intern()` 可复用池中引用

## 面试一句话

> String 不可变；StringBuilder 可变非线程安全；StringBuffer 可变且同步，高并发拼接用 Builder+外部同步或别的方式。
""",
"面试题/Java基础/深拷贝和浅拷贝的区别.md": """# 深拷贝和浅拷贝的区别

## 对比

| | 浅拷贝 | 深拷贝 |
|---|--------|--------|
| 基本字段 | 复制值 | 复制值 |
| 引用字段 | **共享同一对象** | **递归复制新对象** |
| 实现 | `clone()` 默认、拷贝构造浅拷 | 手动递归、`序列化`、工具库 |

## 实现方式

- `Cloneable` + 重写 `clone()`（注意深拷要逐层 clone）
- 序列化/反序列化（需所有引用可序列化）
- 第三方：MapStruct、BeanUtils（注意是否深拷）

## 面试一句话

> 浅拷贝只复制引用；深拷贝引用指向的对象也全新复制，互不影响。
""",
"面试题/Java基础/面向对象和面向过程的区别.md": """# 面向对象和面向过程的区别

## 对比表

| 维度 | 面向过程 | 面向对象 |
|------|----------|----------|
| 核心 | 函数、步骤 | 对象、封装 |
| 单位 | 过程/算法 | 类与对象 |
| 扩展 | 改流程影响大 | 继承、多态易扩展 |
| 代表语言 | C | Java、C++ |

## OOP 四大特性

封装、继承、多态、抽象（面试常答）

## 面试一句话

> 面向过程以函数和步骤为中心；面向对象以对象封装数据与行为，便于扩展与维护。
""",
"面试题/Java基础/线程,程序,进程的基本概念与关系.md": """# 线程、程序、进程的基本概念与关系

## 概念

| 术语 | 说明 |
|------|------|
| 程序 | 磁盘上的静态代码 |
| 进程 | 程序的一次运行实例，OS 分配资源的基本单位 |
| 线程 | 进程内的执行单元，CPU 调度的基本单位 |

## 关系

- 一个程序可对应多个进程；一个进程可有多个线程
- 线程共享进程的堆、方法区；各有虚拟机栈、程序计数器

## 与 Java

- JVM 线程对应 OS 线程（1.8 默认）
- 主线程：`main` 入口

## 面试一句话

> 程序是代码，进程是运行实例，线程是进程内 CPU 调度单位，共享进程资源。
""",
"面试题/Java基础/死锁的四个必要条件.md": """# 死锁的四个必要条件

四者**同时成立**才可能死锁，破坏任一即可避免。

## 四个条件

| 条件 | 含义 |
|------|------|
| 互斥 | 资源只能被一个线程占用 |
| 占有且等待 | 持有资源的同时等待其他资源 |
| 不可抢占 | 资源只能由持有者释放 |
| 循环等待 | 存在线程资源的环形等待链 |

## 预防/避免

- 固定加锁顺序
- 超时 `tryLock`
- 银行家算法（理论）

## 面试一句话

> 死锁需互斥、占有等待、不可抢占、循环等待四条件同时具备；破环等待或占有等待最常用。
""",
"面试题/Java基础/红黑树特征.md": """# 红黑树特征

`HashMap` 在桶链表过长时转红黑树（JDK 8+），保证最坏 O(log n) 查找。

## 五条性质

1. 节点非红即黑
2. 根为黑
3. 红节点的子必须为黑（无连续红）
4. 从任一节点到叶子的所有路径含相同**黑高**
5. 近似平衡，最长路径不超过最短 2 倍

## 与 HashMap

- 链表 **≥8** 且 table **≥64** → 树化
- 树节点 **≤6** → 退链表

## 面试一句话

> 红黑树通过颜色约束保持近似平衡；HashMap 桶内树化阈值 8、退化 6。
""",
"面试题/操作系统/进程和线程的区别.md": """# 进程和线程的区别

## 对比表

| 维度 | 进程 | 线程 |
|------|------|------|
| 定义 | 资源分配的基本单位 | CPU 调度的基本单位 |
| 资源 | 独立地址空间、文件描述符等 | 共享所属进程资源 |
| 开销 | 创建/切换大 | 创建/切换小 |
| 通信 | IPC（管道、消息队列等） | 共享内存，需同步 |
| 崩溃影响 | 相对隔离 | 同进程线程可能拖垮进程 |

## 上下文切换

保存/恢复：寄存器、PC、栈、页表等；线程切换通常轻于进程。

## 面试一句话

> 进程拥有独立资源是分配单位；线程共享进程资源是调度单位，切换更轻。
""",
}
# fmt: on

def main():
    updated = []
    for rel, content in REWRITE_BLOCKS.items():
        path = ROOT / rel.replace("/", "\\") if "\\" in str(ROOT) else ROOT / rel
        path = ROOT / rel
        text = content.strip() + "\n"
        old = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
        if old != text:
            path.write_text(text, encoding="utf-8")
            updated.append(rel)
    print(f"REWRITE_COUNT={len(updated)}")
    for u in updated:
        print(u)

if __name__ == "__main__":
    main()
