from appium import webdriver
import time

driver = {
  "platformName": "Android",         # 安卓系统
  "platformVersion": "6.0.1",        # 系统版本
  "deviceName": "2233ed1e",          # adb devices 机名
  "noReset": True,                   # True 为不清空应用数据，默认清空
  "unicodeKeyboard": True,           # 使用Unicode编码方式发送字符串
  "resetKeyboard": True,             # 隐藏键盘
  "automationName": "UiAutomator2",  # 相对比较稳定，最大区别可以定位toast，系统自带提示
  "chromeOptions": {'androidProcess': 'com.tencent.mm:tools'},  # 微信操作
  # 微信
  "appPackage": "com.tencent.mm",
  "appActivity": ".ui.LauncherUI",
}

# 调用 apium 服务，传上的driver参数给它
url = 'http://localhost:4723/wd/hub'    # appium 服务地址
driver = webdriver.Remote(url, driver)
time.sleep(10)

driver.find_element_by_id('com.tencent.mm:id/qi').click()
time.sleep(1)
driver.find_element_by_id('com.tencent.mm:id/li').send_keys('悠悠讲堂')
time.sleep(1)
driver.find_element_by_id('com.tencent.mm:id/rb').click()   # 点击该公众号头像
time.sleep(1)
driver.find_element_by_id('com.tencent.mm:id/aom').send_keys('悠悠讲堂我爱你')
driver.find_element_by_id('com.tencent.mm:id/aot').click()  # 发送
b = driver.contexts   #
print(b)




