
# 一、迭代器,怎样查看呢？

# print(dir(list))                    # 查看某数据类型拥有的所有可调用方法
# print(dir([]))                      # [] == list
# print('__iter__' in dir(int))
# print('__iter__' in dir(bool))
# print('__iter__' in dir(list))
# print('__iter__' in dir(dict))
# print('__iter__' in dir(set))
# print('__iter__' in dir(tuple))
# print('__iter__' in dir(enumerate([])))
# print('__iter__' in dir(range(1)))

# # 只要含有 __iter__ 方法的都是可迭代的 --- 可迭代协议
# 发现只要是能被 for 循环的数据类型，就一定拥有 __iter__ 方法
# print([].__iter__())
# # 一个数据类型执行了 __iter__() 方法之后的返回值就是一个迭代器

# # 通过 next 就可以从迭代器中一个一个的取值
# ls = [1, 2, 3]
# res = ls.__iter__()          # 一个一个取值,不可逆
# print(res.__next__())       # 1
# print(res.__next__())       # 2
# print(res.__next__())       # 3
# print(res.__next__())       # list 只有 3个元素，所以这里会报错

# # 内部含有__next__和__iter__方法的就是迭代器
# print('__iter__' in dir([].__iter__()))
# print('__next__' in dir([].__iter__()))
#
#
# 实例
from collections import Iterable, Iterator
class A:
    ''' # 内部含有__next__和__iter__方法的就是迭代器,缺一都不行 '''
    # def __iter__(self):pass
    def __next__(self):pass

res = A()
print(isinstance(res, Iterator))      # 迭代器
print(isinstance(res, Iterable))      # 可迭代

# 可以被for循环的都是可迭代的
# 可迭代的内部都有__iter__方法
# 只要是迭代器 一定可迭代
# 可迭代的.__iter__()方法就可以得到一个迭代器
# 迭代器中的__next__()方法可以一个一个的获取值
#
#迭代器的好处：
    # 从容器类型中一个一个的取值，会把所有的值都取到。
    # 节省内存空间
        #迭代器并不会在内存中再占用一大块内存，
            # 而是随着循环 每次生成一个
            # 每次next每次给我一个
#只有 是可迭代对象的时候 才能用for，for循环本质就是迭代器
#当我们遇到一个新的变量，不确定能不能for循环的时候，就判断 __iter__ 它是否可迭代
#
#
# # 对比一下
# print(range(10))
# print(list(range(10)))

