'''
一、用于面向对象的内置函数
1、__str__
2、__repr__
3、__del__
4、__call__
'''

# 1、__str__：一旦被调用，就返回调用这个方法的对象的内存地址
# class A:
#     def __init__(self,name):self.name=name
#     def __str__(self):
#         return 'A is object '+self.name
# res = A('广深小龙')
# print(res)  # 打印一个对象，相当于调用了a.__str__
# print('%s：%s'%('A：',res))

# # 2、__repr__：
# class A:
#     def __init__(self,name):self.name=name
#     def __str__(self):
#         return 'A is object '+self.name
#     def __repr__(self):return str(self.__dict__)
# res = A('广深小龙')
# print(res)  # 打印一个对象，相当于调用了a.__str__
# print('%s：%s'%('A：',res))
# print(repr(res))

# # 调用了 __repr__，如果注释后调用父类的，返回的是对象
# print('%r'%res)

'''
repr(),只会找__repr__,如果没有找父类的,优先推荐repr。
如果没有__str__方法，会先找本类中的__repr__方法，再没有再找父类中的__str__。
print(obj)/'%s'%obj/str(obj)的时候，实际上是内部调用了obj.__str__方法，如果str方法有，那么他返回的必定是一个字符串。
'''
# 3、__len__：内置方法有很多,可以定制自己的内置方法
# class A:
#     def __init__(self,name):
#         self.name=[]
#     def __len__(self):
#         return len(self.name)+1
# res=A('小龙龙')
# res.name.append('广深小龙')
# res.name.append('广深小龙')
# print(len(res))

# 4、__del__:析构函数
# 删除一个对象之前，进行一些收尾工作
# class A:
#     def __del__(self):
#         print('执行我了')
# a=A()
# del a   # 既执行了del方法，也删除了变量a

# 5、__call__，调用能直接返回想要返回的功能，不用传方法名称
# class A:
#     def __init__(self,name):self.name=name
#     def __call__(self, *args, **kwargs):
#         print(self.__dict__)
# a=A('小龙龙')()        # 调用内部__call__方法

'''
二、
1、item系列
'''
# 1、list：增删查改
# class A:
#     def __init__(self,name):self.name=name
#     def __getitem__(self, item):
#         if hasattr(self,item):
#             return self.__dict__[item]
#     def __setitem__(self, key, value):
#         self.__dict__[key]=value
#     def __delitem__(self, key):del self.__dict__[key]
# a=A('广深小龙')
# print(a['name'])    # 查
# a['age']='22'       # 增
# print(a.age)
# a['age']='55'       # 改
# print(a['age'])
# del a.name           # 删
# del a['age']
# print(a.__dict__)


# # 2、__new__：构造方法
# class A:
#     def __init__(self):
#         print('init')
#     def __new__(cls, *args, **kwargs):  # 会先执行__new__方法
#         print('__new__')
#         return object.__new__(A, *args, **kwargs)
# a = A()
# # 会先执行cls，object.__new__,再执行self的__init__

# 3、设计模式：单列模式
'''
一个类只有一个实例,多个实例内存地址是一样。
当你第一次实例化这个类的时候 就创建一个实例化的对象。
当你之后再来实例化的时候 就用之前创建的对象。
'''
# class A:
#     __res=False
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __new__(cls, *args, **kwargs):  # 会先执行__new__方法
#         if cls.__res:
#             return cls.__res
#         cls.__res=object.__new__(A)
#         return cls.__res
# a = A('广深小龙','22')
# b = A('小龙女','18')
# print(a)
# print(b)
# print(a.name)
# print(b.name)
# a.addr='广深'
# print(b.addr)   # a追加，但b也有。单列模式


# 8、__eq__：比较两个值，也是可定制处理
class A:
    def __init__(self,name):
        self.name=name
    def __eq__(self, other):
        if self.name==other.name:
            print('%s 就是等于 %s'%(self.name,other.name))
            return True
        else:False
res1=A('gsxl')
res2=A('gsxl')
print(res1==res2)   # 正常是不相等，但__eq__可以定制处理

# 9、__hash__:定制化将哈希函数
# set 依赖对象的 hash eq
# class A:
#     def __init__(self,name,hname):
#         self.name=name
#         self.hname=hname
#     def __hash__(self):
#         return hash(self.name+self.hname)
#
# res1=A('gsxl','2233')
# res2=A('gsxl','2233')
# print(hash(res1))
# print(hash(res2))




