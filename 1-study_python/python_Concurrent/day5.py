'''
一、进程池
每开启进程,开启属于这个进程的内存空间；
能提升计算机的效率，进程过多 操作系统的调度；
    python中的进程池，是先创建一个属于进程的池子；
    进程池能指定能存放n个进程执行；
'''
# from multiprocessing import Pool,Process
# import time
# def func(i):
#     print(i)
#
# if __name__ == '__main__':
#     # 进程池的效果
#     st=time.time()
#     pool=Pool(5)                # 池子可放5个(一般CPU的个数+1)
#     pool.map(func,range(100))   # 100个进程任务
#     t1=time.time()-st
#     st=time.time()
#     print('进程池时间：',t1)
#
#     # 原来多进程的效果
#     p_lst=[]
#     for i in range(100):
#         p=Process(target=func,args=(i,))
#         p_lst.append(p)
#         p.start()
#     for p in p_lst:p.join()
#     t2=time.time()-st
#     print('多进程时间：',t2)

#  2、进程池传多个参数：
# from multiprocessing import Pool
# import time
# def func(i):
#     print(i)
#
# if __name__ == '__main__':
#     st=time.time()
#     pool=Pool(5)
#     pool.map(func,[(10,'name','age'),100])

# # 3、apply：同步
# from multiprocessing import Pool
# import time
# def func():
#     print('--开始~')
#     time.sleep(0.1)
#     print('==结束！'+'\n')
# if __name__ == '__main__':
#     pool=Pool()
#     for i in range(5):
#         pool.apply(func)       # 同步了

# 4、apply_async：异步
# from multiprocessing import Pool
# import time,os
# def func(i):
#     pid=os.getpid()
#     print('%s--开始~:%s'%(i,pid))
#     time.sleep(1)
# if __name__ == '__main__':
#     pool=Pool(2)
#     for i in range(5):
#         pool.apply_async(func,(i,))
#     pool.close()        # 结束进程池接收任务
#     pool.join()         # 感知进程池中的任务执行结束

# 5、apply_async实现：sevrer服务端
# def sevrer(conn):
#     conn.send(b'hello!!!')
#     msg=conn.recv(1024).decode('utf-8')
#     print(msg)
#     conn.close()
# if __name__ == '__main__':
#     import socket
#     from multiprocessing import Pool
#     sk = socket.socket()
#     sk.bind(('127.0.0.1', 8888))
#     sk.listen()
#     p = Pool(2)
#     while 1:
#         conn,addr=sk.accept()
#         p.apply_async(sevrer,args=(conn,))

# 5、进程池的返回值
# apply:直接接收返回值
# apply_async:需要get(),会堵塞因等待返回值，解决可先放列表get()
# from multiprocessing import Pool
# import time
# def func(i):
#     time.sleep(0.5)
#     return i+1
# if __name__ == '__main__':
#     p=Pool(3)
#     p_lst=[]
#
#     for i in range(10):
#         res=p.apply(func,args=(i,))        # 直接接收返回值
#         print(res)

    #     res=p.apply_async(func,args=(i,))   # apply_async
    #     p_lst.append(res)
    # for i in p_lst:print(i.get())

    # res=p.map(func,range(10))               # map一次性返回
    # print(res)

# 6、进程池回调函数
# 先执行异步函数func，将func返回值传入func1函数中的ii参数。
# 回调函数是在主进程中执行，而不是子进程中。
from multiprocessing import Pool
def func(i):
    return i
def func1(ii):
    print('i+1=',ii+1)
if __name__ == '__main__':
    p=Pool()
    for i in range(5):
        p.apply_async(func,args=(i,),callback=func1)
    p.close()
    p.join()

'''
总结：
p=Pool()：实例化；
p.map(函数名,可迭代类型)：默认异步的执行任务,且自带close和join；
p.apply：同步调用；
p.apply_async：异步调用和主进程完全异步，需要手动close和join；
'''