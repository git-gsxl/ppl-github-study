import unittest, ddt
from selenium import webdriver

test_data = [
    {'user': 'admin', 'pwd': '123456', 'exp': 'admin'},
    {'user': 'lyl', 'pwd': '123456', 'exp': 'lyl'},
    {'user': 'admin11', 'pwd': '', 'exp': ''},
    {'user': '', 'pwd': '123456', 'exp': ''},
]
# @unittest.skip('跳过1')
@ddt.ddt
class Test_login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('url')
        # self.d = login(self.driver)       # 登录模块

    def tearDown(self):
        self.driver.quit()

    @ddt.data(*test_data)
    def test_01(self, data):
        print('测试数据是：%s' % data)
        user = data['user']
        pwd = data['pwd']
        self.d.login(user, pwd)
        res = self.d.res_text()         # 实际结果
        print('获取实际结果：%s' % res)
        exp = data['exp']               # 期望结果
        self.assertEquals(res, exp)

if __name__ == '__main__':
    unittest.main()
