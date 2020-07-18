'''
一、反射,四个方法
hasattr()
getattr()
setattr()
delattr()
'''
# # 1、isinstance、issubclass
# class A:pass
# class B(A):pass
# a = A()
# print(isinstance(a,A))  # 判断实例化a是否是A的类，返回bool
# print(issubclass(B,A))  # 判断子类B是否是A中继承过来，返回bool


# # 1、反射对象的属性：
# class A:
#     dic={
#         'a':1,
#         'b':2,
#         'c':''}
#     def __init__(self,name):self.name=name
# res=A('广深小龙')
# r=getattr(res,'name')       # 查看属性:(实例化对象，属性变量名)
# print(r)

# # 2、反射对象的方法：
# class A:
#     dic={
#         'a':1,
#         'b':2,
#         'c':''}
#     @staticmethod
#     def func():
#         return 'qasdasdasd'
# r1 = getattr(A,'func')
# print(r1)           # 拿到的是func方法
# print(r1())         # 可以调用到函数


# # 3、反射类的属性：
# class A:
#     dic = {
#         'a':'ff',
#         'b':'func'}
# print(getattr(A,'dic'))

# # 4、反射类的方法：
# class A:
#     dic = {
#         'a':'ff',
#         'b':'func'}
#     @staticmethod
#     def ff():return '调用了ff方法'
#     @classmethod
#     def func(cls):return '调用了func方法'
#     def hub(self):return '调用了hub方法'
# print(getattr(A,'ff')())
# print(getattr(A(),'hub')()) # 注意：A()是因为hub是普通类的方法需要传self
#
# if hasattr(A(),'hub'):  # hasattr 判断是否存在，返回bool
#     print(getattr(A,'func')())

# # 5、反射模块的属性与方法
# # 内置函数、自己定义的函数都可以使用
# import test
# getattr(test,'r')               # 反射模块的属性
# func=getattr(test,'func')      # 反射模块的方法
# print(func())

# 6、反射自己模块中的变量与方法：
# name = '广深小龙'
# def func():
#     return 'func函数'
#
# import sys
# print(getattr(sys.modules['__main__'],'name'))     # 反射自己模块的变量
# print(getattr(sys.modules['__main__'],'func')())   # 反射自己模块的函数

'''
# 可能给其他模块调用就将'__main__'改为变量：__name__
import sys
def name():return '小龙女'
ret=print(getattr(sys.modules[__name__],'name')())# 反射自己模块的函数

import test
getattr(test,'ret')     # 反射自己模块的函数
'''
# import test
# getattr(test,'ret')     # 反射自己模块的函数


# # 7、反射带参数、反射模块的类函数
# class A:
#     @staticmethod
#     def func(name,age):return name+age
# print(getattr(A,'func')('广深小龙','23'))   # 反射带参数
# import test
# if hasattr(test,'A'):                        # 判断是否反射到其他模块类：A，返回bool
#     res = getattr(test,'A')()                # 反射其他模块的类：A
#     print(res.f())
# else:print('没有反射到对象！')

# 8、新增静态属性：setattr
class A:pass
a = A()
setattr(a,'name','广深小龙')
setattr(A,'name','小龙')
print(a.name)
print(A.name)

# delattr 删除静态属性
delattr(a,'name')      # 删除实例化的a
print(a.name)           # 找的是类的name，因为原来的 广深小龙 被删除了



# # 反射示例：
# class A:
#     dic = {
#         'a':'ff',
#         'b':'func'}
#     @staticmethod
#     def ff():return '调用了ff方法'
#     @classmethod
#     def func(cls):return '调用了func方法'
#
# for i in A.dic:
#     key = i
#     func = getattr(A,A.dic[key])
#     if hasattr(A,A.dic[key]):
#         res = getattr(A, A.dic[key])
#         print(res())
#     else:print('没有这个函数！')

'''
普通方法：self
静态方法：无
类方法：cls
属性方法：property装饰器
'''