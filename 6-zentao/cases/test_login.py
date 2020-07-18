from python_study.zentao.pages.login_page import login
from python_study.zentao.common.URL import dr, url
import unittest

class Test_login(unittest.TestCase):

    def setUp(self):
        self.driver = dr()
        self.driver.get(url())
        self.d = login(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login001(self):
        self.d.login()
        res = self.d.res_text()
        exp = 'admin'
        self.assertEquals(res, exp)
        print('实际结果是：%s' % res)
