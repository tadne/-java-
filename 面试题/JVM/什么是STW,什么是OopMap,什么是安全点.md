# 什么是 STW、OopMap、安全点

## Stop-The-World（STW）

- GC 或部分 GC 阶段需要**暂停所有应用线程**，保证引用关系不变。
- **Minor GC** STW 通常较短；**Full GC**、部分老年代收集 STW 更长。
- **G1/ZGC** 目标缩短 STW，但并非完全无停顿。

## 安全点（Safepoint）

- 线程执行到**安全点**时才能暂停（如方法调用、循环回边等）。
- 不能在任意字节码中间停，否则栈上引用不一致。

## 安全区域（Saferegion）

- 线程处于 Sleep/Blocked 等无法跑到安全点时，进入安全区域，仍可参与 GC 根扫描。

## OopMap

- 记录**栈帧里哪些槽位是引用**（Ordinary Object Pointer Map）。
- GC 扫描根集合时根据 OopMap 找引用，避免把 int 当指针。

## 关系

```
应用运行 → 到达 Safepoint → STW → 根据 OopMap 扫描根 → GC → 恢复
```

## 面试一句话

> STW 暂停业务线程做 GC；只能在安全点停；OopMap 标记栈上哪些是对象引用供根扫描。
