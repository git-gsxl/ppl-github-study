# coding=utf-8
from selenium import webdriver
import time

path = r'H:\python\chromedriver.exe'
profile = webdriver.FirefoxProfile(path)
driver = webdriver.Firefox(profile)  # 火狐浏览器加载配置

# op = webdriver.ChromeOptions()    # 谷歌浏览器加载配置，路径不要有中文
# op.add_argument(r'—user-data-dir=C:\Users\Default\AppData\Local\360Chrome\Chrome\User Data')
# driver = webdriver.Chrome(Chrome_options=op)

driver.get('https://www.baidu.com')

time.sleep(2)       # 等待2s
driver.back()       # 返回
driver.forward()    # 右箭头
driver.refresh()    # 刷新页面
driver.quit()       # 退出浏览器

'''
①windows 64位 安装pycharm
②python 3.6版本 环境变量配置
③pip install selenium 安装selenium库(ddt 1.1.2 , xrld )
'''

