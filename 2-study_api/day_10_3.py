from requests_html import HTMLSession

session = HTMLSession()
url = 'http://699pic.com/tupian/photo-fengjing.html'
r = session.get(url)

r.html.render()         # 渲染html

a = r.html.xpath('.//img[@class="lazy"]')
print(a)

for i in a:
    try:
        img_url = i.attrs['data-original']      # 取它的 url
        print(img_url)
        title = i.attrs['title']                 # 取它的命名
        print(title)
        with open(title+'.jpg', 'wb') as fp:    # 下载图片
            r_jpg = session.get(img_url)
            fp.write(r_jpg.content)
    except Ellipsis as msg:                      # 抛异常，打印出错误日志
        n = 1
        print('失败第%s次为:%s' % (n, str(msg)))
        n += 1




