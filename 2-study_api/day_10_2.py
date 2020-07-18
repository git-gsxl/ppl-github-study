from requests_html import HTMLSession

session = HTMLSession()

url = 'https://www.baidu.com'
r = session.get(url)

# xpath 获取，可查找任意标签、元素值等
t = r.html.xpath('//*[@id="su"]')
# print(t)                            # xpaht 获取element所有元素属性
# for i in t:
#     print(i.text)                   # 文本内容
#     print(i.absolute_links)         # html内容
#     print(i.attrs)
#     print(i.attrs['id'])

# CSS语法
t1 = r.html.find('#su')
print(t1)
for i in t1:
    print(i.text)
    print(i.absolute_links)
    print(i.attrs['id'])

# {} 取中间
t2 = r.html.xpath('//*[@id="su"]')      # list 对象
a = t2[0].search("value='{}一下'")      # 取中间,切割
print(a)

