
def sevrer(sk,ip,port,buffer=10240):
    sk.bind((ip, port))
    sk.listen()
    conn,addr=sk.accept()

    head_pack=conn.recv(4)                           # 先接收pack的4个字节
    head_len=struct.unpack('i',head_pack)[0]        # unpack解字节后得到一个元组，取第[0]个即可
    head=conn.recv(head_len).decode('utf-8')        # bytes报头内容
    head_loads=json.loads(head)                      # json报头内容
    FlieSize=head_loads['FlieSize']                 # 取json报头内容中FlieSize对应的值
    with open(head_loads['FlieName'],'wb')as f:    # 创建文件，名称=json报头内容中FlieName对应的名称
        while FlieSize:                              # 如果FlieSize有数值
            if FlieSize>=buffer:                     # 大于等于buffer，给下面直接写入buffer个字节
                f.write(conn.recv(buffer))           # 写入buffer个字节
                FlieSize-=buffer                     # FlieSize每次减少buffer个字节
            else:                                    # 如果小于buffer个字节，直接读完
                f.write(conn.recv(buffer))           # 读取完毕，退出循环
                break
    conn.close()
    sk.close()                                       # 结束，关闭连接

if __name__ == '__main__':
    import socket, struct, json
    sk = socket.socket()
    sevrer(sk,ip='127.0.0.1',port=8888)