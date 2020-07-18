import socket
sk=socket.socket()
sk.connect(('127.0.0.1',9999))
while 1:
    msg=input('send：')
    if msg=='8':break
    sk.send(msg.encode('utf-8'))
    ret=sk.recv(1024).decode('utf-8')
    print(ret)
sk.close()