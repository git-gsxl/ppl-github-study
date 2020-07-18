
def swipeUp(driver, duration=500):
    a = driver.get_window_size()    # 获取当前屏幕上的高度与宽度
    print('当前手机屏幕分辨率为：', a)  # {'width': 1440, 'height': 2560}

    # 往上滑动
    start_x = a['width']/2
    start_y = a['height']/5*4
    end_x = a['width']/2
    end_y = a['height']/5*1
    driver.swipe(start_x, start_y, end_x, end_y, duration=500)
    # return Up

def swipeDwon(driver, duration=500):
    # 向下滑动
    a = driver.get_window_size()  # 获取当前屏幕上的高度与宽度
    print('当前手机屏幕分辨率为：', a)  # {'width': 1440, 'height': 2560}

    # 往上滑动
    start_x = a['width'] / 2
    start_y = a['height'] / 5 * 4
    end_x = a['width'] / 2
    end_y = a['height'] / 5 * 1
    driver.swipe(end_x, end_y, start_x, start_y, duration=500)


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
        # 淘宝
        "appPackage": "com.taobao.taobao",
        "appActivity": "com.taobao.tao.welcome.Welcome",
    }
    url = 'http://127.0.0.1:4723/wd/hub'
    driver = webdriver.Remote(url, driver)
    time.sleep(5)

    driver.tap([(170, 940), (160, 930), (165, 935)])
    # swipeUp(driver)
    # time.sleep(3)
    # swipeDwon(driver)
    # time.sleep(2)
    # driver.quit()

