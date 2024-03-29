## HTTP特性

到目前为止，HTTP常见版本有： HTTP/1.1,HTTP/2.0,HTTP/3.0  不同版本特性不同

### HTTP/1.1

##### 优点

**简单、灵活、和易于扩展、应用广泛和跨平台**

1. 简单： HTTP基本的报文格式就是header+body，头部信息也是key-value简单文本的形式，易于理解，降低了学习和使用的门槛
2. 灵活和易于扩展： HTTP协议中的各类请求方法、URL/URI、状态码想、头字段等组成没有被固定，运行开发自定义和扩展，同时HTTP由于工作在应用层，它的下层可以随意变化。
   1. 比如HTTPS就是HTTP和TCP间增加SSL/TLS安全传输层
   2. HTTP/1.1和HTTP/2.0传输协议使用的是TCP协议，到了HTTP/3.0传输协议改为使用UDP协议
3. 应用广泛和跨平台。

##### 缺点

HTTP协议里有优缺点一体的双刃剑，分别是【无状态、明文传输】，同时还【不安全】

1. 无状态：
   1. 好处是服务器不会记忆HTTP状态，不需要额外的资源来记录状态信息，能减轻服务器的负担，能把更多CPU和内存用来对外提供服务。
   2. 坏处是服务器没有记忆能力，在完成有关联性的操作时非常麻烦，比如登录、添加购物车、..、支付。由于无状态这一串操作每次都要进行身份验证
      1. 解决方案： 比较多，简单的有Cookie，通过在请求和响应报文中写入Cookie来控制客户端状态。相当于客户端请求后，服务器下发有客户信息的Cookie，后续客户端再次请求时，带上它就能识别了
2. 明文传输
   1. 传输过程中可以方便阅读，如Wireshark抓包可以直接肉眼查看，调式方便，但是信息裸奔。
3. 不安全
   1. 明文传输导致信息泄露
   2. 不验证通信放身份，容易遭遇伪装
   3. 不能证明报文完整性，可能被篡改，如植入广告等

安全问题可以使用HTTPS解决，也就是引入SSL/TLS层，使安全上达到极致

##### 性能

HTTP协议基于TCP/IP，使用了请求-应答的通信方式，性能的关键在两点

1. 长连接
   1. 早期HTTP/1.0每次发起请求都要三次握手，做了无谓的TCP建立和断开，增加了通信开销
   2. 为了解决这个问题，HTTP/1.1提出了长连接的通信方式，也叫持久连接。
      1. 好处：减少了TCP连接的重复建立和断开，减轻的服务器的负载
   3. 特点：只要任意一端没有明确提出断开连接就保存连接，但如果HTTP连接长时间没有数据交互，服务端会主动断开
2. 管道网络传输
   1. HTTP/1.1采用了长连接的方式，使得管道网络传输成为可能，即在同一个TCP连接中，客户端可以发出多个请求，而不必等待请求的响应
      1. 这样就解决了请求的队头阻塞问题，也就是某个请求的丢失或者延迟导致持续没有响应，无法再次发出请求的问题。
      2. 但是这样只解决了请求的队头阻塞，没有解决响应的队头阻塞。
   2. 管道技术在HTTP/1.1中不是默认开启，而且浏览器基本不支持，也就是这个功能基本不怎么使用

##### 对头阻塞

请求应答的模式会造成HTTP性能问题。因为当顺序发送请求序列中的请求因为某种原因被阻塞时，后面排队的请求也会阻塞，导致客户端请求不到数据，这就是对头阻塞

##### 总结

HTTP/1.1就是性能不咋地，后续的版本都是在优化性能
