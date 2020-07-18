'''
进程：启动多个进程 进程之间是由操作系统负责调用
线程：启动多个线程 真正被CPU执行的最小单位实际是线程
     开启一个线程 创建一个线程 寄存器 堆栈
     关闭一个线程
协程：
    本质上是一个线程能够在多个任务之间切换来节省一些IO时间
    协程中任务之间的切换也消耗时间,但是开销要远远小于进程线程之间的切换
进程和线程的任务切换是操作系统调度
协程任务之间可以通过代码调度切换(但只有协程模块能识别的IO操作才能实现效果)
'''
# 一、初识协程：greenlet例子
# 执行A函数切换至B函数执行后，又切换回A函数。一般编程高并发用：进程+线程+协程
# from greenlet import greenlet
# def func():
#     print('func_start')
#     r2.switch()                 # 切换到r2，并记录func函数的执行到的位置
#     print('func_end')
# def func1():
#     print('func1_start')
#     r1.switch()                 # 切换到r1，所以最后会打印func_end
#     print('func1_end')
# r1=greenlet(func)
# r2=greenlet(func1)
# r1.switch()

# 2、gevent:协程
'''
gevent.sleep(2)模拟的是gevent可以识别的io阻塞,而time.sleep(2)或其他的阻塞,gevent是不能直接识别的需要用下面一行代码,打补丁,就可以识别了,from gevent import monkey;monkey.patch_all() 必须写上，最后直接写在导入模块前。
'''
# from gevent import monkey;monkey.patch_all()
# import gevent
# import time
# def func():
#     print('func_start')
#     time.sleep(1)       # 只能导入：monkey;monkey.patch_all() 才能感知
#     # gevent.sleep(1)   # 否则用自己的模块的等待
#     print('func_end')
# def func1():
#     print('func1_start')
#     time.sleep(1)
#     # gevent.sleep(1)
#     print('func1_end')
# r1=gevent.spawn(func)   # 起一个协程任务
# r2=gevent.spawn(func1)  # 起一个协程任务
# r1.join()           # 执行
# r2.join()           # 执行

# 3、同步与异步
# from gevent import monkey;monkey.patch_all()
# import gevent
# import time
#
# def func():
#     time.sleep(1)
#     print(666)
# def sync():             # 同步
#     for i in range(2):
#         func()
# def async():            # 异步
#     g_lst=[]
#     for i in range(5):
#         g=gevent.spawn(func)
#         g_lst.append(g)
#     gevent.joinall(g_lst)
# sync()
# async()


''' 二、协程应用实例 '''
# 1、简单爬虫实例

# ①正常写法，没有协程：
# import requests,time
# s=requests.session()
# def get_len(url):
#     r=s.get(url)
#     return len(r.text)
#
# urls=['https://www.cnblogs.com/gsxl/','http://news.baidu.com/','https://www.baidu.com/',
#      'https://daohang.qq.com/?fr=hmpage','https://www.csdn.net/']
# start=time.time()
# for url in urls:
#     r=get_len(url)
#     print(r)
# t1=time.time()-start
# print('时间：',t1)

# ②运用协程：gevent
# from gevent import monkey;monkey.patch_all()
# import requests,time
# import gevent
# s=requests.session()
# def get_len(url):
#     r=s.get(url)
#     return len(r.text)
#
# urls=['https://www.cnblogs.com/gsxl/','http://news.baidu.com/','https://www.baidu.com/',
#      'https://daohang.qq.com/?fr=hmpage','https://www.csdn.net/']
# r_lst=[]
# start=time.time()
# for url in urls:
#     r=gevent.spawn(get_len,url)
#     r_lst.append(r)
# gevent.joinall(r_lst)
# for i in r_lst:
#     print(i.value)
# t1=time.time()-start
# print(t1)