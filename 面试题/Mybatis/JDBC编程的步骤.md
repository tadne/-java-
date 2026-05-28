# JDBC编程的步骤

JDBC（Java Database Connectivity）是 Java 访问关系型数据库的标准 API。

## 标准步骤（JDK 8+）

| 步骤 | 操作 | 说明 |
|------|------|------|
| 1 | 加载驱动 | `Class.forName` 已不推荐；**SPI 自动加载**（`DriverManager`） |
| 2 | 获取连接 | `DriverManager.getConnection(url, user, pwd)` 或 **DataSource** |
| 3 | 创建语句 | `prepareStatement(sql)`（推荐，防注入） |
| 4 | 执行 | `executeQuery` / `executeUpdate` |
| 5 | 处理结果 | 遍历 `ResultSet` |
| 6 | 释放资源 | `try-with-resources` 自动关闭 |

## 推荐写法（try-with-resources）

```java
String sql = "SELECT id, name FROM user WHERE id = ?";
try (Connection conn = dataSource.getConnection();
     PreparedStatement ps = conn.prepareStatement(sql)) {
    ps.setLong(1, id);
    try (ResultSet rs = ps.executeQuery()) {
        while (rs.next()) {
            // 映射数据
        }
    }
}
```

## 与 MyBatis 关系

MyBatis 底层仍使用 JDBC，封装了连接管理、参数绑定、结果映射。

## 面试要点

- 优先 **PreparedStatement**，不用拼接 SQL。
- 生产用连接池（HikariCP），不要每次 new 连接。
- JDBC 4+ 驱动通过 SPI 加载，一般无需 `Class.forName`。

## 面试一句话

> JDBC 核心是获取连接、PreparedStatement 执行 SQL、处理 ResultSet，并用 try-with-resources 关闭资源。
