# import socket
# sk=socket.socket()                         # 创建客户套接字
# sk.connect(('192.168.1.124',8080))       # 尝试连接服务端
# while 1:
#     ret=input('帅哥>>>')
#     if ret=='886':
#         sk.send(bytes(ret.encode('utf-8')))
#         break
#     sk.send(bytes(ret.encode('utf-8')))     # 发送信息
#     msg=sk.recv(1024).decode('utf-8')       # 接收信息
#     print(msg)
#     if msg=='886':break
# sk.close()                                   # 关闭客户套接字


# 2、基于UDP协议的socket
# import socket
# ip_port=('127.0.0.1',8080)
# udp_sk=socket.socket(type=socket.SOCK_DGRAM)
# udp_sk.sendto(b'udp_client',ip_port)
# back_msg,addr=udp_sk.recvfrom(1024)
# print(back_msg.decode('utf-8'),addr)

# 3、长链接
# 因同一时间只能一个程序链接，所以多个只会连接一个
import socket
sk=socket.socket()                         # 创建客户套接字
sk.connect(('192.168.1.124',8080))       # 尝试连接服务端
while 1:
    ret=input('帅哥>>>')
    if ret=='886':
        sk.send(bytes(ret.encode('utf-8')))
        break
    sk.send(bytes(ret.encode('utf-8')))     # 发送信息
    msg=sk.recv(1024).decode('utf-8')       # 接收信息
    print(msg)
    if msg=='886':break
sk.close()                                   # 关闭客户套接字
