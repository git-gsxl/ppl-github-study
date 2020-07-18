
# 一.内置函数
'''
内置函数官方标准库中说明有68个：https://docs.python.org/zh-cn/3.6/library/functions.html
在网上找到了一个汇总得不错的内置函数划分图：

'''

# 1.前面所学内容种我们用到过以下内置函数：
# print()
# input()
# type()
# len()
# int()
# str()
# list()
# tuple()
# set()
# open()
# dir()
# range()
# help()...等等~
# help(print)

# print(locals())  #返回本地作用域中的所有名字
# print(globals()) #返回全局作用域中的所有名字
# global 变量
# nonlocal 变量

#迭代器.__next__()
# next(迭代器)
# 迭代器 = iter(可迭代的)
# 迭代器 = 可迭代的.__iter__()

# range(10)
# range(1,11)
# print('__next__' in dir(range(1,11,2)))

# dir 查看一个变量拥有的方法
# print(dir([]))
# print(dir(1))

# help
# help(str)

# 变量
# print(callable(print))
# a = 1
# print(callable(a))
# print(callable(globals))
# def func():pass
# print(callable(func))

import time
# t = __import__('time')
# print(t.time())

# 某个方法属于某个数据类型的变量，就用.调用
# 如果某个方法不依赖于任何数据类型，就直接调用  —— 内置函数 和 自定义函数

# f = open('1.复习.py')
# print(f.writable())
# print(f.readable())

#id
#hash - 对于相同可hash数据的hash值在一次程序的执行过程中总是不变的
#     - 字典的寻址方式
# print(hash(12345))
# print(hash('hsgda不想你走，nklgkds'))
# print(hash(('1','aaa')))
# print(hash([]))

# ret = input('提示 ： ')
# print(ret)

# print('我们的祖国是花园',end='')  #指定输出的结束符
# print('我们的祖国是花园',end='')
# print(1,2,3,4,5,sep='|') #指定输出多个值之间的分隔符
# f = open('file','w')
# print('aaaa',file=f)
# f.close()

# import time
# for i in range(0,101,2):
#      time.sleep(0.1)
#      char_num = i//2
#      per_str = '\r%s%% : %s\n' % (i, '*' * char_num) \
#          if i == 100 else '\r%s%% : %s' % (i,'*'*char_num)
#      print(per_str,end='', flush=True)
#progress Bar

# exec('print(123)')
# eval('print(123)')
# print(eval('1+2+3+4'))   # 有返回值
# print(exec('1+2+3+4'))   #没有返回值
# exec和eval都可以执行 字符串类型的代码
# eval有返回值  —— 有结果的简单计算
# exec没有返回值   —— 简单流程控制
# eval只能用在你明确知道你要执行的代码是什么

# code = '''for i in range(10):
#     print(i*'*')
# '''
# exec(code)

# code1 = 'for i in range(0,10): print (i)'
# compile1 = compile(code1,'','exec')
# exec(compile1)

# code2 = '1 + 2 + 3 + 4'
# compile2 = compile(code2,'','eval')
# print(eval(compile2))

# code3 = 'name = input("please input your name:")'
# compile3 = compile(code3,'','single')
# exec(compile3) #执行时显示交互命令，提示输入
# print(name)
# name #执行后name变量有值
# "'pythoner'"


# 复数 —— complex
# 实数 ： 有理数
#         无理数
# 虚数 ：虚无缥缈的数
# 5 + 12j  === 复合的数 === 复数
# 6 + 15j

# 浮点数（有限循环小数，无限循环小数）  != 小数 ：有限循环小数，无限循环小数，无限不循环小数
# 浮点数
    #354.123 = 3.54123*10**2 = 35.4123 * 10
# f = 1.781326913750135970
# print(f)

# print(bin(10))
# print(oct(10))
# print(hex(10))

# print(abs(-5))
# print(abs(5))

# print(divmod(7,2))   # div出发 mod取余
# print(divmod(9,5))   # 除余

# print(round(3.14159,3))
# print(pow(2,3))   #pow幂运算  == 2**3
# print(pow(3,2))
# print(pow(2,3,3)) #幂运算之后再取余
# print(pow(3,2,1))

# ret = sum([1,2,3,4,5,6])
# print(ret)

# ret = sum([1,2,3,4,5,6,10],)
# print(ret)

