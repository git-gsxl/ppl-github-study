'''
1.进入小程序；
2.cmd输入：①adb shell ②dumpsys activity top | grep ACTIVITY
3.cmd中出现：appbrand0;是什么就把它放在driver参数中：
"chromeOptions": {'androidProcess': 'com.tencent.mm:appbrand0'}
注意：内核驱动版本对应，不用切换webvivw,公众号需要切换；
'''

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
  "chromeOptions": {'androidProcess': 'com.tencent.mm:appbrand0'},  # 微信小程序操作
  # 微信
  "appPackage": "com.tencent.mm",
  "appActivity": ".ui.LauncherUI",
}

# 调用 apium 服务，传上的driver参数给它
url = 'http://localhost:4723/wd/hub'    # appium 服务地址
driver = webdriver.Remote(url, driver)
time.sleep(10)

driver.find_elements_by_id('com.tencent.mm:id/sh')[2].click()
time.sleep(1)
driver.find_element_by_xpath('//*[@text="小程序"]').click()
time.sleep(1)
driver.find_elements_by_id('com.tencent.mm:id/jq')[0].click()
time.sleep(10)
b = driver.contexts     # 小程序不用切换
print(b)
driver.find_elements_by_id('com.tencent.mm:id/cw')[2].click()
cur = driver.current_context    # 获取当前 webvivw
print('当前的webvivw为：', cur)
time.sleep(1000)



