'''
1.模块级：全局的，整个模块开只运行一次，优先于测试用例。
2.类级别：定义在类里面，只针对此类生效。类似unittest的cls装饰器
3.函数级：只对函数生效，类下面的函数不生效。
4.方法级：定义在类里面，每个用例都执行一次。
'''

# def setup_module():
#     print('\n整个模块 前 只运行一次')
#
# def teardown_module():
#     print('\n整个模块 后 只运行一次')
#
# def setup_function():
#     print('\n不在类中的函数，每个用例 前 只运行一次')
#
# def teardown_function():
#     print('\n不在类中的函数，每个用例 后 只运行一次')
#
# def test_ab():
#     b = 2
#     assert b < 3
#
# def test_aba():
#     b = 2
#     assert b < 3

class Test_api():

    def setup_class(self):
        print('\n此类用例 前 只执行一次')
    def teardown_class(self):
        print('\n此类用例 后 只执行一次')

    def setup_method(self):
        print('\n此类每个用例 前 都执行一次')

    def teardown_method(self):
        print('\n此类每个用例 后 都执行一次')

    def test_aa(self):
        a = 1
        print('\n我是用例：a')       # pytest -s 显示打印内容
        assert a > 0

    def test_b(self):
        b = 2
        print('\n我是用例：b')       # pytest -s 显示打印内容
        assert b < 3

