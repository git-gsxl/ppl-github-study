''' 一、线程锁 '''
# # 1、Lock给线程加锁
# from threading import Thread,Lock
# import time
# def func(l):
#     l.acquire()     # 拿钥匙
#     global num
#     t=num
#     time.sleep(0.1)
#     num=t-1
#     l.release()     # 还钥匙
# num=5
# t_lst=[]
# l=Lock()
# for i in range(5):
#     t=Thread(target=func,args=(l,))
#     t.start()
#     t_lst.append(t)
# for i in t_lst:i.join()
# print(num)
#

# 2、递归锁，用来解决Lock互斥锁造成死锁问题
# # ①死锁：被堵塞了，多次acquire()造成
# from multiprocessing import Lock
# rl=Lock()
# rl.acquire()
# rl.acquire()
# rl.acquire()
# rl.acquire()
# rl.acquire()
# print(6666)

# ②RLock：递归锁，可以在一个线程中acquire()多次。
# from multiprocessing import RLock
# rl=RLock()          # 递归锁：RLock
# rl.acquire()
# rl.acquire()
# rl.acquire()
# rl.acquire()
# rl.acquire()
# print(6666)

''' 二、信号量 '''
# from threading import Semaphore,Thread
# import time
# def func(s):
#     s.acquire()
#     print(111)
#     time.sleep(2)
#     s.release()
# s=Semaphore(2)      # 2个线程，既每次运行2个线程。
# for i in range(10):
#     t=Thread(target=func,args=(s,))
#     t.start()


''' 三、事件 '''
# from threading import Event,Thread
# import time,random
# def connect(e):
#     count=0
#     while count<3:
#         e.wait(0.5)             # 如果is_set()为False,等待0.5s就结束。
#         if e.is_set()==True:
#             print('连接成功！')
#             break
#         else:
#             count+=1
#             print('第%s次连接失败~')
#     else:print('TimeoutError 连接超时')
#
# def check(e):
#     time.sleep(random.randint(0,3))
#     e.set()
# e=Event()
# t=Thread(target=connect,args=(e,))
# t1=Thread(target=check,args=(e,))
# t.start()
# t1.start()


''' 四、条件和定时器 '''
# 2、Condition：条件
# wait()等待，钥匙是一次性的。
# from threading import Thread,Condition
# def func(con,i):
#     con.acquire()
#     con.wait()          # 等钥匙，不会归还，用了就没有了。
#     print('我是：',i)
#     con.release()
#
# if __name__ == '__main__':
#     con=Condition()
#     for i in range(10):
#         t=Thread(target=func,args=(con,i))
#         t.start()
#     while 1:
#         num=int(input('>>>'))
#         con.acquire()
#         con.notify(num)     # 造钥匙数量
#         con.release()

# # 2、定时器
# from threading import Timer
# import time
# def func():
#     print('等待了3s')
# while 1:
#     Timer(3,func).start()       # 成了同步
#     time.sleep(3)

# 4、队列
# # ①普通队列，先进先出
# import queue
# q=queue.Queue()
# q.put(1)
# q.put(2)
# print(q.get())
# print(q.get())
#
# # ②栈：先进后出
# q=queue.LifoQueue()
# q.put(1)
# q.put(2)
# print(q.get())  # get取到的是2，先进后出。
# print(q.get())
#
# # ③优先级队列
# q=queue.PriorityQueue()
# q.put(11)
# q.put(10)
# q.put(20)
# print(q.get())

# 5、线程池
from concurrent.futures import ThreadPoolExecutor
import time
def func(i):
    time.sleep(1)
    return i
def func1(i):
    msg=i.result()                        # 拿返回值
    print(msg+100)
tp=ThreadPoolExecutor(max_workers=5)     # 默认为计算机本身的cpu个数
# 回调函数
for i in range(10):
    t=tp.submit(func,i).add_done_callback(func1)


# submit():提交异步任务执行
# result()：获取返回值
# shutdown():相当于close+join
# .add_done_callback(func1)：回调函数
# map(func,可迭代类型)