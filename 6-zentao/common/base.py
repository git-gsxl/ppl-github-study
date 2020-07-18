from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Base():

    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.timeout = 3
        self.alert_timeout = 0.5
        self.poll = 1

    def find(self, locator):            # 查找元组方法
        '''locator = ("id", "id值")'''  # 所有定位方法都可以用
        element = WebDriverWait(self.driver, self.timeout, self.poll).until(
            lambda x: x.find_element(*locator))
        return element

    def finds(self, locator):           # 查找多个元组方法
        '''locator = ("id", "id值")'''  # 所有定位方法都可以用
        elements = WebDriverWait(self.driver, self.timeout, self.poll).until(
            lambda x: x.find_elements(*locator))
        return elements

    def send(self, locator, _text):
        self.find(locator).send_keys(_text)

    def click(self, locator):
        self.find(locator).click()

    def clear(self, locator):
        self.find(locator).clear()

    def text_in_enement(self, locator, _text):
        '''断言文本值'''
        try:  # 抛异常
            res = WebDriverWait(self.driver, self.timeout, self.poll
                                ).until(EC.text_to_be_present_in_element(locator, _text))
            return res
        except:
            return False

    def value_in_enement(self, locator, _text):
        '''断言value值'''
        try:
            res = WebDriverWait(self.driver, self.timeout, self.poll
                                ).until(EC.text_to_be_present_in_element_value(locator, _text))
            return res
        except:  # 抛异常
            return False

    def no_enement(self, locator):
        '''断言元素是否存在'''
        try:
            res = self.find(locator)
            return True
        except:
            return False

    def move_element(self, locator):
        '''鼠标悬停操作'''
        element = self.find(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def select_index(self, locator, index=0):
        '''select中的index方法'''
        element = self.find(locator)
        Select(element).select_by_index(index)

    def select_value(self, locator, value):
        '''select中的value方法'''
        element = self.find(locator)
        Select(element).deselect_by_value(value)

    def select_text(self, locator, text):
        '''select中的text方法'''
        element = self.find(locator)
        Select(element).select_by_visible_text(text)

    def is_alert(self):
        '''alert弹窗处理：①确定：accept() ②取消：dismiss() ③输入值:send_keys() ④获取弹出框文本：text'''
        try:
            alert = WebDriverWait(self.driver, self.alert_timeout, self.poll).until(EC.alert_is_present())
            if alert:
                alert = self.driver.switch_to.alert
                return alert
        except:
            return False

    def get_text(self, locator):
        '''获取元素的文本值'''
        try:
            element_text = WebDriverWait(self.driver, self.timeout, self.poll).until(
                lambda x: x.find_element(*locator).text)
        except:
            element_text = ''
        return element_text

    def js_top(self):
        '''滑动至顶部，内嵌滚动条需先定位到iframe'''
        self.driver.execute_script('window.scrollTo(0,0)')

    def js_element(self, locator):
        '''聚焦元素位置'''
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def js_tail(self):
        '''滑动至底部'''
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

if __name__ == '__main__':
    from common.URL import dr, url
    d = dr()
    d.get(url())
    loc_user = ('css selector', '#account')
    loc_pwd = ('css selector', '[type="password"]')
    loc_login = ('css selector', '#submit')
    d.find_element(*loc_user).send_keys('admin')
    d.find_element(*loc_pwd).send_keys('123456')
    d.find_element(*loc_login).click()
    c = Base(d)
    loc = ('id', '1')
    t = c.res(loc)
    print(t)

    # driver = dr()
    # driver.get('https://www.baidu.com/')
    # b = Base(driver)
    # l1 = ('css selector', '#kw')
    # b.send(l1, 'AI')
    #
    # l3 = ('css selector', '#su')
    # b.click(l3)
    #
    # loc = ('css selector', '[class="t c-gap-bottom-small"]')
    # p = b.no_enement(loc)
    # import time
    # time.sleep(2)
    # print(p)
    # driver.quit()

