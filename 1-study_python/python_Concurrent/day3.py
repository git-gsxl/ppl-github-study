'''
一、初识队列
队列：先进先出
'''
# 1、初识队列
import time
from multiprocessing import Queue
q=Queue(3)              # 设置3个,没设置即为不上限
q.put(1)
q.put(2)
q.put(3)
print(q.full())         # 查看队列是否满了
print(q.get())          # 取走队列的对象
print(q.get())          # 取走队列的对象
print(q.get())          # 取走队列的对象
print(q.empty())        # 判断队列是否为空
# # print(q.get_nowait())   # 如果为空，抛异常queue.Empty
# while 1:
#     try:q.get_nowait()
#     except:
#         print('队列为空！！！')
#         time.sleep(1)

# # 2、队列在进程中使用
# from multiprocessing import Process,Queue
# def func(q):
#     q.put('给我一个吻，可以不可以？')
# def give(q):
#     q.get()
# if __name__ == '__main__':
#     q=Queue()
#     p=Process(target=func,args=(q,))
#     p1=Process(target=give,args=(q,))
#     p.start()
#     p1.start()
#     print(q.get())

'''
生产者 进程
消费者 进程
为什么会出现生产者/消费者膨胀问题？
    比如生产者在生产，生产的货物积囤有限，那么可以一边卖给消费者，一边生产。
    但是这样子会导致任意一方可能出现 供过于求或供不应求，所以要平衡。
'''
# 1、Queue，第一种解决：生产者/消费者膨胀问题。
# import time
# import random
# from multiprocessing import Process,Queue
# def consumer(q,name):
#     while 1:
#         mask = q.get()
#         if mask is None:
#             print('%s口罩空'%name)
#             break
#         print('%s使用了 %s' % (name,mask))
#         time.sleep(random.randint(1,3))
#
# def producer(name,mask,q):
#     for i in range(1,5):
#         time.sleep(random.randint(1,3))
#         f = '%s生产了%s %s'%(name,mask,i)
#         print(f)
#         q.put(f)
#
# if __name__  == '__main__':
#     q = Queue()
#     p1 = Process(target=producer,args=('大厂','N95口罩',q))
#     p2 = Process(target=producer, args=('小厂','N90口罩', q))
#     c1 = Process(target=consumer, args=(q,'A企业'))
#     c2 = Process(target=consumer, args=(q,'B企业'))
#     p1.start()
#     p2.start()
#     c1.start()
#     c2.start()
#     p1.join()
#     p2.join()
#     q.put(None)
#     q.put(None)

# # 2、JoinableQueue，第二种解决：生产者/消费者膨胀问题。

'''
基本思路：
①消费者 中把所有的任务执行完；
②生产者 中的p.join()感知到消费者任务执行完就停止阻塞；
③生产者停止堵塞后意味着 生产者 的所有进程结束；
    主进程中的p.join()结束
    主进程中代码结束
守护进程(消费者的进程)结束
'''
import time
import random
from multiprocessing import Process,JoinableQueue
def consumer(q,name):
    while 1:
        mask = q.get()
        if mask is None:
            print('%s口罩空'%name)
            break
        print('%s使用了 %s' % (name,mask))
        time.sleep(random.randint(1,3))
        q.task_done()                      # 类似监控生产的数量，计数器每次-1

def producer(name,mask,q):
    for i in range(1,5):
        time.sleep(random.randint(1,3))
        m = '%s生产了%s %s'%(name,mask,i)
        print(m)
        q.put(m)
    q.join()                             # 堵塞，等到队列中的所有数据全部都被消费者执行完

if __name__  == '__main__':
    q = JoinableQueue()
    p1 = Process(target=producer,args=('大厂','N95口罩',q))
    p2 = Process(target=producer, args=('小厂','N90口罩', q))
    c1 = Process(target=consumer, args=(q,'A企业'))
    c2 = Process(target=consumer, args=(q,'B企业'))
    p1.start()
    p2.start()
    c1.daemon=True      # 设为守护进程，既是主进程的代码执行完后子进程自动结束
    c2.daemon=True      # 设为守护进程，既是主进程的代码执行完后子进程自动结束
    c1.start()
    c2.start()
    p1.join()
    p2.join()
