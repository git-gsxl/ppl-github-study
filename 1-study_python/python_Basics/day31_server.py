'''
一、socket
'''
# 1、基于TCP协议的socket
# tcp是基于链接的，必须先启动服务端，然后再启动客户端去链接服务端
# import socket
# sk=socket.socket()
# sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# sk.bind(('192.168.1.124',8080)) # 绑定服务端的：IP+端口
# sk.listen()                       # 监听连接
# conn, addr = sk.accept()          # 接收连接 三次握手conn
# lis=list(addr)
# print('IP:%s 端口:%s 已请求连接！'%(lis[0],lis[1]))
# while 1:
#     res=conn.recv(1024).decode('utf-8')        # 接收信息
#     print(res)
#     if res=='886':break
#     ret=input('美女>>>')
#     if ret=='886':
#         conn.send(bytes(ret.encode('utf-8')))  # 发送信息
#     conn.send(bytes(ret.encode('utf-8')))      # 发送信息
# conn.close()                                     # 关闭客户端套接字
# sk.close()                                       #关闭服务器套接字


# 2、基于UDP协议的socket
# udp是无链接的，启动服务之后可以直接接受消息，不需要提前建立链接
# import socket
# udp_sk = socket.socket(type=socket.SOCK_DGRAM)   # 创建一个服务器的套接字
# udp_sk.bind(('127.0.0.1',8080))                 # 绑定服务器套接字
# msg,addr = udp_sk.recvfrom(1024)
# print(msg)
# udp_sk.sendto(b'udp_server',addr)               # 对话(接收与发送)
# udp_sk.close()                                   # 关闭服务器套接字



# 3、长链接
# 因同一时间只能一个程序链接，所以多个只会连接一个
import socket
sk=socket.socket()
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sk.bind(('192.168.1.124',8080)) # 绑定服务端的：IP+端口
sk.listen()                       # 监听连接
while 1:
    conn, addr = sk.accept()  # 接收连接 三次握手conn
    lis = list(addr)
    print('IP:%s 端口:%s 已请求连接！' % (lis[0], lis[1]))
    while 1:
        res = conn.recv(1024).decode('utf-8')  # 接收信息
        print(res)
        if res=='886':break
        ret=input('美女>>>')
        if ret=='886':
            conn.send(bytes(ret.encode('utf-8')))  # 发送信息
        conn.send(bytes(ret.encode('utf-8')))      # 发送信息
    conn.close()                                     # 关闭客户端套接字
