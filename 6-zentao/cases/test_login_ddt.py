from python_study.zentao.pages.login_page import login
from python_study.zentao.common.URL import dr, url
import unittest, ddt

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
        self.driver = dr()
        self.driver.get(url())
        self.d = login(self.driver)

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
