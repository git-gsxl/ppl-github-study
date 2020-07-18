import unittest
from selenium import webdriver
import time

class TestAdd(unittest.TestCase):

    def setUp(self):    # 每个用例前执行一次
        self.dr = webdriver.Chrome()
        self.dr.get('https://www.baidu.com')

    def tearDown(self):     # # 每个用例后执行一次
        time.sleep(2)
        self.dr.quit()

    def test_01(self):
        self.dr.find_element_by_css_selector('#kw').send_keys('广东')
        self.dr.find_element_by_css_selector('#wd').click()

    def test_02(self):
        self.dr.find_element_by_css_selector('#kw').send_keys('广西')
        self.dr.find_element_by_css_selector('#wd').click()

if __name__ == '__mian__':
    unittest.main()