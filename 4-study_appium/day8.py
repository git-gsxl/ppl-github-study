from project_lyl.app.common.start import start_app
import time, unittest

class Test_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = start_app()

    # 获取当前页面的 activity
    def test_001(self):
        act1 = self.driver.current_activity
        print(act1)

        self.driver.find_element_by_id('com.taobao.taobao:id/tab_title').click()
        self.driver.wait_activity('com.taobao.weex.WXActivity', 10)      # 等待它的出现
        time.sleep(3)
        act2 = self.driver.current_activity
        print(act2)

        # adb获取：adb shell dumpsys activity top | findstr ACTIVITY
        self.driver.start_activity('com.taobao.taobao', 'com.taobao.tao.TBMainActivity')    # 自动跳转到这个页面

        act3 = self.driver.current_activity
        print(act3)
        time.sleep(3)
