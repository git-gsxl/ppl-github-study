# 1、hmac的检验客户端合法性
# import socket,hmac
# sk=socket.socket()
# sk.connect(('127.0.0.1',9999))
# msg=sk.recv(1024)
# h=hmac.new(msg)
# digest=h.digest()
# sk.send(digest)
# sk.close()



# 2、socketserver处理并发：客户端
import socket
sk=socket.socket()
sk.connect(('127.0.0.1',9999))
while 1:
    msg=input('蒙柱宏：')
    if msg=='8':break
    sk.send(msg.encode('utf-8'))
    ret=sk.recv(1024).decode('utf-8')
    print(ret)
sk.close()