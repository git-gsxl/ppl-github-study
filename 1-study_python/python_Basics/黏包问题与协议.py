'''
1、解决黏包问题
    为什么会出现黏包现象?
    ①首先只有在TCP协议中才会出现黏包现象,
    ②是因为TCP协议是面向流的协议
    ③在发送的数据传输的过程中还有缓存机制来避免数据丢失
    ④因此在连续发送小数据的时候以及接收大小不符的时候都容易出现黏包现象
    ⑤本质还是因为我们在接收数据的时候不知道发送的数据的长短

2、解决黏包问题
    ①在传输大量数据之前先告诉接收端要发送的数据大必
    ②如果想更漂亮的解决问题，可以通过struct模块 来定制协议

3、struct模块
    pack unpack
    模式 'i'
    pack之后的长度为4个字节
    unpack之后拿到的数据是一个元祖。元祖的第一个元素才是pack的值

'''

'''
1.端口号
2.网络编程
3.mac地址
4.arp协议:通过ip找mac
5.ip地址是什么-一台机器在网络上的位置#公网ip 局域网ip
6.网络相关的程序才需要开一个端口，为的是能找到某台计算机上唯一的一个程序#在同一台机器上同一时间只能有一个程序占用同一个端口,一般情况下，8000之后
7.TCP协议和UDP协议
    tcp协议:可靠的，面向连接的，耗时长
    三次握手
    四次挥手
8.udp协议:不可靠无连接，效率高

9.ip协议属于网络osi七层协议中的哪一一层: 网络层
    tcp协议udp协议属于传输层
    arp协议 属于数据链路层
'''