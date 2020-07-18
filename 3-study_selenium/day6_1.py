import unittest
import HTMLTestRunner

# 加载所有用例
all_cases = "G:\selenium_test\one_day"  # 查找用例目录,地址不要写死


all = unittest.defaultTestLoader.discover(all_cases,
                                          pattern='test*.py',)  # 匹配所有test开头.py的文件
print(all)


# 测试报告
bg = open(r"C:\Users\Administrator\Desktop\BG1.study_html", "wb")

runner = HTMLTestRunner.HTMLTestRunner(stream=bg,
                        title='测试报告',
                        retry=0)    # retry表示执行错误的用例继续执行x次
runner.run(all)
