from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html')
time.sleep(2)

# jQuery脚本语法
jq = '''
$('#account').val('admin');
$('[name="password"]').val('123456');
$('[name="keepLogin[]"]').click();
$('#submit').click()

'''
driver.execute_script(jq)

time.sleep(2)
driver.quit()


'''
                JS语法
            
1.通过id获取
document.getElementById(“id”)----------获取的是单个

2.通过name获取
document.getElementsByName(“Name”)[0]---------获取的是多个
返回的是list 


3.通过标签名选取元素
document.getElementsByTagName(“tag”) --------获取的是多个


4.通过CLASS类选取元素
document.getElementsByClassName(“class”) --------获取的是多个
兼容性：IE8及其以下版本的浏览器未实现getElementsByClassName方法

5.通过CSS选择器选取元素  （应常用定位不到的元素）
document.querySelectorAll(“css selector")
兼容性：IE8及其以下版本的浏览器只支持CSS2标准的选择器语法
'''
'''
代码参考：
from selenium import webdriver
from pages.login_page import Login

driver = webdriver.Firefox()
a = Login(driver)
a.login()

# 打开bug编辑页面
driver.get("http://127.0.0.1:81/zentao/bug-create-1-0-moduleID=0.html")

# 插入body内容
body = "hello world"

# 执行js语句
js1 = 'document.getElementsByClassName("ke-edit-iframe")[0].contentWindow.document.body.innerHTML="%s"'%body
driver.execute_script(js1)


'''