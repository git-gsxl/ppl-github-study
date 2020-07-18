from unittest import TestCase

# class 继承：TestCase
class Test_Login(TestCase):

    def setUp(self):
        print('每个用例“前”都执行 1 次')

    def tearDown(self):
        print('每个用例“后”都执行 1 次')

    # 以下是用例，需已 test 开头，用例可以写多个。
    def test_001(self):
        print('我是用例:case_01')
        self.assertEqual((1+2), 3)                      # 断言两个值相等

    def test_002(self):
        print('我是用例:case_02')
        res = '广深'  # 假如这是实际结果
        self.assertIn('小龙', res, msg='他说没有小龙')  # 断言 小龙 在 res 中，如果不在msg是返回值
        self.assertTrue(res == '广深')                  # 断言两个值相等（也可以False,断言==、!=、in）







