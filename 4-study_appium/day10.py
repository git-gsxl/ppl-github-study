from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver

class Base():
    def __init__(self, driver:webdriver.Remote, t=500, n=1, timeout=10):
        '''t=滑动ms，n=循环多少次  '''
        self.driver = driver
        self.t = t
        self.n = n
        self.a = self.driver.get_window_size()  # 获取当前屏幕上的高度与宽度
        self.timeout = timeout

    def click(self, locator):
        self.find(locator).click()

    def clear(self, locator):
        self.find(locator).clear()

    def send(self, locator, _text):
        self.find(locator).send_key(_text)

    def find(self, locator):
        '''
        单个元素定位：
        locator={'name': '元素名称', 'by': 'id', 'value': 'xx'}
        '''
        if "name" in locator:
            print('正在定位元素名称：%s' % locator['name'], "，定位方法：%s-->%s" % (locator['by'], locator['value']))

        if "desc" in locator['by']:
            ele = WebDriverWait(self.driver, self.timeout, 1).until(
                lambda x: self.driver.find_element_by_accessibility_id(locator['value']))
        elif "text" in locator["by"]:
            value = '//*[@text="%s"]' % locator['value']
            ele = WebDriverWait(self.driver, self.timeout, 1).until(
                lambda x: self.driver.find_element_by_xpath(value))
        elif "android" in locator["by"]:
            ele = WebDriverWait(self.driver, self.timeout, 1).until(
                lambda x: self.driver.find_element_by_android_uiautomator(locator['value']))
        else:
            loc = (locator['by'], locator['value'])
            ele = WebDriverWait(self.driver, self.timeout, 1).until(
                EC.presence_of_element_located(loc))
        return ele

    def finds(self, locator):
        '''
        复数定位：
        locator={'by': 'id', 'value': 'xx'}
        '''
        if "name" in locator:
            print('正在定位元素名称：%s' % locator['name'], "，定位方法：%s-->%s" % (locator['by'], locator['value']))
        if "desc" in locator['by']:
            ele = WebDriverWait(self.driver, self.timeout, 1).until(
                lambda x: self.driver.find_elements_by_accessibility_id(locator['value']))
        elif "text" in locator["by"]:
            value = '//*[@text="%s"]' % locator['value']
            ele = WebDriverWait(self.driver, self.timeout, 1).until(
                lambda x: self.driver.find_elements_by_xpath(value))
        elif "android" in locator["by"]:
            ele = WebDriverWait(self.driver, self.timeout, 1).until(
                lambda x: self.driver.find_elements_by_android_uiautomator(locator['value']))
        else:
            loc = (locator['by'], locator['value'])
            ele = WebDriverWait(self.driver, self.timeout, 1).until(
                EC.presence_of_all_elements_located(loc))
        return ele

    def is_toast(self, _text):
        ''' 模糊匹配toast '''
        loc_toast = ("xpath", ".//*[contains(@text,'%s')]" % _text)
        try:
            ele = WebDriverWait(self.driver, 10, 0.3).until(EC.presence_of_element_located(loc_toast))
            t = ele.text
            print("toast实际结果为：", t)
            if _text in t:
                return True
            else:
                return False
        except:
            print('toast没有找到')
            return False

    def tap(self, x=None, y=None, el=None):
        '''点击元素，可传坐标xy或元素值 '''
        action = TouchAction(self.driver)
        if el is not None:
            action.tap(element=el, count=self.n).perform()
        else:
            action.tap(x=x, y=y, count=self.n).perform()

    def swipeUp(self):
        ''' 向上滑动 '''
        print('当前手机屏幕分辨率为：', self.a)  # {'width': 1440, 'height': 2560}

        start_x = self.a['width'] / 2
        start_y = self.a['height'] / 5 * 4
        end_x = self.a['width'] / 2
        end_y = self.a['height'] / 5 * 1
        for i in range(self.n):
            self.driver.swipe(start_x, start_y, end_x, end_y, duration=self.t)

    def swipeDwon(self):
        ''' 向下滑动 '''
        print('当前手机屏幕分辨率为：', self.a)  # {'width': 1440, 'height': 2560}

        start_x = self.a['width'] / 2
        start_y = self.a['height'] / 5 * 4
        end_x = self.a['width'] / 2
        end_y = self.a['height'] / 5 * 1
        for i in range(self.n):
            self.driver.swipe(start_x, start_y, end_x, end_y, duration=self.t)

    def swipLeft(self):
        ''' 向左滑动 '''
        print('当前手机屏幕分辨率为：', self.a)  # {'width': 1440, 'height': 2560}
        start_x = self.a['width'] / 4
        start_y = self.a['height'] / 2
        end_x = self.a['width'] / 4 * 3
        end_y = self.a['height'] / 2
        for i in range(self.n):
            self.driver.swipe(start_x, start_y, end_x, end_y, duration=self.t)

    def swipRight(self):
        ''' 向右滑动 '''
        print('当前手机屏幕分辨率为：', self.a)  # {'width': 1440, 'height': 2560}
        start_x = self.a['width'] / 4
        start_y = self.a['height'] / 2
        end_x = self.a['width'] / 4 * 3
        end_y = self.a['height'] / 2
        for i in range(self.n):
            self.driver.swipe(end_x, end_y, start_x, start_y, duration=self.t)


if __name__ == '__main__':
    from appium import webdriver
    import time
    driver = {
        "platformName": "Android",  # 安卓系统
        "platformVersion": "6.0.1",  # 系统版本
        "deviceName": "2233ed1e",  # adb devices 机名
        "noReset": True,  # True 为不清空应用数据，默认清空
        "unicodeKeyboard": True,  # 使用Unicode编码方式发送字符串
        "resetKeyboard": True,  # 隐藏键盘
        "automationName": "UiAutomator2",  # 相对比较稳定，最大区别可以定位toast，系统自带提示
        # 微信
        # "appPackage": "com.tencent.mm",
        # "appActivity": ".ui.LauncherUI",
        # 淘宝
        "appPackage": "com.taobao.taobao",
        "appActivity": "com.taobao.tao.welcome.Welcome",
    }
    url = 'http://127.0.0.1:4723/wd/hub'
    driver = webdriver.Remote(url, driver)
    time.sleep(5)
    b = Base(driver)
    # loc_login = {'by': 'desc', 'value': '我的淘宝'}
    # loc_login = {'by': 'text', 'value': '分类'}
    # loc_login = {'by': 'android', 'value': 'text("分类")'}
    loc_login = {'name': '分类按钮', 'by': 'id', 'value': 'com.taobao.taobao:id/tab_title'}
    b.click(loc_login)

    # locs_login = {'by': 'class name', 'value': 'android.widget.TextView'}
    # d = b.finds(locs_login)
    # print(d)
    # print(len(d))
    # d[1].click()