# print(min([1,2,3,4]))
# print(min(1,2,3,4))
# print(min(1,2,3,-4))
# print(min(1,2,3,-4,key = abs))

# print(max([1,2,3,4]))
# print(max(1,2,3,4))
# print(max(1,2,3,-4))
# print(max(1,2,3,-4,key = abs))

# reversed()
# l = [1,2,3,4,5]
# l.reverse()
# print(l)
# l = [1,2,3,4,5]
# l2 = reversed(l)
# print(l2)
# 保留原列表，返回一个反向的迭代器

# l = (1,2,23,213,5612,342,43)
# sli = slice(1,5,2)
# print(l[sli])
# print(l[1:5:2])

# print(format('test', '<20'))
# print(format('test', '>40'))
# print(format('test', '^40'))

#bytes 转换成bytes类型
# 我拿到的是gbk编码的，我想转成utf-8编码
# print(bytes('你好',encoding='GBK'))     # unicode转换成GBK的bytes
# print(bytes('你好',encoding='utf-8'))   # unicode转换成utf-8的bytes

# 网络编程 只能传二进制
# 照片和视频也是以二进制存储
# html网页爬取到的也是编码
# b_array = bytearray('你好',encoding='utf-8')
# print(b_array)
# print(b_array[0])
# '\xe4\xbd\xa0\xe5\xa5\xbd'
# s1 = 'alexa'
# s2 = 'alexb'

# l = 'ahfjskjlyhtgeoahwkvnadlnv'
# l2 = l[:10]

# 切片 —— 字节类型  不占内存
# 字节 —— 字符串 占内存

# print(ord('好'))
# print(ord('1'))
# print(chr(97))

# print(ascii('好'))
# print(ascii('1'))
# name = 'egg'
# print('你好%r'%name)
# print(repr('1'))
# print(repr(1))


# 三、几个重要的内置函数

# print(all(['a','',123]))
# print(all(['a',123]))
# print(all([0,123]))

# print(any(['',True,0,[]]))

# l = [1,2,3,4,5]
# l2 = ['a','b','c','d']
# l3 = ('*','**',[1,2])
# d = {'k1':1,'k2':2}
# for i in zip(l,l2,l3,d):
#     print(i)

# def is_odd(x):
#     return x % 2 == 1
#
# def is_str(s):
#     return s and str(s).strip()
#
# ret = filter(is_odd, [1,  6, 7, 12, 17])
# ret = filter(is_str, [1, 'hello','','  ',None,[], 6, 7, 'world', 12, 17])
# print(ret)
# for i in ret:
#     print(i)
# [i for i in [1, 4, 6, 7, 9, 12, 17] if i % 2 == 1]

# from math import sqrt
# def func(num):
#     res = sqrt(num)
#     return res % 1 == 0
# ret = filter(func,range(1,101))
# for i in ret:
#     print(i)


# ret = map(abs,[1,-4,6,-8])
# print(ret)
# for i in ret:
#     print(i)


# filter 执行了filter之后的结果集合 <= 执行之前的个数
        #filter只管筛选，不会改变原来的值
# map 执行前后元素个数不变
      # 值可能发生改变

# l = [1,-4,6,5,-10]
# # l.sort(key = abs)   # 在原列表的基础上进行排序
# # print(l)
#
# print(sorted(l,key=abs,reverse=True))      # 生成了一个新列表 不改变原列表 占内存
# print(l)

# l = ['   ',[1,2],'hello world']
# new_l = sorted(l,key=len)
# print(new_l)









# 二、内置函数
list= [1, 2, 3, -4, 5, 6]

def func(no):
    return no>4

ret = map(abs, list)
print(ret)
for i in ret:
    print(i)





'''
匿名函数：为了解决一些功能很简单的需求而设计的一句话函数
'''
# 匿名函数：lambda,如下:
# res = lambda a:a*a
# print(res(2))
#
# # 上述的匿名函数，我们写个常规的函数来表示，既：
# def res(a):
#     return a*a
# print(res(2))

# min,max,map,filter,sorted 这五个可以和 lambda 组合，如：
# 将ret元组打印出来为：[{'a':'c','b':'d'}]
ret = zip((('a'),('b')),(('1'),('2')))
res = map(lambda tp:{tp[0]:tp[1]}, ret)
print(list(res))