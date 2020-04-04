# Wireshark Lab: HTTP

## 1. 基本HTTP GET/response交互

1. 您的浏览器是否运行HTTP版本1.0或1.1？服务器运行什么版本的HTTP？

    ```
    GET /wireshark-labs/HTTP-wireshark-file1.html HTTP/1.1\r\n

    HTTP/1.1 200 OK\r\n
    ```
    我的浏览器运行HTTP 1.1, 服务器也运行 HTTP 1.1

2. 您的浏览器会从接服务器接受哪种语言（如果有的话）？

    ```
    Accept-Language: zh-CN,zh;q=0.9\r\n
    ```
    浏览器期望接受中文，优先简体中文，权重0.9

3. 您的计算机的IP地址是什么？ gaia.cs.umass.edu服务器地址呢？

    ```
    "354","1585986392.144748","192.168.0.105","128.119.245.12","HTTP","537","GET /wireshark-labs/HTTP-wireshark-file1.html HTTP/1.1 "
    ```
    观察分组列表窗口得，我的IP为：192.168.0.105，服务器IP为：128.119.245.12

4. 服务器返回到浏览器的状态代码是什么？
    
    ```
    HTTP/1.1 200 OK\r\n
    ```
    状态码为200，表示请求成功

5. 服务器上HTML文件的最近一次修改是什么时候？

    ```
    Last-Modified: Sat, 04 Apr 2020 05:59:02 GMT\r\n
    ```
    最近一次修改为 2020-4-4 05:59:02

6. 服务器返回多少字节的内容到您的浏览器？

    ```
    Content-Length: 128\r\n
    ```
    服务器返回128字节内容

7. 通过检查数据包内容窗口中的原始数据，你是否看到有协议头在数据包列表窗口中未显示？ 如果是，请举一个例子。

    很多都没显示，比如 Keep-Alive、Connection

## 2. HTTP条件Get/response交互

8. 检查第一个从您浏览器到服务器的HTTP GET请求的内容。您在HTTP GET中看到了“IF-MODIFIED-SINCE”行吗？

    没有看到

9. 检查服务器响应的内容。服务器是否显式返回文件的内容？ 你是怎么知道的？

    ```
    HTTP/1.1 200 OK\r\n
    Content-Length: 371\r\n
    ```
    显式的返回了，因为响应200，并且 Content-Length 不为 0

10. 现在，检查第二个HTTP GET请求的内容。 您在HTTP GET中看到了“IF-MODIFIED-SINCE:”行吗？ 如果是，“IF-MODIFIED-SINCE:”头后面包含哪些信息？

    ```
    If-Modified-Since: Sat, 04 Apr 2020 05:59:02 GMT\r\n
    ```
    看到了“IF-MODIFIED-SINCE:”行，包含上次请求文件时获得的Last-Modified时间

11. 针对第二个HTTP GET，从服务器响应的HTTP状态码和短语是什么？服务器是否明确地返回文件的内容？请解释。

    ```
    HTTP/1.1 304 Not Modified\r\n
    ```
    返回状态码为304，短语为 Not Modified，没有返回文件内容，因为在上次请求到本次请求之间，服务器端的文件没有改变，所以服务器返回304，告诉浏览器可以使用本地的缓存

## 3. 检索长文件

12. 您的浏览器发送多少HTTP GET请求消息？哪个数据包包含了美国权利法案的消息？

    浏览器只发送了一个请求消息，响应的数据包中共均包含了权利法案的消息

13. 哪个数据包包含响应HTTP GET请求的状态码和短语？

    响应的第一个数据包

14. 响应中的状态码和短语是什么？

    ```
    HTTP/1.1 200 OK\r\n
    ```
    响应的状态码为200，短语为OK

15. 需要多少包含数据的TCP段来执行单个HTTP响应和权利法案文本？

    ```
    [4 Reassembled TCP Segments (4861 bytes): #79(1408), #80(1408), #81(1408), #93(637)]
    [Frame: 79, payload: 0-1407 (1408 bytes)]
    [Frame: 80, payload: 1408-2815 (1408 bytes)]
    [Frame: 81, payload: 2816-4223 (1408 bytes)]
    [Frame: 93, payload: 4224-4860 (637 bytes)]
    [Segment count: 4]
    [Reassembled TCP length: 4861]
    [Reassembled TCP Data: 485454502f312e3120323030204f4b0d0a446174653a2053…]
    ```
    需要4个包含数据的TCP段

## 4. 具有嵌入对象的HTML文档

16. 您的浏览器发送了几个HTTP GET请求消息？ 这些GET请求发送到哪个IP地址？

    浏览器发送了3个GET请求，都发送到了 128.119.245.12
  
17. 浏览器从两个网站串行还是并行下载了两张图片？请说明。

    串行下载的两张图，因为浏览器在收到第一张图的响应后，才发出对第二张图的请求

## 5. HTTP认证

18. 对于您的浏览器的初始HTTP GET消息，服务器响应（状态码和短语）是什么响应？

    ```
    HTTP/1.1 401 Unauthorized\r\n
    ```
    响应的状态码为401，短语为Unauthorized，即未授权，要先认证才能访问

19. 当您的浏览器第二次发送HTTP GET消息时，HTTP GET消息中包含哪些新字段？

    ```
    Authorization: Basic d2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms=\r\n
    ```
    包含了 Authorization 字段
    