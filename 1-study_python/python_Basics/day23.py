# # 1、组合实例
# class Ojb_1:
#     '''假设Ojb_1是一个装备库，func_name是其中一件装备，装备后加1000战力。'''
#     def __init__(self, agg):
#         self.agg = agg
#
#     def func_name(self):
#         self.agg += 1000                # 在本身的战力上+1000
#         return self.agg                 # 返回最终战力
#
# class Ojb_2:
#     '''假设Ojb_2是一个角色类，每个角色都有名称等信息'''
#     def __init__(self, name, agg):
#         self.name = name                # 角色名称
#         self.agg = agg                  # 本身的战力
#         self.Ojb_1 = Ojb_1(self.agg)    # 将该人物原来的战力传到装备库
#
#
# if __name__ == '__main__':
#     '''假设广深小龙原来战力=500'''
#     r1 = Ojb_2('广深小龙', 500)
#     res = r1.Ojb_1.func_name()
#     print(res)
#

# 2、实例2
# 我是一个人，叫广深小龙，我学的是Python，我的生日是1999年6月6日，工作是IT，地址是广深
# class Work:
#     '''工作是IT，用的是Python，所以我学习Python'''
#     def work_lg(self, work='IT', lg='Python'):
#         return '工作是：%s,用的是：%s' % (work, lg)
#
# class Birth:
#     '''出生日期：birth，地址：address'''
#     def birth_add(self, birth, address):
#         return '出生日期：%s,地址：%s' % (birth, address)
#
# class Race:
#     def __init__(self, name):
#         self.name = name
#         self.Work = Work()
#         self.Birth = Birth()
#
# if __name__ == '__main__':
#     r = Race('广深小龙')
#     print(r.Work.work_lg())
#     print(r.Birth.birth_add('1996.6.6', '广深'))



'''
二、初识继承
继承是一种创建新类的方式，在python中，新建的类可以继承一个或多个父类，父类又可称为基类或超类，新建的类称为派生类或子类，先有父类才会有子类
'''

# # 1、初识继承
# class A:pass
#
# class B:pass
#
# # Python语言中一个类可继承多个父类
# class AB_son(A, B):pass     # 继承了A、B类
# print(AB_son.__bases__)       # 查看父类
# print(A.__bases__)            # 没有继承父类，默认是类的祖宗：object


# 2、继承用法实例
'''
父类中没有的属性 在子类中出现 叫做派生属性
父类中没有的方法 在子类中出现 叫做派生方法
只要是子类的对象调用，子类中有的名字 一定用子类的，子类中没有才找父类的，如果父类也没有报错
如果父类 子类都有 用子类的
    如果还想用父类的，单独调用父类的:
          父类名.方法名 需要自己传self参数
          super().方法名 不需要自己传self
正常的代码中 单继承 === 减少了代码的重复
继承表达的是一种 子类是父类的关系
'''
class Work:
    '''工作是IT，用的是Python，所以我学习Python'''
    def work_lg(self, work='IT', lg='Python'):
        return '工作是：%s,用的是：%s' % (work, lg)


class Race(Work):                       # 继承了 Work 类
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    r = Race('广深小龙').work_lg()      # 子类调用了父类的方法
    print(r)

