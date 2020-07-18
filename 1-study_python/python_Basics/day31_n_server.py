import socket,struct
sk=socket.socket()
sk.bind(('127.0.0.1',8888))
sk.listen()
conn,addr=sk.accept()
while 1:
    cmd=input('请输入命令：')
    if cmd=='q':
        conn.send(b'q')
        break
    conn.send(cmd.encode('gbk'))     # win系统gbk编码
    num=conn.recv(4)
    num=struct.unpack('i',num)[0]    # 将4个字节解码转为原来的大小
    print(num)
    res=conn.recv(int(num)).decode('gbk')
    print(res)
conn.close()
sk.close()