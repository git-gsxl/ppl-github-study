# 1.装饰器进阶
# 1.列子1,带参数的装饰器
import time
flag = False         # True 就走装饰器 if ，否则不走装饰器

def timmer(f):
    def inner(*args, **kwargs):
        ''' 多判断一个参数：flag，让其运行或不运行装饰函数 '''
        if flag:
            start = time.time()
            ret = f(*args, **kwargs)
            end = time.time()
            print('已等待：', end-start)
            return ret
        else:
            print('没有等待')
            ret = f(*args, **kwargs)
            return ret
    return inner

@ timmer
def gs(a):
    time.sleep(1)
    return '返回值：', a

# print(gs(flag))

# 2、列子2,带参数的装饰器
import time
flag1 = False
def timmer_out(fg):
    def timmer(f):
        def inner(*args, **kwargs):
            if fg:
                start = time.time()
                ret = f(*args, **kwargs)
                end = time.time()
                print('已等待：', end-start)
                return ret
            else:
                print('没有等待')
                ret = f(*args, **kwargs)
                return ret
        return inner
    return timmer

@ timmer_out(flag1)
def gs1(a):
    time.sleep(1)
    return '返回值：', a

# print(gs1(flag1))


# 3、调用多个装饰
# 俄罗斯套娃，上面到下面前置执行一次，然后下面到上面的后置执行一此
def wrapper1(func):
    def inner1(*args, **kwargs):
        print('是：wrapper1--前')
        res = func(*args, **kwargs)
        print('是：wrapper1--后')
        return res
    return inner1

def wrapper2(func):
    def inner2(*args, **kwargs):
        print('是：wrapper2--前')
        res = func(*args, **kwargs)
        print('是：wrapper2--后')
        return res
    return inner2

@ wrapper1
@ wrapper2
def f():
    print('F')
    return '拉回给你'

print(f())