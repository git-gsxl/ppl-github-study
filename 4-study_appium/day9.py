from appium import webdriver
import getopt, sys

# 淘宝APP包名和activity配置
package = 'com.taobao.taobao'
activity = 'com.taobao.tao.welcome.Welcome'

des_max2 = {
    "platformName": "Android",  # 安卓系统
    "platformVersion": "6.0.1",  # 系统版本
    "deviceName": "2233ed1e",  # adb devices 机名
    "noReset": True,  # True 为不清空应用数据，默认清空
    "unicodeKeyboard": True,  # 使用Unicode编码方式发送字符串
    "resetKeyboard": True,  # 隐藏键盘
    "automationName": "UiAutomator2",  # 相对比较稳定，最大区别可以定位toast，系统自带提示
    "udid": "2233ed1e",
    "appPackage": package,
    "appActivity": activity,
     "post": "4710"}

des_yeshen = {
    "platformName": "Android",  # 安卓系统
    "platformVersion": "5.1.1",  # 系统版本
    "deviceName": "127.0.0.1:62001",  # adb devices 机名
    "noReset": True,  # True 为不清空应用数据，默认清空
    "unicodeKeyboard": True,  # 使用Unicode编码方式发送字符串
    "resetKeyboard": True,  # 隐藏键盘
    "automationName": "UiAutomator2",  # 相对比较稳定，最大区别可以定位toast，系统自带提示
    "udid": "127.0.0.1:62001",
    "appPackage": package,
    "appActivity": activity,
    "post": "4720"}

des_62025 = {
    "platformName": "Android",
    "platformVersion": "5.0.1",
    "deviceName": "127.0.0.1:62025",
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "automationName": "UiAutomator2",
    "udid": "127.0.0.1:62025",
    "appPackage": package,
    "appActivity": activity,
    "post": "4730"}

def main(argv):
    deviceName = 'max2'
    try:
        # 这里的 h 就表示该选项无参数，n:表示 n 选项后需要有参数
        opts, args = getopt.getopt(argv, 'hn:', ['device='])
    except getopt.GetoptError:
        print('错误，请传参数: app.py -n <devicename>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print('帮助信息：app.py -n <devicename>')
            sys.exit()
        elif opt in ("-n", "--device"):
            deviceName = arg
    print('启动手机设备名称为 : %s' % deviceName)
    return deviceName

def start_app(n=None):
    ''' 设备选择，默认为：max2 '''
    if n == None:
        deviceName = main(sys.argv[1:])
    else:
        deviceName = n

    if deviceName == "max2":
        des = des_max2
        post = des_max2['post']
    elif deviceName == "yeshen":
        des = des_yeshen
        post = des_yeshen['post']
    else:
        des = des_62025
        post = des_62025['post']
    driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub' % post, des)
    return driver

if __name__ == '__main__':
    start_app()

