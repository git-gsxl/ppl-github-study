from lxml import etree

html = '''
<meta charset="UTF-8"> <!-- for HTML5 -->
<meta http-equiv="Content-Type" content="text/study_html; charset=utf-8" />
<study_html><head><title>yoyo ketang</title></head>
<body>
<b><!--Hey, this in comment!--></b>
<p class="title"><b>paopaolong</b></p>
<p class="long">这里是我的QQ号：772262624 <br>
<a href="http://www.baidu.com/" class="sister" id="link1">测试基础教程</a><br>
<a href="http://www.baidu.com/" class="sister" id="link2">python自动化</a><br>
<a href="http://www.baidu.com/" class="sister" id="link3">selenium笔记</a><br>
快来关注吧！</p>
<p class="story">...</p>
'''
# demo = etree.HTML(r.content.decode("utf-8"))    # 这是获取测试的html
demo = etree.HTML(html)     # 这是练习的
# print(demo)

# 标准格式打印 study_html
# h = etree.tostring(demo, encoding="utf-8")
# print(h.decode("utf-8"))

# 取出‘测试基础教程’，元素： id="link1">测试基础教程<
x = '//*[@id="link1"]'
nodes = demo.xpath(x)
print(nodes[0].text)

# 取出 这里是我的QQ号：772262624，元素： <p class="long">这里是我的QQ号：772262624 <br>
q = '//*[@class="long"]'
nodes1 = demo.xpath(q)
print(nodes1[0].text)

# 获取元素的属性值
print(nodes[0].get("id"))
print(nodes[0].get("href"))
print(nodes1[0].get("class"))

# 父级定位,继续 .xpath

