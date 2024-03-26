# Socket编程

## 针对TCP该如何Socket编程？

![](../../../../../AppData/Local/Temp/format,png-20230309230545997.webp)

- 服务端和客户端初始化socket，得到文件描述符
- 服务端调用bind，将socket绑定在指定IP地址和端口
- 服务端调用listen监听
- 服务端调用accept，等待客户端连接
- 客户端调用connect，向服务端地址和端口发起连接
- 服务端accept返回用于传输的socket的文件描述符
- 客户端调用write写入数据，服务端调用read读取数据
- 客户端端口连接时，调用close，那么服务端read读取数据时会读取EOF，待处理完数据后，服务端调用close，表示连接关闭

服务端调用accept时，连接成功了会返回一个已经完成连接的socket，后续用来传输数据。所以监听的socket和真正传输数据的socket是两个socket，一个叫**监听socket**，一个叫**已完成连接socket**

成功连接后，双方开始通过read和write函数读写数据
