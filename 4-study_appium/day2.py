from appium import webdriver
import time

driver = {
  "platformName": "Android",        # 安卓系统
  "platformVersion": "6.0.1",       # 系统版本
  "deviceName": "2233ed1e",         # adb devices 机名
  "noReset": True,                  # True 为不清空应用数据，默认清空
  "unicodeKeyboard": True,  # 使用Unicode编码方式发送字符串
  "resetKeyboard": True,    # 隐藏键盘
  "automationName": "UiAutomator2",

  # 陀螺世界
  # "appPackage": "com.tuoluo.world",
  # "appActivity": "com.tuoluo.world.ui.activity.SplashActivity",

  # 淘宝
  "appPackage": "com.taobao.taobao",
  "appActivity": "com.taobao.tao.welcome.Welcome",
}

# 调用 apium 服务，传上的driver参数给它
url = 'http://localhost:4723/wd/hub'    # appium 服务地址
driver = webdriver.Remote(url, driver)
time.sleep(2)

# 1、id 定位
# driver.find_element_by_id('com.taobao.taobao:id/home_searchedit').click()

# 2、xpath定位
# driver.find_element_by_xpath('//*[@text="扫一扫"]').click()

# 3、content_desc定位
# driver.find_element_by_accessibility_id('跳转到猜你喜欢').click()

# 4、class定位
driver.find_element_by_class_name('android.widget.RelativeLayout') .click()

# 5、list(elements)定位  可以组合上述几种使用
# driver.find_elements_by_class_name('class元素值')[0].click()

# driver.find_elements_by_id('xxx元素值')[0].click()



