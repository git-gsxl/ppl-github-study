import socket,subprocess,struct
sk=socket.socket()
sk.connect(('127.0.0.1',8888))

while 1:
    cmd=sk.recv(1024).decode('gbk')
    if cmd=='q':
        break
    res=subprocess.Popen(cmd,shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    std_out=res.stdout.read()
    std_err=res.stderr.read()
    len_num=len(std_out)+len(std_err)   # 长度
    num_by=struct.pack('i',len_num)     # struct处理后变为4个字节
    sk.send(num_by)                      # 先发送处理后的长度，让对方解字节
    sk.send(std_out)
    sk.send(std_err)
sk.close()