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

    # 智行火车票
    # "appPackage": "com.yipiao",
    # "appActivity": "com.zt.main.entrance.ZTLaunchActivity",
}
url = 'http://127.0.0.1:4723/wd/hub'
driver = webdriver.Remote(url, driver)
time.sleep(5)

# 获取当前页面的 activity
act1 = driver.current_activity
print(act1)

driver.find_element_by_id('com.taobao.taobao:id/tab_title').click()
driver.wait_activity('com.taobao.weex.WXActivity', 10)      # 等待它的出现
time.sleep(3)
act2 = driver.current_activity
print(act2)

# adb获取：adb shell dumpsys activity top | findstr ACTIVITY
driver.start_activity('com.taobao.taobao', 'com.taobao.tao.TBMainActivity')    # 自动跳转到这个页面

act3 = driver.current_activity
print(act3)
time.sleep(3)


driver.keyevent(keycode=3)  # HOME 键
