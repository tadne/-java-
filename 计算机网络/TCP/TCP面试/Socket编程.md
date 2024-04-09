# Socket编程

## 针对TCP该如何Socket编程？

![基于 TCP 协议的客户端和服务端工作](https://cdn.xiaolincoding.com//mysql/other/format,png-20230309230545997.png)

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

## listen的时候参数backlog的意义

Linux会维护两个队列：

- 半连接队列：接收一个SYN建立连接请求，进入SYN_RCVD状态
- 全连接队列（Accept）：完成TCP三次握手，进入ESTABLISHED状态

![ SYN 队列 与 Accpet 队列 ](https://cdn.xiaolincoding.com//mysql/other/format,png-20230309230542373.png)

- 参数1：socketfd 是 socketfd文件操作符
- 参数2：backlog
  - 在早期linux内核中，backlog是SYN队列大小
  - linux2.2后，backlog变成accept队列长度。上限值是内核参数somaxconn的大小。

## accept发生在三次握手的哪一步

客户端连接服务端时：

- 客户端发送SYN，并发送序列号client_isn，客户端进入SYN_SENT
- 服务端收到后回syn+ack，以及序列号+1，服务端进入SYN_RCVD
- 客户端协议栈收到ack让应用程序调用connect，单向连接建立，客户端进入ESTABLISHED，客户端返回ack和序列号+1
- 服务端收到ack，服务端也进入ESTABLISHED，服务端协议栈使得accept调用返回，双向连接建立成功

以上说明了，connect成功返回是在客户端第二次握手时，accept成功返回时在三次握手成功后。

## 客户端调用close，连接断开的流程

- 客户端调用close,表示客户端没有数据发送了，向服务端发送fin，进入fin_wait_1
- 服务端收到fin，tcp协议栈将fin包插入文件结束符EOF到接受缓冲区中，应用程序通过read感知fin包，EOF会放在排队等待的已接受数据之后。EOF表示该连接不再有额外数据到达，服务端进入CLOSE_WAIT
- 服务端处理完数据，读取到EOF，调用close关闭套接字，向客户端发fin，进入LASK_ACK
- 客户端收到fin，发送ack，客户端进入TIME_WAIT
- 服务端收到ACK，进入CLOSE
- 客户端在2MSL时间后，进入CLOSE

## 没有accept，能建立tcp连接嘛

可以

accept系统调用不参与tcp三次握手，只是负责从tcp全连接队列取出已经建立连接的socket，用户通过accept获取已经建立连接的socket来进行读写操作

## 没有listen，能建立tcp连接嘛

可以

客户端可以自己连自己形成连接，也可以两个客户端同时向对方发出请求连接。也就是说，可以没有服务器参与
