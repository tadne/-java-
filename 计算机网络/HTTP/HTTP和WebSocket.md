# HTTP和WebSocket协议

HTTP在应用中往往是：用户点击，前端发HTTP请求，网站返回HTTP响应

但是这种情况下，服务器不会主动给客户端发消息，例：你并没有点击鼠标，刷网页时就突然弹出的广告..，并且还是动图..

### 用HTTP轮询

**怎么样在用户不做任何操作的情况下，网页也能收到消息并发生变动？**

常见方案：网页的前端代码定时不停发HTTP到服务器，服务器再响应。

这是一种伪服务器推送模式，这种场景常见的有扫码登录。一些平台扫码登录页面，前端不知道你扫了没，只能不停请求服务器查询你扫没扫

HTTP轮询的问题：
- 当打开F12页面时，发现满屏HTTP请求，占用带宽和下游服务器负担
- 最坏情况下，用户要等待好几秒才能触发下次HTTP请求才能跳转页面

### 长轮询
HTTP请求发出后，服务器会留一定时间做响应。

如果**HTTP请求将超时设置的很大**，如30秒，在这**30秒内只要服务器收到扫码请求就返回给客户端**。超时就立即重试

这样就可以减少HTTP请求的数量，并且在30秒的区间扫码可以很快响应。这就是长轮询机制。常用的RocketMQ就用到了这种方式

但是，这种机制只能适应简单的场景，如果是网页游戏，那大量的数据要从服务器推送到客户端，这种方式就无法适应了

### WebSocket是什么

TCP连接的两端，**在同一时间，双方都可以主动向对方发数据**，这既是全双工。

现在使用广泛的HTTP1，**客户端和服务器只能有一方主动发数据**，这是半双工

因为TCP设计之初，考虑的是网页文本的场景，客户端请求再服务器响应就够了，不需要考虑网页游戏

现在需要一款基于TCP的新协议，于是有了新应用层协议WebSocket协议

### 怎么建立WebSocket连接
网页文本要使用HTTP协议、网页游戏要使用WebSocket协议。

要兼容这种场景，浏览器在三次握手后，统一使用HTTP进行一次通信。
- 如果是普通HTTP请求，就按照HTTP协议交互
- 如果是想建立WebSocket连接，就会在HTTP请求的请求头中添加特殊heade头

请求头如下：

    Connection: Upgrade
    Upgrade: WebSocket
    Sec-WebSocket-Key: T2a6wZlAwhgQNqruZ2YUyg==\r\n

这些请求头的意思是，浏览器想升级协议，并且想升级为WebSocket协议。同时带上一段随机生成的 base64 码（Sec-WebSocket-Key），发给服务器。

接下来如果浏览器支持WebSocket协议，就会进行WebSocket的握手流程，同时根据base64码用一个公开算法变成一段字符串，放在HTTP的响应头中，并带上101状态码

响应如下：

    HTTP/1.1 101 Switching Protocols\r\n
    Sec-WebSocket-Accept: iBJKv/ALIW2DobfoA4dmr3JHBCY=\r\n
    Upgrade: WebSocket\r\n
    Connection: Upgrade\r\n

- 状态码101：协议切换
浏览器用同样的公开算法将base64码转换为另一段字符串，如果字符串和服务器传的一致就验证通过。这样就完成了两次HTTP握手，WebSocket就建立完成。

其实可以注意到WebSocket和HTTP都是基于TCP协议，经理TCP三次握手后，用HTTP协议升级为WebSocket协议，但是这不是说WebSocket是基于HTTP的协议，它只是升级时相关，升级之后就没有任何关系了

### WebSocket的消息格式
![alt text](3a63a86e5d7e72a37b9828fc6e65c21f.webp)

其中只要关注以下几个字段：

opcode字段： 用来标志数据帧的类型，如1表示text类型数据，2表示二进制类型数据
payload字段：存放真正传输的数据的长度，单位是字节
payload data字段：存放的就是真正要传输的数据

其实WebSocket的数据格式也是数据头+数据的形式，这是因为TCP本身就是全双工，但直接用TCP传输数据有粘包问题，上层协议要用消息头和消息体格式包装数据定义边界。消息头中有消息长度来截取消息体。HTTP、RPC、WebSocket都一样。

### WebSocket使用场景
WebSocket继承了TCP的全双工能力，解决了粘包问题。

适用于**服务器和客户端频繁交互**的场景

比如游戏，需要数据的大量计算和互动

### 总结
- TCP协议是全双工的，但常用的HTTP1是半双工的，对要求服务器主动推送数据的场景不友好
- HTTP1中，只要客户端不问，服务端就不答。这种情况下简单的服务器推送场景可以使用长轮询或者定时轮询来处理
- 对于客户端和服务器频繁交互的场景，还是要考虑使用WebSocket协议
- 各个浏览器都支持HTTP，所以使用HTTP协议升级为WebSocket比较方便，但是升级之后，WebSocket就和HTTP无关了。