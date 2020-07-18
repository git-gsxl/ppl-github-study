
import os, time

def start_appium(port=4723):
    if not is_start_appium():
        os.system('appium -p %s' % port)
    else:
        print('appium服务已启动，端口：%s' % port)

def is_start_appium(port=4723):
    r = os.popen('netstat -ano | findstr "%s" ' % port)
    time.sleep(2)
    t = r.read()
    pid = str(t).split(" ")[-1]
    if 'LISTENING' in t:
        print('appium服务已启动pid为：%s' % pid)
        return True
    else:
        return False

def kill_appium(port=4723):
    r = os.popen('netstat -ano | findstr "%s" ' % port)
    time.sleep(2)
    t = r.read()
    pid = str(t).split(" ")[-1]
    if 'LISTENING' in t:
        os.popen("taskkill /f /pid %s" % pid)
        print('已kill掉进程：%s' % pid)
    else:
        pass

if __name__ == '__main__':
    print(is_start_appium())
    start_appium()
    kill_appium()
    time.sleep(5)
    print(is_start_appium())
    start_appium()
