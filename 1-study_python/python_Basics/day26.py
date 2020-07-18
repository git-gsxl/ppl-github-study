'''
一、多态
1.Python天生是多态。
'''
# 1、证明Python天生是多态：
# 不管在传参的时候什么类型都可以什么对象ojbect、int/str/dict等等,对类型不敏感。
# 不像其它语言，接收参数要定义它的数据类型，入参类型不一致就会报错。
# def func(a):
#     return a
# print(func('asdasdasdasd'))
# print(func(123))
# print(func(('传什么','都可以')))

# 2、鸭子类型
# list 与 tuple 都有着相似的方法，并没有产生父类子类关系,称为：鸭子类型
# l = list
# l.index()
# l.count()
#
# t = tuple
# t.index()
# t.count()

# 有着相似的方法，但它不崇尚根据继承所得来的相似；
# 强类型语言，只能用多态定义一个类型；
# 鸭子类型优点 ： 松耦合 每个相似的类之间都没有影响；
# 鸭子类型缺点 ： 太随意,没有硬性约束只能看自己了；

'''
接口类和抽象类 在python当中的应用点并不是非常必要；
Python中不崇尚像其它语言那样去继承做规范，就比如list与tuple都有着相似的方法都没有用继承；
所以Python是崇尚鸭子类型，所以不崇尚继承做规范；
'''


'''
二、封装
封装：面向对象的思想本身就是一种封装，让特有对象能够调用类中的方法；
也就是面向对象的三大特性之一，属性与方法都看不到实际的对象数据。
'''

# 1、登录账号例子：
# 并不知道实际的登录的是哪个账号，所以我们面向对象封装了一个登录的类
# class Login:
#     def __init__(self, name, pwd):
#         self.name = name
#         self.pwd = pwd
#     def login(self):
#         return self.name+' 登录成功!'
#
# res_name = input('请输入您的账号')
# res_pwd = input('请输入您的密码')
# res_lg = Login(res_name, res_pwd)
# login = res_lg.login()
# print(login)

# 2、私有动态属性、私有方法、私有静态属性
class Login:
    __key = '666'                       # 私有静态属性
    def __init__(self, name, pwd):
        self.name = name
        self.__pwd = pwd                 # 私有动态属性

    def name(self):
        return self.name

    # 静态发方法：__get_pwd
    def __get_pwd(self):return self.__key+self.__pwd

    def login(self):                  # 类内部调用：self.__get_pwd()
        return self.name+' 登录成功! '+self.__get_pwd()

res_name = input('请输入您的账号：')
res_pwd = input('请输入您的密码：')
res_lg = Login(res_name, res_pwd)
print(res_lg.login())
print(res_lg.__dict__)                   # 但是也能看到它所有动态属性
print(res_lg._Login__pwd)                # 但是也能看到它的属性
# print(res_lg._get_pwd())               # __get_pwd是私有方法类外部调不到

'''
所有的私有都是在类的变量的左边加上双下划綫
    对象的私有属性
    类中的私有方法
    类中的静态私有属性
所有的私有的 都不能在类的外部使用，虽然可以调
'''
