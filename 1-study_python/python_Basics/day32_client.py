
def client(sk,FlieName,FliePath,buffer=10240):

    head={
        'FlieName': FlieName,                                     # 文件名
        'FliePath': FliePath,                                     # 文件目录
        'FlieSize': None,}                                       # 文件大小为空
    cur_path=os.path.join(head['FliePath'],head['FlieName'])    # 拼接文件路径
    FlieSize=os.path.getsize(cur_path)                             # 获取文件字节大小
    head['FlieSize']=FlieSize                                     # 将文件大小传入head字典
    head_bytes=json.dumps(head).encode('utf-8')                   # 序列化
    head_len=len(head_bytes)                                       # 报头的长度
    head_pack=struct.pack('i',head_len)                            # pack为4个字节长度
    sk.send(head_pack)                                             # 发送pack的4个字节
    sk.send(head_bytes)                                            # 发送bytes类型报头
    with open(cur_path,'rb')as f:                                 # 打开拼接路径的文件
        while FlieSize:                                            # 如果FlieSize有数值
            if FlieSize>=buffer:                                    # 大于等于buffer，给下面直接写入buffer个字节
                sk.send(f.read(buffer))                            # 写入buffer个字节
                FlieSize-=buffer                                    # FlieSize每次减少buffer个字节
            else:
                sk.send(f.read(buffer))                            # 如果小于buffer个字节，直接读完
                break                                              # 读取完毕，退出循环
    sk.close()                                                      # 关闭连接
    return FlieSize

if __name__ == '__main__':
    import socket, struct, os, json
    sk = socket.socket()
    sk.connect(('127.0.0.1',8888))

    FlieName=r'bash教程.pdf'
    FliePath=r'C:\Users\Administrator\Desktop'
    print('上传成功，总共字节：',client(sk,FlieName,FliePath))
