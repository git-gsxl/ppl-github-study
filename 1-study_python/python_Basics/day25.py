'''
一、接口类
'''
# # 1、接口类：统一一个支付的入口
# class A_pay:
#     def pay(self, money):
#         print('A钱包支付：%s元' % money)
#
# class B_pay:
#     def pay(self, money):
#         print('B钱包支付：%s元' % money)
#
# def pay(pay_ojb, money):
#     '''pay对象：统一支付入口'''
#     pay_ojb.pay(money)
#
# pay(A_pay(), 1000)
# pay(B_pay(), 100)



# # 2、假如新同学接手怎么写？所以要有接口类规范化
# # ①创建一个规范父类；②元类：metaclass=ABCMeta；③装饰某方法作为约束规范；
# from abc import abstractclassmethod, ABCMeta
# class Payment(metaclass=ABCMeta):   # 元类，规范的类。
#     @abstractclassmethod              # 引用装饰该方法，作为约束的方法。
#     def pay(self, money):pass
# class A_pay(Payment):
#     def pay(self, money):
#         print('A钱包支付：%s元' % money)
# class B_pay(Payment):
#     def pay(self, money):
#         print('B钱包支付：%s元' % money)
# class C_pay(Payment):
#     def shop_pay(self, money):
#         print('C钱包支付：%s元' % money)
# def pay(pay_ojb, money):
#     '''pay对象：统一支付入口'''
#     pay_ojb.pay(money)
#
# ret = C_pay()
#
# # 3、接口类多继承
# # A会唱歌、打篮球
# # B会唱歌、开车
# # C会唱歌、开车、打篮球
# from abc import abstractmethod,ABCMeta
# class All_abc(metaclass=ABCMeta):       # 规范
#     @abstractmethod
#     def sing(self):pass
#     @abstractmethod
#     def ball(self):pass
#     @abstractmethod
#     def drive(self):pass
#
# class Sing_ojb(metaclass=ABCMeta):      # 唱歌
#     @abstractmethod
#     def sing(self):pass
# class Ball_ojb(metaclass=ABCMeta):      # 打篮球
#     @abstractmethod
#     def ball(self):pass
# class Drive_ojb(metaclass=ABCMeta):     # 开车
#     @abstractmethod
#     def drive(self):pass
# class A(Sing_ojb, Ball_ojb):            # A会唱歌、打篮球
#     def sing(self):return Sing_ojb
#     def ball(self):return Ball_ojb
# ret = A()
# print(ret.ball())
# 接口类:接口隔离原则,是面向对象开发的思想的一种规范



'''
二、抽象类
一般情况下单继承实现的功能都是一样的，所以在父类中可以有一些简单的基础实现
多继承的情况 由于功能比较复杂，所以不容易抽象出相同的功能的具体实现写在父类中

'''

# 3、抽象类
# A会唱歌
# B会唱歌、开车
import abc
class All_ab(metaclass=abc.ABCMeta):  # All_ab：抽象类
    @abc.abstractmethod
    def sing(self):pass               # 定义抽象类规范的方法
    @abc.abstractmethod
    def drive(self):pass              # 定义抽象类规范的方法

class A(All_ab):                       # 子类继承父类，必须要定义父类(抽象类)规范的方法
    def sing(self):return '唱歌'
    def drive(self):return '开车'

ret = A()
print(ret)
print(ret.drive())
