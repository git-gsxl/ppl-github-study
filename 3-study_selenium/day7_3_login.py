from selenium import webdriver
import time
import unittest

time.sleep(2)

class zentao_login():
    def __init__(self, driver : webdriver.Chrome):
        self.driver = driver

    def login_test01(self, user="admin", psw="123456"):

        driver.find_element_by_css_selector('#account').send_keys(user)
        driver.find_element_by_css_selector('[name="password"]').send_keys(psw)
        driver.find_element_by_css_selector('#submit').click()
        time.sleep(1)

    def get_admin(self):
        t = "1234"
        y = self.driver.find_element_by_css_selector("#userMenu").text
        print(y)
        try:
            t == y
        except:
            print('错误')
        print(t)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html')
    time.sleep(2)
    zentao = zentao_login(driver)
    zentao.login_test01()
    res = zentao.get_admin()


