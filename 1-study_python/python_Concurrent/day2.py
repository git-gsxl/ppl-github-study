'''
一、多个进程中同一时间，某一个程序同时被N个进程执行；
上一篇说锁的时候是单个，现在说的是N个。
'''
# # 1、信号量-Semaphore:比如一个程序最多2个进入
# from multiprocessing import Process,Semaphore
# import time
# def func(i,sem):
#     sem.acquire()
#     print('用户 %s 进入了'%i)
#     time.sleep(5)
#     print('用户 %s 退出了'%i)
#     sem.release()
# if __name__ == '__main__':
#     sem=Semaphore(2)        # 设置能执行N个同时执行
#     for i in range(1,5):
#         p=Process(target=func,args=(i,sem))
#         p.start()


# 2、事件：通过一个信号控制多个进程，同时执行或阻塞
# 一个信号可以是所有的进程都进入阻塞状态
# 也可以控制所有的进程解除阻塞，创建时默认为阻塞状态
# from multiprocessing import Event
# e=Event()
# e.is_set()          # 创建一个事件，默认为阻塞状态:False
# print('阻塞前~')
# e.set()             # 将事件堵塞状态设为：True
# e.wait()            # 如果is_set()的值为False，那么进行堵塞，否则不堵塞
# e.clear()           # 将事件的堵塞状态清空，即为默认状态:False
# print('阻塞后~~~')

'''
总结：
    is_set()：创建一个事件
    set()、e.clear()：修改事件堵塞的状态为Ture或False
    is_set：查看事件堵塞状态
    wait()：根据事件状态来判断是否进行堵塞，Ture：不堵塞，False：堵塞
'''
from multiprocessing import Process,Event
import time
def func(e):
    while 1:
        if e.is_set():
            e.clear()
            print('红灯停~~')
        else:
            e.set()
            print('绿灯亮起~')
        time.sleep(3)
def car(i,e):
    if not e.is_set():
        print('%s 等红灯中==' % i)
        e.wait()
    print('%s 通行中-->' % i)

if __name__ == '__main__':
    e=Event()
    p=Process(target=func,args=(e,))
    p.start()
    for i in range(1,11):
        p1=Process(target=car,args=(i,e))
        p1.start()
        time.sleep(0.5)


