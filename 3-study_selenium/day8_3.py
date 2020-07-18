# 自动获取目录
import os
import unittest
import HTMLTestRunner

# 获取模块目录
dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

allsases = os.path.join(dir_path, "cases")  # 获取用例目录

report_path = os.path.join(dir_path, "report", "Test_bg.study_html")   # 报告生成目录




# 加载所有用例
all_cases = allsases  # 查找用例目录,地址不要写死


all = unittest.defaultTestLoader.discover(all_cases,
                                          pattern='test*.py',)  # 匹配所有test开头.py的文件
print(all)


# 测试报告
bg = open(report_path, "wb")

runner = HTMLTestRunner.HTMLTestRunner(stream=bg,
                        title='xxx自动化测试报告',
                        retry=0)    # retry表示执行错误的用例继续执行x次
runner.run(all)
