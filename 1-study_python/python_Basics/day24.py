'''
继承进阶：
父类中没有的属性 在子类中出现 叫做派生属性
父类中没有的方法 在子类中出现 叫做派生方法
'''

# # 1、派生属性：父类中没有的属性，在子类中出现。
# # 2、派生方法：父类中没有的方法，在子类中出现
# class Work:
#     '''工作是IT，用的是Python，所以我学习Python'''
#     def __init__(self, work='IT', lg='Python'):
#         self.work = work
#         self.lg = lg
#
#     def work_lg(self):
#         return '工作是：%s,用的是：%s' % (self.work, self.lg)
#
# class Race(Work):                          # 继承了 Work 类
#     def __init__(self, work, lg, name):
#         Work.__init__(self, work, lg)
#         self.name = name                    # 派生属性: self.name = name
#
#     def func(self):
#         print('我是派生方法！！！')         # 派生方法：func
#
# if __name__ == '__main__':
#     r = Race('广深小龙', 'IT', 'Python')  # 父类中没有的属性,在子类中出现,叫做派生属性
#     r.func()
#     print(r.work_lg())




# # 2、继承类的方法，可以在父类的方法上做扩展
# class Work:
#     '''工作是IT，用的是Python，所以我学习Python'''
#     def __init__(self, work='IT', lg='Python'):
#         self.work = work
#         self.lg = lg
#
#     def work_lg(self):
#         print('执行了：Work.work_lg')
#         return '工作是：%s,用的是：%s ' % (self.work, self.lg)
#
# class Race(Work):                                    # 继承了 Work 类
#     def __init__(self, work, lg, name):
#         Work.__init__(self, work, lg)
#         self.name = name                              # 派生属性: self.name = name
#
#     def work_lg(self):
#         re1 = '继承类的方法后，先做的事情！！！'    # 继承类方法后，先做的事情！！！
#         print(re1)
#         ret = Work.work_lg(self)
#         re2 = '继承类的方法后，后做的事情！！！'    # 继承类方法后，后做的事情！！！
#         print(re2)
#         return ret
#
# if __name__ == '__main__':
#     r = Race(name='广深小龙', work='IT', lg='Python').work_lg()



# # 3、super():①类内部使用可以找到父类；②还可以在外部调用时使用
# class Work:
#     '''工作是IT，用的是Python，所以我学习Python'''
#     def __init__(self, work='IT', lg='Python'):
#         self.work = work
#         self.lg = lg
#     def work_lg(self):
#         return '工作是：%s,用的是：%s' % (self.work, self.lg)
#
# class Race(Work):
#     def __init__(self, work, lg, name):
#         super().__init__(work, lg)     # super()：不需要传self，相当于传了super(self, name)
#         self.name = name
#
#     def work_lg(self):print('Race.work_lg')
#
#
# if __name__ == '__main__':
#     r = Race(name='广深小龙', work='IT', lg='Python')
#     r.work_lg()
#     r_super = super(Race, r).work_lg()    # 传一个类：Race，再传一个对象：r
#     print(r_super)



'''
多继承
'''
# # 1、多继承,同方法被调用顺序:按照继承类的顺序，如A、B、C，则先A再到B再到C
# class A:
#     # def func(self):print('A')
#     pass
# class B:
#     def func(self):print('B')
# class C:
#     def func(self):print('C')
# class D(A,B,C):
#     # def func(self):print('D')
#     pass
#
# d = D().func()

# class F:
#     def func(self):print('F')
#     pass
#
# class E(F):
#     def func(self):print('E')
#     pass

# # 2、Python3 广度优先，从左往右就近原则。
class E():
    def func(self):print('E')
    pass

class D():
    def func(self):print('D')
    pass

class B(D):
    # def func(self):print('B')
    pass

class C(E):
    def func(self):print('C')
    pass

class A(B,C):
    # def func(self):print('A')
    pass

d = A().func()





# # 2、Python3 广度优先，从左往右就近原则。
'''扩展：
Python2.7
新式类 继承object类的才是新式类 广度优先
经典类 如果你直接创建一个类在2.7中就是经典类 深度优先

单继承 ： 子类有的用子类 子类没有用父类
多继承中，我们子类的对象调用一个方法，默认是就近原则，找的顺序是什么？
经典类中 深度优先
新式类中 广度优先
python2.7 新式类和经典类共存，新式类要继承object
python3   只有新式类，默认继承object
经典类和新式类还有一个区别  mro方法只在新式类中存在
super 只在python3中存在
super的本质 ：不是单纯找父类 而是根据调用者的节点位置的广度优先顺序来的
'''

# class F():
#     def func(self):print('F')
#     pass
# class E(F):
#     def func(self):print('E')
#     pass
#
# class D(F):
#     def func(self):print('D')
#     pass
#
# class B(D):
#     # def func(self):print('B')
#     pass
#
# class C(E):
#     def func(self):print('C')
#     pass
#
# class A(B,C):
#     # def func(self):print('A')
#     pass
#
# d = A().func()
# print(A.mro())

