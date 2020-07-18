from selenium import webdriver
import time

# dr = webdriver.Chrome()
# dr.get('https://www.baidu.com')
#
# CSS定位，可以任意组合

# 1.id
# dr.find_element_by_css_selector('#wk').send_keys('广东')
#
# # 2.class
# dr.find_element_by_css_selector('.s_ipt').send_keys('广东')
#
# # 3.tag
# dr.find_element_by_css_selector("input").send_keys('广东')
#
# # 4.其他属性用中括号[xxx="xx"]
'''
属性组合选择过滤 没有and 只需要多个[]连接 就可以如：driver.find_element_by_css_selector('[id="blog_nav_admin"][class="menu"]').click()
'''
# dr.find_element_by_css_selector('[name="wd"]').send_keys('广东')
# dr.find_element_by_css_selector('[type="submit"]').click()

dr = webdriver.Chrome()
dr.get('http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html')
if dr.title == '用户登录 - 禅道':
    print('正确', dr.title)
else:
    print('错误')

time.sleep(2)

# 登录
dr.find_element_by_css_selector('#account').send_keys('admin')
dr.find_element_by_css_selector('[name="password"]').send_keys('123456')
dr.find_element_by_css_selector('#submit').click()
time.sleep(1)

# 获取文本值
ad = dr.find_element_by_css_selector('[data-toggle="dropdown"]').text

if ad == 'admin':
    print(ad, '登录成功')
else:
    print('登录失败')


time.sleep(3)
dr.quit()

