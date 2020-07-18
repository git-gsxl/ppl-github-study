from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.hao123.com')
time.sleep(2)

# 句柄切换
handlel = driver.current_window_handle  # 当前的
print(handlel)

driver.find_element_by_link_text('人民网').click()
time.sleep(2)

handlels = driver.window_handles  # 所有的
print(handlels)

# 获取最新打开的窗口
print(handlels[-1])
driver.switch_to_window(handlels[-1])
tl = driver.title
print('当前的title为：%s' % tl)

driver.close()      # 关闭当前窗口

# 回到第一个窗口
driver.switch_to_window(handlels[0])
tll = driver.title
print('回到第一个：', tll)




time.sleep(2)
driver.quit()

