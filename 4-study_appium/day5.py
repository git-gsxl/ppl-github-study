'''

1.触摸：tap
2.短按：press
3.长按：long_press
4.等待：wait
5.移动到：moveTo
6.释放：release
7.执行：perfrom

'''

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

driver = {
  "platformName": "Android",         # 安卓系统
  "platformVersion": "6.0.1",        # 系统版本
  "deviceName": "2233ed1e",          # adb devices 机名
  "noReset": True,                   # True 为不清空应用数据，默认清空
  "unicodeKeyboard": True,           # 使用Unicode编码方式发送字符串
  "resetKeyboard": True,             # 隐藏键盘
  "automationName": "UiAutomator2",  # 相对比较稳定，最大区别可以定位toast，系统自带提示
  # 淘宝
  "appPackage": "com.taobao.taobao",
  "appActivity": "com.taobao.tao.welcome.Welcome",
}
url = 'http://127.0.0.1:4723/wd/hub'
driver = webdriver.Remote(url, driver)
time.sleep(5)

driver.find_element_by_xpath('//*[@content-desc="我的淘宝"]').click()
time.sleep(10)  # 获取不到，请手动点击帮助按钮

driver.swipe(140, 620, 1400, 620, duration=2000)    # 坐标按着滑动
