'''
一、hmac的检验客户端合法性
基本逻辑：客户端生成一串密文发送给客户端接收，客户端发送的时候要先校验是否与客户端密文一致
'''
# import socket,os,hmac
# sk=socket.socket()
# sk.bind(('127.0.0.1',9999))
# sk.listen()
# conn,addr=sk.accept()
#
# def exp():
#     msg=os.urandom(32)              # 随机生成字节
#     conn.send(msg)                  # 发送随机生成的字节
#     digest=hmac.new(msg).digest()  #  生成密文给下面对比
#     res_digest=conn.recv(1024)      # 接收客户端的密文
#     res=hmac.compare_digest(digest,res_digest)   # 对比服务端与客户端的密文是否相等，返回bool
#     return res
# res=exp()
# if res:
#     print('合法请求')
#     sk.close()
# else:
#     print('不合法请求')
#     sk.close()

'''
二、socketserver处理并发
'''
import socketserver
class Mysevrer(socketserver.BaseRequestHandler):
    def handle(self):
        while 1:
            msg=self.request.recv(1024).decode('utf-8')
            if msg=='8':break
            print('蒙柱宏：'+msg)
            info=input('广深小龙：')
            self.request.send(info.encode('utf-8'))

if __name__ == '__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',9999),Mysevrer)
    server.serve_forever()


