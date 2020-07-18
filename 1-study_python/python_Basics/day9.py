
'''
开放封闭原则：
1.开放：对扩展是开放的
2.关闭：对修改是封闭的
维护代码稳定性才出现的

装饰器的意义：
1.不想修改函数的调用方式 但是还想在原来的函数前后添加功能；
2.timmer就是一个装饰器函数，只是对一个函数 有一些装饰作用
'''

# 1.装饰器初成
# import time
# def func():
#     time.sleep(1)
#     print('我在等待一秒钟')
#
# def timmer(f):                  # 装饰器函数
#     def inner():
#
#         start = time.time()
#
#         f()                      # 被装饰函数
#         end = time.time()
#
#         print(end-start)
#
#     return inner                # 别加 () 调用函数了，应传内部函数名字
#
# ff = timmer(func)
# ff()

# 2.装饰器使用
# import time
# def timmer(f):
#     def inner():
#         start = time.time()
#         ret = f()
#         end = time.time()
#         return end-start, ret
#     return inner
#
# @timmer         # @装饰器函数名
# def func():    # 被装饰的函数
#     time.sleep(1)
#     return '我在等待一秒钟'
# print(func())


# 3.万能参数装饰器
import time
def timmer(f):
    def inner(*args, **kwargs):     # *args, **kwargs 万能接收参数
        start = time.time()
        ret = f(*args, **kwargs)     # *args, **kwargs 万能传入参数
        end = time.time()
        print(end-start)
        return ret
    return inner

@timmer
def func(a, b):
    print(a, b)
    time.sleep(1)
    return '我在等待一秒钟'

@timmer
def func1(a):
    print(a)
    time.sleep(1)
    return '我在等待一秒钟'

print(func(1, 2))
print(func1(1))


# # 4.装饰器固定模式
# def wrapper(f):                     # 装饰器函数：wrapper   被装饰函数：f
#     def inner(*args, **kwargs):     # 被装饰函数：inner == f
#         # 在被装饰函数之 前 要做的功能
#         ret = f(*args, **kwargs)
#         # 在被装饰函数之 后 要做的功能
#         return ret
#     return inner
#
# @wrapper        # @装饰器函数，实际相当于：wrapper(fon)
# def fon(a):
#     print('打酱油')
#     return a
#
# r = fon('固定模式就是这样')          # 实际相当于调用：inner
# print(r)

from functools import wraps
def wrapper(func):  #func = holiday
    @wraps(func)
    def inner(*args,**kwargs):
        print('在被装饰的函数执行之前做的事')
        ret = func(*args,**kwargs)
        print('在被装饰的函数执行之后做的事')
        return ret
    return inner

@wrapper   #holiday = wrapper(holiday)
def holiday(day):
    '''这是一个放假通知'''
    print('全体放假%s天'%day)
    return '好开心'

print(holiday.__name__)
print(holiday.__doc__)
ret = holiday(3)   #inner
print(ret)


# def wahaha():
#     '''
#     一个打印娃哈哈的函数
#     :return:
#     '''
#     print('娃哈哈')

# print(wahaha.__name__) #查看字符串格式的函数名
# print(wahaha.__doc__)  #document
