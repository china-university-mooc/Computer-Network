# Wireshark Lab: DNS

## 1. nslookup

1. 运行nslookup以获取一个亚洲的Web服务器的IP地址。该服务器的IP地址是什么？

    ```
    > nslookup www.icourse163.org
    Server:		10.202.4.4
    Address:	10.202.4.4#53

    Non-authoritative answer:
    Name:	www.icourse163.org
    Address: 223.252.199.73
    ```
    中国大学MOOC服务器的IP地址为：223.252.199.73

2. 运行nslookup来确定一个欧洲的大学的权威DNS服务器。

    ```
    > nslookup -type=NS cam.ac.uk
    Server:		10.202.4.4
    Address:	10.202.4.4#53

    Non-authoritative answer:
    cam.ac.uk	nameserver = dns0.eng.cam.ac.uk.
    cam.ac.uk	nameserver = ns1.mythic-beasts.com.
    cam.ac.uk	nameserver = auth0.dns.cam.ac.uk.
    cam.ac.uk	nameserver = dns0.cl.cam.ac.uk.
    cam.ac.uk	nameserver = ns2.ic.ac.uk.
    cam.ac.uk	nameserver = ns3.mythic-beasts.com.

    Authoritative answers can be found from:
    ```
    剑桥大学的其中一个权威服务器为：dns0.eng.cam.ac.uk

3. 运行nslookup，使用问题2中一个已获得的DNS服务器，来查询Yahoo!邮箱的邮件服务器。它的IP地址是什么？

    ```
    > nslookup smtp.mail.yahoo.com
    Server:		10.202.4.4
    Address:	10.202.4.4#53

    Non-authoritative answer:
    smtp.mail.yahoo.com	canonical name = smtp.mail.global.gm0.yahoodns.net.
    Name:	smtp.mail.global.gm0.yahoodns.net
    Address: 106.10.248.80
    ```
    貌似不支持指定权威服务器查询，一直失败，直接查询得到IP：106.10.248.80

## 2. ipconfig

Mac 上清楚DNS缓存的命令
```
sudo dscacheutil -flushcache;sudo killall -HUP mDNSResponder;say cache flushed
```

### 3. 使用Wireshark追踪DNS

4. 找到DNS查询和响应消息。它们是否通过UDP或TCP发送？
    通过UDP发送

5. DNS查询消息的目标端口是什么？ DNS响应消息的源端口是什么？
    查询消息的目标端口号是53，响应消息的源端口也是53

6. DNS查询消息发送到哪个IP地址？使用ipconfig来确定本地DNS服务器的IP地址。这两个IP地址是否相同？
    发送到 114.114.114.114，跟本地DNS服务器IP一致

7. 查DNS查询消息。DNS查询是什么"Type"的？查询消息是否包含任何"answers"？

    Type是A，不包含任何sanswer

8. 检查DNS响应消息。提供了多少个"answers"？这些答案具体包含什么？

    ```
    Answers
    www.ietf.org: type CNAME, class IN, cname www.ietf.org.cdn.cloudflare.net
    www.ietf.org.cdn.cloudflare.net: type A, class IN, addr 104.20.1.85
    www.ietf.org.cdn.cloudflare.net: type A, class IN, addr 104.20.0.85
    ```
    提供了3个sanswer，包括该域名对应的规范主机名，以及规范主机名对应的两个IP地址
9. 考虑从您主机发送的后续TCP SYN数据包。 SYN数据包的目的IP地址是否与DNS响应消息中提供的任何IP地址相对应？
    与DNS响应消息中返回的IP之一一致

10. 这个网页包含一些图片。在获取每个图片前，您的主机是否都发出了新的DNS查询？
    没有发出新的DNS查询，因为之前查到的IP被缓存到本地了,不用重新查询

`nslookup www.mit.edu`

11. DNS查询消息的目标端口是什么？ DNS响应消息的源端口是什么？
    都是 53

12. DNS查询消息的目标IP地址是什么？这是你的默认本地DNS服务器的IP地址吗？
    目标IP是114.114.114.114，跟本地DNS服务器IP一致

13. 检查DNS查询消息。DNS查询是什么"Type"的？查询消息是否包含任何"answers"？
    Type是A，不包含任何sanswer

14. 检查DNS响应消息。提供了多少个"answers"？这些答案包含什么？
    提供了3个sanswer，包括两个别名记录，以及规范主机名对应的IP

15. 提供屏幕截图。
    ```
    Answers
    www.mit.edu: type CNAME, class IN, cname www.mit.edu.edgekey.net
    www.mit.edu.edgekey.net: type CNAME, class IN, cname e9566.dscb.akamaiedge.net
    e9566.dscb.akamaiedge.net: type A, class IN, addr 23.73.205.167
    ```

`nslookup -type=NS mit.edu`

16. DNS查询消息发送到的IP地址是什么？这是您的默认本地DNS服务器的IP地址吗？
    目标IP是114.114.114.114，跟本地DNS服务器IP一致

17. 检查DNS查询消息。DNS查询是什么"Type"的？查询消息是否包含任何"answers"？
    ```
    mit.edu: type NS, class IN
    ```
    type是NS，不包含任何answers

18. 检查DNS响应消息。响应消息提供的MIT域名服务器是什么？此响应消息还提供了MIT域名服务器的IP地址吗？
    提供了8个MIT域名服务器，不包含MIT域名服务器的IP地址

19. 提供屏幕截图。
    ```
    Answers
    mit.edu: type NS, class IN, ns ns1-173.akam.net
    mit.edu: type NS, class IN, ns asia1.akam.net
    mit.edu: type NS, class IN, ns use5.akam.net
    mit.edu: type NS, class IN, ns eur5.akam.net
    mit.edu: type NS, class IN, ns usw2.akam.net
    mit.edu: type NS, class IN, ns ns1-37.akam.net
    mit.edu: type NS, class IN, ns asia2.akam.net
    mit.edu: type NS, class IN, ns use2.akam.net
    ```
`nslookup www.aiit.or.kr ns1-173.akam.net`

20. DNS查询消息发送到的IP地址是什么？这是您的默认本地DNS服务器的IP地址吗？如果不是，这个IP地址是什么？
    发送到的IP地址是：193.108.91.173,不是默认的DNS服务器，是域名ns1-173.akam.net的IP

21. 检查DNS查询消息。DNS查询是什么"Type"的？查询消息是否包含任何"answers"？
    ```
    www.aiit.or.kr: type A, class IN
    ```
    Type为A，不包含任何answers

22. 检查DNS响应消息。提供了多少个"answers"？这些答案包含什么？
    由于查询失败，所以没有返回answers