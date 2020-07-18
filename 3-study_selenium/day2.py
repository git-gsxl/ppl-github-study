from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains  # 导入鼠标悬停模块
from selenium.webdriver.common.keys import Keys                     # 导入键盘事件模块

dr = webdriver.Chrome()
dr.get('https://www.baidu.com')
time.sleep(2)

# 1.id定位= kw，输入‘广东’
# dr.find_element_by_id('kw').send_keys('广东')

# 2.name定位= wd，输入‘广东’
# dr.find_element_by_name('wd').send_keys('广东')

# 3.class定位= s_ipt，输入‘广东’
# dr.find_element_by_class_name('s_ipt').send_keys('广东')

# 4.tag标签定位= input
dr.find_element_by_tag_name('input').send_keys('广东')

# 5.link text定位= 地图，点击地图
# dr.find_element_by_link_text('地图').click()  # 匹配全部
# dr.find_element_by_partial_link_text('设为主页').click()    # 匹配部分

# 6.xpath定位= //*[@id="kw"]，输入‘广东’
# dr.find_element_by_xpath('//*[@id="kw"]').send_keys('广东')   # 注意单双引号交替使用

# 7.任意元素复数定位= mnav，点击地图
# dr.find_elements_by_class_name('mnav')[2].click() # 注意是find_elements


# 鼠标悬停事件
mo = dr.find_element_by_link_text('设置')
ActionChains(dr).move_to_element(mo).perform()
time.sleep(1)
dr.find_element_by_link_text('搜索设置').click()


# 键盘输入事件 F1-F12等
dr.find_element_by_id('kw').send_keys(Keys.TAB)

time.sleep(2)

dr.quit()
