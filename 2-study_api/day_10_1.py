from requests_html import HTMLSession

session = HTMLSession()
url = 'https://www.baidu.com'
r = session.get(url)
# print(r.content.decode('utf-8'))
# print(r.text)
all = r.html.links                 # 获取相对路径所有链接
print(all)

abs = r.html.absolute_links        # 获取绝对路径所有链接
print(type(abs))                   # 这叫 set 集合，交集、并集等，一般用法：去重
