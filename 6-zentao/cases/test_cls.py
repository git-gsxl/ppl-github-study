from python_study.zentao.pages.login_page import login, dr, url
import unittest, ddt, os
from python_study.zentao.common.excel_read import Excel

curpath = os.path.dirname(os.path.realpath(__file__))   # 获取当前目录
excelpath = os.path.join(curpath,
                         '\Study_python\project_lyl\zentao\excel_data\cases_login.xls')    # 获取目录下的cases_login。这个文件
data = Excel(excelpath)                                 # 调用这个类
test_data = data.dict_data()                            # 调用这个类的方法

# @unittest.skip('跳过')
@ddt.ddt
class Test_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = dr()
        cls.d = login(cls.driver)
        cls.driver.get(url())


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        alert = self.d.is_alert()   # 每次用例前判断是否有弹窗
        if alert:
            print(alert.text)       # 打印弹窗内容
            alert.accept()          # 弹窗 点击确定
        self.driver.delete_all_cookies()    # 清空缓存，退出登录
        self.driver.refresh()               # 刷新页面

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
