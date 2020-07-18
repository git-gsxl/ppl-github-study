''' 裁剪验证码 '''
from selenium import webdriver
import time
from PIL import Image           # 安装：Pioolw 库

driver = webdriver.Chrome()
driver.get('http://zhuan.weiwee.com/SignIn.aspx')
time.sleep(2)

a = ('xpath', '//input[@id="ValidateCode"]')    # 点击出现验证码
b = ('xpath', '//img[@id="validatecode"]')      # 验证码位置
t = driver.find_element(*a).click()

# 整个截图
driver.save_screenshot('G:\\project_lyl\\study_day\\selenium_day\\muke\\img.png')

loc_img = driver.find_element(*b)   # 验证码位置
print(loc_img.location)

# 设置计算 验证码 它的坐标位置
left = loc_img.location['x']
top = loc_img.location['y']
right = loc_img.size['width'] + left
height = loc_img.size['height'] + top
im = Image.open('G:\\project_lyl\\study_day\\selenium_day\\muke\\img.png')

# 裁剪验证码，命名为：1img.png 保存
img = im.crop((left, top, right, height))
img.save('G:\\project_lyl\\study_day\\selenium_day\\muke\\1img.png')
