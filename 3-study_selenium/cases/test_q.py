import unittest
from selenium import webdriver
import time

class TestAdd(unittest.TestCase):
    @classmethod        # 每次调用都需要@classmethod

    def setUpClass(cls):    # 用例前只执行一次
        cls.driver = webdriver.Chrome()

    def setUp(self):
        self.driver.get('https://www.baidu.com')    # 每条用例执行前回到这个URL

    @classmethod
    def tearDownClass(cls):     # 用例最后只执行一次
        cls.driver.quit()

    def test_01(seif):
        seif.driver.find_element_by_css_selector('#kw').send_keys('广东')
        time.sleep(2)

    def test_02(seif):
        # 测试错误的啊
        q = seif.driver.title
        w = '百度一下，你就知'
        seif.driver.find_element_by_css_selector('#kw').send_keys('广西')
        seif.assertTrue(q == w)


if __name__ == '__mian__':
    unittest.main()