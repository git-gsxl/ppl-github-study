'''
一、封装进阶
'''
# # 1、私有方法属性的约束，newName 只能是字符串且非纯字符串的全数字
# class Login:
#     def __init__(self, name, pwd):
#         self.__name = name
#         self.__pwd = pwd
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, newName):
#         '''约束属性：newName，字符串且非纯字符串的数字'''
#         if type(newName) is str and newName.isdigit() == False:
#             self.__name = newName
#         else:print('输入的类型有误，请重新输入！')
#
# if __name__ == '__main__':
#     r = Login('广深小龙', 123)
#     print(r.get_name())
#     r.set_name('1')
#     print(r.get_name())


# # 2、父类的私有属性也不能被子类调用
# class A:
#     __pwd = 666
#
# class B(A):
#     print(A.__pwd)
# '''
# 1.隐藏起一个属性 不想让类的外部调用
# 2.我想保护这个属性，不想让属性随意被改变
# 3.我想保护这个属性，不被子类继承
# '''
# # 没实例化运行都直接报错

'''
二、property内置装饰器函数
只在面向对象中使用，对属性
'''
# # 1、property：装饰该方法,方法伪装成为一个属性，少写了一个括号
# class A:
#     def __init__(self, num):
#         self.__num = num
#     @property               # 装饰该方法,方法伪装成为一个属性
#     def square(self):
#         return self.__num*self.__num
#
# r = A(-2)
# print(r.square)            # 实例化调用方法就不用加括号：r.square，方便将它传入下一个


# 实例2：gmi
'''
偏瘦10.≤18.4
正常18.5≤23.9
过重24.0≤27.9
肥胖28.0≤32.0

# class Person:
#     def __init__(self, weight, high):
#         self.high = high
#         self.weight = weight
#     @property
#     def bmi(self):
#         return self.weight / self.high**2
# r = Person(55, 1.70)
# print(r.bmi)
'''

# 2、setter：对对象的修改，两个函数名参数要一样，@property，@函数.setter
# class A:
#     def __init__(self,name):
#         self.__name = name
#     @property                    # 装饰该方法
#     def f_name(self):
#         return '非主流-'+self.__name
#     @f_name.setter
#     def f_name(self, newName):   # 只能传一个值
#         self.__name = newName
#
# r = A('广深小龙')
# print(r.f_name)
# r.f_name = '小龙女'
# print(r.f_name)

# 3、商品折扣
# class Goods:
#     discount = 0.5
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price
#     @property
#     def prices(self):
#         return self.__price*self.discount
# r = Goods('雪梨', 5)
# print(r.prices)

'''
属性可以查看、修改、删除
'''
# 3、deleter:property装饰器函数，属性删除
# class A:
#     def __init__(self, name):
#         self.__name = name
#     @property
#     def name(self):
#         return self.__name
#     @name.deleter
#     def name(self):
#         del self.name
#     @name.setter
#     def name(self, Newname):
#         self.__name = Newname
#
# r = A('广深小龙')
# del r.name          # 删除会报错的
# r.name = '小龙龙'
# print(r.name)

'''
classmethod：类方法
staticmethod:静态方法
都是类能直接调用，不需要实例化
'''

# 1、classmethod：类方法，cls是默认参数
# 只涉及静态属性的时候，就应使用这个classmethod装饰该方法
class Goods:
    discount = 0.5
    def __init__(self, name, price):
        self.name = name
        self.__price = price
    @property
    def prices(self):
        return self.__price*self.discount

    @classmethod    # 装饰后不需实例化，直接能操作
    def update(cls, Newdiscount):
        cls.discount = Newdiscount

r = Goods.update(2)     # classmethod装饰后不用传对象
res = Goods('雪梨', 6)
print(res.prices)

# # 1、staticmethod：静态方法
# class Login:
#     def __init__(self, usr, pwd):
#         self.usr = usr
#         self.pwd = pwd
#     def login(self):
#         return '登录成功！！！'
#
#     @staticmethod
#     def usr_pwd():   # 静态方法，没有默认参数，像个函数一样
#         usr = input('请输入您的账号：')
#         pwd = input('请输入您的密码：')
#         return Login(usr, pwd)
# r = Login.usr_pwd()
# print(r.login())