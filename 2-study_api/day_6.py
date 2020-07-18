'''
一、参数
'''
# 1.格式化输出
a = 'good!'
b = 'ok!'
print('hello %s word!%s' % (a, b))

# 2.字典传参
token = 'lylqyq'

h = {
    "a": "13",
    "token": token
}
print(h)


'''
二、参数化关联前取值：
1.上传一个文件，会返回一个文件id，可用正则提取（re）；
2.关联文件id，对该文件进行删除；
3.正则先取到值，再传给下一个需要的；

注意返回的格式是：list，一般用[0]提取值
'''
import requests
import re
url = 'http://japi.juhe.cn/qqevaluate/qq'

par = {
    'key': '03af13597f058c3edd9ebc51cf6e6512',
    'qq': '772262624'
}
r = requests.get(url, params=par)
print(r.url)

# 取中间的值
key = re.findall("\?key=(.+?)&", r.url)        # 提取该key的值
print('我取出来的key为：', key)

# 取最后面的值：$
QQ = re.findall("qq=(.+?)$", r.url)            # 提取该QQ号
print('我取出来的QQ为：', QQ)

# 取最前面的值：^
u = re.findall("^(.+?)\?key", r.url)           # 获取URL
print(u)

'''
三、运用二中取值进行参数化关联
'''
hh = {
    "key": key,
    "qq": QQ
}
r1 = requests.get(url, params=hh)
print('r1.url=:', r1.url)


# 解析 urlencode
from urllib import parse
URL = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&' \
      'wd=%E4%BA%94%E9%99%A9%E4%B8%80%E9%87%91%E8%AE%A1%E7%AE%97%E5%99%A8'

aa = parse.unquote(URL)     # 解析为：五险一金计算器
print(aa)
