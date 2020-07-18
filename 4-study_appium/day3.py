
# Chrome浏览器输入url,看它内核版本：chrome://inspect/

# webvivw，需要开启webview远程调试功能， Android 4.4以上，需要在应用代码中增加一下代码段开启该功能
# 可由开发人员增加后重新打包给测试，修改Activity extends CordovaActivity，设置setWebContentsDebuggingEnabled(true);

# No Chromedriver found that can automate Chrome '46.0.2490' 没有46版本装驱动

# 下载地址：https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/web/chromedriver.md

# 驱动放置路径：
# C:\Users\Administrator\AppData\Local\Programs\Appium\resources\app\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win
# C:\Users\Administrator\node_modules\appium-chromedriver\chromedriver\win

# 2.命令行版本里面的chromedriver在本地电脑上地址：
# C:\sers\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\appium-android-driver\node_modules\appium-chromedriver\chromedriver\win

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

  # 陀螺世界
  # "appPackage": "com.tuoluo.world",
  # "appActivity": "com.tuoluo.world.ui.activity.SplashActivity",

  # 淘宝
  # "appPackage": "com.taobao.taobao",
  # "appActivity": "com.taobao.tao.welcome.Welcome",

  # 智行火车票
  "appPackage": "com.yipiao",
  "appActivity": "com.zt.main.entrance.ZTLaunchActivity",
}

# 调用 apium 服务，传上的driver参数给它
url = 'http://localhost:4723/wd/hub'    # appium 服务地址
driver = webdriver.Remote(url, driver)
time.sleep(8)

driver.find_element_by_android_uiautomator('text("我的")').click()
time.sleep(1)
driver.find_element_by_android_uiautomator('text("产品意见")').click()
time.sleep(1)

cur = driver.current_context    # 获取当前 webvivw
print('当前的webvivw为：', cur)

time.sleep(1)                   # 获取全部 webvivw
a = driver.contexts
print('全部的webvivw为：', a)

time.sleep(1)
# driver.switch_to.context(a[-1])
# b = driver.current_context
driver.switch_to.context('WEBVIEW_com.yipiao')
b = driver.current_context
print(b)

# 保存页面信息到本地,进行元素定位
h = driver.page_source

with open('page.html', 'wb') as f:    # 保存写入这个页面源码，格式为 utf-8
    f.write(h.encode('utf-8'))

driver.find_element_by_id('feedback-contact').send_keys('13364678451')
