#coding=UTF-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains    # 鼠标悬停模块
from selenium.webdriver.support.select import Select    # 导入select下拉框处理的模块

driver = webdriver.Chrome()
driver.get(r"http://www.baidu.com/")

# 鼠标悬停
mo = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(mo).perform()
time.sleep(1)
driver.find_element_by_link_text('搜索设置').click()
time.sleep(1)

# iframe切换
# iframe = driver.find_element_by_id('xxx')
# driver.switch_to_frame(iframe)

# 传索引
# driver.switch_to_frame(0)
# driver.switch_to_default_content()  # 回到首页


# select下拉框操作
# 1.xpath方法
# dr.find_element_by_xpath('//*[@id="nr"]/option[3]').click()

# 2.select方法
# se = driver.find_element_by_id('nr')  # 部分匹配方法
# Select(se).select_by_value('50')

# se = driver.find_element_by_id('nr')    # 全匹配方法
# Select(se).select_by_visible_text('每页显示50条')

# 3.value方法
se = driver.find_element_by_id('nr')
Select(se).select_by_value('50')

time.sleep(2)
driver.find_element_by_link_text('保存设置').click()
time.sleep(2)

# 切换到alert弹窗 标准控件只有确定、取消、输入
al = driver.switch_to.alert
print(al.text)
al.accept()     # 点击“确定”
# al.dismiss()    # 点击“取消”
# al.send_keys("输入内容")

# xpath在Chrome浏览器调试，每个元素都可以
# $x('//*[@id="kw"]')
# $x('//*[text()="新闻"]')

time.sleep(5)
driver.quit()



