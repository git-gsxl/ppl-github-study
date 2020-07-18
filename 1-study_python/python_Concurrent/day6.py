# 初识多线程：threading
# 1、函数中多线程
# from threading import Thread
# import time
# def func(i):
#     time.sleep(2)
#     print(i)
#
# if __name__ == '__main__':
#     for i in range(5):
#         thread=Thread(target=func,args=(i,))
#         thread.start()


# 2、类中多线程
# from threading import Thread
# import time,os
# class MyTread(Thread):
#     def __init__(self,i):
#         super().__init__()
#         self.i=i
#     def run(self):          # 必须有run方法
#         time.sleep(1)
#         print('线程：',self.i+1,os.getpid())
# for i in range(10):
#     t=MyTread(i)
#     t.start()
# print('主线程：',os.getpid())


# 3、代码/数据/文件是共享的实例
# 但变量计算中会可能会同时拿到变量导致数据不安全，但可以加锁(GIL锁)
# from threading import Thread
# import time
# num=10                      # 定义一个全局变量
# class MyTread(Thread):
#     def __init__(self,i):
#         super().__init__()
#         self.i=i
#     def run(self):          # 必须有run方法
#         global num          # global声明变量
#         time.sleep(1)
#         print('线程：',self.i+num) # i+num
# for i in range(10):
#     t=MyTread(i)
#     t.start()

# # 4、多线程与多进程效率对比,同是100个。
# from threading import Thread
# import time
# from multiprocessing import Process
# def func(i):
#     return i+i
# if __name__ == '__main__':
#     start=time.time()
#     t_lst=[]
#     for i in range(100):
#         t=Thread(target=func,args=(i,))     # 多线程
#         t.start()
#         t_lst.append(t)
#     for i in t_lst:i.join()
#     t1=time.time()-start
#     print('多线程执行时间：',t1)
#
#     start=time.time()
#     p_lst=[]
#     for i in range(100):
#         p=Process(target=func,args=(i,))    # 多进程
#         p.start()
#         t_lst.append(p)
#     for i in p_lst:i.join()
#     t2=time.time()-start
#     print('多进程执行时间：',t2)


# threading模块其它方法
import threading,time
def func(i):
    time.sleep(0.5)
    print(i,threading.current_thread())     # 查看线程名字与id
    print(i,threading.get_ident())          # 查看线程id

for i in range(5):
    threading.Thread(target=func,args=(i,)).start()
print(threading.active_count())             # 查看活跃线程数(注意要加上主线程)
print(threading.enumerate())                # 查看线程所有项
print(threading.current_thread())           # 查看线程名字与id



'''
全局解释器GIL锁：
1.同一时间只能一个线程访问cpu；
2.锁的是什么？答：线程；
3.是Python自身的问题吗？答：是Cpython解释器的特性；


小结：
进程是最小的内存分配单位
线程是操作系统调度的最小单位
线程直接被CPU执行,进程内至少含有一个线程,也可以开启多个线程
    开启一个线程所需要的时间要远远小于开启一个进程
    多个线程内部有自己的数据栈,数据不共享
    全局变量在多个线程之间是共享的
GIL锁(即全局解释器锁)
在Cpython解释器下的python程序 在同一时刻 多个线程中只能有一个线程被CPU执行
高CPU : 计算类 --- 高CPU利用率
高IO  : 爬取网页 200个网页
        qq聊天   send recv
        处理日志文件 读文件
        处理web请求
        读数据库 写数据库
'''