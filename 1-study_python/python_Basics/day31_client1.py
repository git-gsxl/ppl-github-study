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