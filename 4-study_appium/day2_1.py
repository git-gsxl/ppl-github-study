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

  # 淘宝
  "appPackage": "com.taobao.taobao",
  "appActivity": "com.taobao.tao.welcome.Welcome",
}

# 调用 apium 服务，传上的driver参数给它
url = 'http://localhost:4723/wd/hub'    # appium 服务地址
driver = webdriver.Remote(url, driver)
time.sleep(2)

# uiautomator text定位
loc_text = 'text("扫一扫")'
driver.find_element_by_android_uiautomator(loc_text).click()

# uiautomator id定位
loc_id = 'resourceId("android.widget.RelativeLayout")'
driver.find_element_by_android_uiautomator(loc_id).send_keys('手机')

# uiautomator dese定位
loc_desc = 'description("跳转到猜你喜欢")'
driver.find_element_by_android_uiautomator(loc_desc).click()

# uiautomator class定位
loc_class = 'className("android.widget.RelativeLayout")'
driver.find_element_by_android_uiautomator(loc_class).click()

# uiautomator class_text 组合定位,可以任意组合
loc_class_text = 'className("  ").text("  ")'
driver.find_element_by_android_uiautomator(loc_class_text).click()

# uiautomator 父级定位：childSelector
log_input = 'resourceID("resourceid元素值").childSelector(text("text元素值"))'
driver.find_element_by_android_uiautomator(log_input).click()

# uiautomator 兄弟定位：fromParent
log_input = 'resourceID("resourceid元素值").fromParent(text("text元素值"))'
driver.find_element_by_android_uiautomator(log_input).click()
