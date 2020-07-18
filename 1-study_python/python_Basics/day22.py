'''
一、面向对象：比如人类，假设人类分为三种人：黄种人、黑种人、白种人。
过程：
    类名 首先 会创造出一个对象，创建了一个self变量
    调用init方法，类名括号里的参数会被这里接收
    执行init方法,返回self
对象能做的事：
    查看属性
    调用方法
    __dict__ 对于对象的增删改查操作都可以通过字典的语法进行
类名能做的事：
    实例化
    调用方法 : 只不过要自己传递self参数
    调用类中的属性,也就是调用静态属性
    __dict__ 对于类中的名字只能看 不能操作

'''

# # 1、面向过程：（记流水账）
# name = '广深小龙'
# type_race = '黄种人'
# age = 22
# work = 'IT'
# print('我名字叫：%s，是%s,年龄：%s，工作是%s' % (name, type, age, work))

# 2、面向对象：
# def race(name, type_race, age, work):
#     '''
#     :param name: 您的名字
#     :param type_race: 三种类型：黄种人、黑种人、白种人
#     :param age: 您的年龄
#     :param work: 您的工作
#     :return:
#     '''
#     type = type_race
#     name = name
#     age = age
#     work = work
#     return '我名字叫：%s，是%s,年龄：%s，工作是%s' % (name, type, age, work)
#
# print(race('广深小龙', '黄种人', '22', 'IT'))
# print(race('美国黑寡妇', '黑种人', '70', 'PM'))
# print(race('小欧欧', '白种人', '18', 'IT'))

# # 3、创建一个叫 Ojb 类
# class Ojb:
#     '''
#     这是一个类，类下面有 func 方法，也就是类的一个函数。
#     '''
#     def func(self):
#         pass



class Ojb:
    def __init__(self, name, type_race, age, work):     # 初始化
        '''
        :param name: 您的名字
        :param type_race: 三种类型：黄种人、黑种人、白种人
        :param age: 您的年龄
        :param work: 您的工作
        :return:
        '''
        '''属性值'''
        self.name = name
        self.type = type_race
        self.age = age
        self.work = work

    def race(self):
        return '我名字叫：%s，是%s,年龄：%s，工作是%s' % (self.name, self.type, self.age, self.work)

    def func(self, num):
        return '家中有%s口人！' % num

    def ar(self):
        return 'ar方法被调用！'

if __name__ == '__main__':
    res = Ojb('广深小龙', '黄种人', '22', 'IT')    # 实例化
    print(res.__dict__['name'])
    # res.__dict__['name'] = '傻小子'                # 修改了对象的变量，和操作字典一样
    res.name = '傻小子'                             # 修改了对象的变量，和操作字典一样
    print(res.age)
    race = res.race()
    res_num = res.func(6)                            # 调用方法
    res_num1 = Ojb.ar(res)                           # 调用方法
    print(race)
    print(res_num)
    print(res_num1)



