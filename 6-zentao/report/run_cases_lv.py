import os
import unittest
import HTMLTestRunner

dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # 获取模块目录

allsases = os.path.join(dir_path, "cases")  # 获取用例目录

report_path = os.path.join(dir_path, "report", "ZT_test.study_html")   # 报告生成目录,文件为ZT_test.study_html

all_cases = allsases  # 加载所有用例

all = unittest.defaultTestLoader.discover(all_cases,
                                          pattern='test*.py',)  # 匹配所有test开头.py的文件
print(all)

bg = open(report_path, "wb")    # 测试报告

runner = HTMLTestRunner.HTMLTestRunner(stream=bg,
                        title='禅道自动化测试报告',
                        retry=0)    # retry表示执行错误的用例继续执行x次

runner.run(all)     # 开始
bg.close()          # 关闭它不然会出问题
