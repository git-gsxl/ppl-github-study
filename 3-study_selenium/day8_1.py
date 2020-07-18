import time
import unittest
from selenium import webdriver


def login(driver, user = 'admin',pwd = '123456' ):
    driver.find_element_by_css_selector('#account').send_keys(user)
    driver.find_element_by_css_selector('[name="password"]').send_keys(pwd)
    driver.find_element_by_css_selector('#submit').click()
    time.sleep(2)

def login_jieguo(driver):
    res = ""
    try:
        res = driver.find_element_by_css_selector('#userMenu').text
        # print('如果定位到了')
    except:
        res = ""
    return res

class Test_login(unittest.TestCase):

    def setUp(self):           # 每个用例前执行一次
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html')

    def tearDown(self):     # 每个用例后执行一次
        self.driver.quit()

    def test_login1(self):
        login(self.driver, '123')
        res = login_jieguo(self.driver)
        exp = '213'
        self.assertTrue(res != exp)

    def test_lgoin2(self):
        login(self.driver, 'lyl12')
        res = login_jieguo(self.driver)
        # print(res)
        exp = '李四'
        self.assertTrue(res == exp)

    def test_login2(self):
        login(self.driver)
        res = login_jieguo(self.driver)
        # print(res)
        exp = 'admin'
        self.assertTrue(res == exp)


if __name__ == '__main__':
    unittest.main()
