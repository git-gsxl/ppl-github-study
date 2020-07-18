'''
一、环境搭建
1.详细看：Appium-环境搭建.docx

2.ADB 常用命令：
连接设备：adb connect 127.0.0.1:62025
显示连接设备：adb devices
路径安装app：adb install 	[app路径]　
包名安装app：adb uninstall　[app 包名]
显示第三方应用：adb shell ps list package -3
APP/PC拷贝文件：adb pull  <path-APP>  <path-pc>　　 -p　　显示进度
进入shell：adb shell　
启动adb server：adb start-server　　
停止adb server：adb kill-server　　　
重启设备：adb reboot　
任意键继续：pause
杀掉menkey 进程：①adb shell		②ps | grep menkey		③kill -9 20857

获取包名：aapt d badging pak

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
time.sleep(3)

driver.find_element_by_id('com.taobao.taobao:id/home_searchedit').click()
time.sleep(1)
driver.find_element_by_id('com.taobao.taobao:id/searchEdit').send_keys('充气娃娃')
driver.find_element_by_id('com.taobao.taobao:id/searchbtn').click()
time.sleep(3)
driver.quit()

