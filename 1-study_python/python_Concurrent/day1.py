# 1、多线程
'''
# 多进程代码
# from multiprocessing import Process
# 方法
    .start()：开启一个子进程
    .join()：感知一个子进程的结束
    .terminate()：结束一个子进程
    .is_alive()：查看某个子进程是否还在运行
# 属性
    # .name        进程名
    # .pid         进程号
    # .daemon      值为True的时候,表示新的子进程是一个守护进程
            # 守护进程 随着主进程代码的执行结束而结束
            # 一定在start之前设置


# from multiprocessing import Lock
# l = Lock()
# l.acquire()   # 拿钥匙
# 会造成数据不安全的操作
# l.release()   # 还钥匙
'''
# 异步多线程
# from multiprocessing import Process
#
# def func(arg1,arg2):
#     print('arg1:',arg1)
#     print('arg2:',arg2)
#
# if __name__ == '__main__':
#     p=Process(target=func,args=(5,8))
#     p.start()
#     print('》》》最后一行代码的打印') # 没约束时，不会待线程执行完再执行下面的代码

# 2、join()：感知子进程的结束，将异步变为同步
# from multiprocessing import Process
#
# def func(arg1,arg2):
#     print('arg1:',arg1)
#     print('arg2:',arg2)
#
# if __name__ == '__main__':
#     p=Process(target=func,args=(5,8))
#     p.start()
#     p.join()        # 感知子进程的结束，将异步变为同步
#     print('》》》最后一行代码的打印')


# 3、多个子进程执行
# from multiprocessing import Process
# import time
#
# def func(arg1,arg2):
#     print('arg1:',arg1)
#     time.sleep(0.1)
#     print('arg2:',arg2)
#
# if __name__ == '__main__':
#     p_list=[]
#     for i in range(5):              # 异步多个子进程同时执行
#         p = Process(target=func, args=(1*i, 10))
#         p_list.append(p)
#         p.start()
#         p.join()
#     print('哈哈哈！')

# 多线程+列表推导式
# from multiprocessing import Process
# import time
#
# def func(arg1,arg2):
#     print('arg1:',arg1)
#     time.sleep(0.1)
#     print('arg2:',arg2)
#
# if __name__ == '__main__':
#     p_list=[]
#     for i in range(5):              # 异步多个子进程执行
#         p = Process(target=func, args=(1*i, 10))
#         p_list.append(p)
#         p.start()
#     [p.join() for p in p_list]      # 必须执行完多个子进程后，再执行下面的代码。
#     print('哈哈哈！')

# 4、另一种多线程,自定义类继承Process
# from multiprocessing import Process
# import time
# class My_func(Process):
#     def __init__(self,num):
#         super().__init__()      # 传参数需用继承的方法解决
#         self.num=num
#
#     def run(self):
#         '''下面多线程要运行的代码'''
#         print(self.num)
#         time.sleep(0.1)
#         print(self.num*self.num)
# if __name__ == '__main__':
#     p1=My_func(1)
#     p1.start()
#     p2=My_func(2)
#     p2.start()

'''
二、守护进程
守护进程 会 随着 主进程的代码执行完毕 而 结束
在主进程内结束一个子进程 p.terminate()
     结束一个进程不是在执行方法之后立即生效,需要一个操作系统响应的过程
检验一个进程是否活着的状态 p.is_alive()
p.name p.pid 这个进程的名字和进程号
'''
# from multiprocessing import Process
# import time
# def func():
#     while 1:
#         time.sleep(1)
#         print('func1')
# if __name__ == '__main__':
#     p=Process(target=func)
#     p.daemon=True           # 设置为守护进程
#     p.start()
#     print(1)
#     print(p.is_alive())     # 查看进度是否存在，返回bool
#     time.sleep(2)
#     # p.terminate()           # 结束一个进程
#     print(p.is_alive())
#     time.sleep(2)
#     print('守护进程随着所有主进程执行后而结束！！')
#     print(p.is_alive())

'''
三、进程锁
'''
# 每天免费开放10张门票
from multiprocessing import Process,Lock
import time,json
def find():
    with open(r'test.py')as f:
        d = json.load(f)
    print('剩余免费门票：%s'%d['count'])

def buy(i,):
    # lock.acquire()                          # 拿钥匙
    with open(r'test.py')as f:
        d = json.load(f)
    if d['count']<=0:print('门票已被抢完~')
    else:
        print('恭喜用户 %s 成功抢到门票了'%i)
    if d['count']!=0:d['count']-=1
    time.sleep(0.2)
    with open(r'test.py', 'w')as f:
        json.dump(d,f)
    # lock.release()                          # 还钥匙
if __name__ == '__main__':
    for i in range(1):       # 5个线程同时查询
        p=Process(target=find)
        p.start()
    lock=Lock()
    for i in range(5):
        p1=Process(target=buy,args=(i,))
        p1.start()
















