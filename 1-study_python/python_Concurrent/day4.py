'''
管道:Pipe，作用是可使两个进程之间进行通信。
'''
# 1、初识管道,可以互相通信。
from multiprocessing import Pipe
conn1, conn2 = Pipe()
conn1.send('123')
print(conn2.recv())
conn2.send('321')
print(conn1.recv())

# 2、管道实现：生产者/消费者模型
# from multiprocessing import Pipe,Process,Lock
# import time,random
# def consumer(con,pro,name,lock):
#     pro.close()
#     while 1:
#         try:
#             lock.acquire()
#             m=con.recv()
#             print('%s使用了 %s' % (name,m))
#             time.sleep(random.random())
#             lock.release()
#         except EOFError:
#             con.close()
#             break
# def producer(con,pro,name,mask):
#     con.close()
#     for i in range(1,11):
#         time.sleep(random.random())
#         m='%s生产了%s %s'%(name,mask,i)
#         print(m)
#         pro.send(m)
#     pro.close()
# if __name__ == '__main__':
#     lock=Lock()
#     con,pro=Pipe()
#     p=Process(target=producer,args=(con,pro,'大厂','N95 '))
#     p.start()
#     c=Process(target=consumer,args=(con,pro,'A企业',lock))
#     c.start()
#     c1=Process(target=consumer,args=(con,pro,'B企业',lock))
#     c1.start()
#     con.close()
#     pro.close()

# 3、Manager,数据共享不安全的，但会进程之间抢占资源。
# 但可以加锁约束解决
# from multiprocessing import Manager,Process,Lock
# def func(dic,lock):
#     lock.acquire()
#     dic['count']+=1
#     lock.release()
#
# if __name__ == '__main__':
#     lock=Lock()
#     m=Manager()
#     dic=m.dict({'count':0})
#     p_lst=[]
#     for i in range(50):
#         p=Process(target=func,args=(dic,lock))
#         p.start()
#         p_lst.append(p)
#     for i in p_lst:i.join()
#     print('主进程：%s'%dic)