import requests


url = 'http://www.baidu.com/'   # 乱码


r = requests.get(url)
print(r.status_code)
print(r.text)
print(r.headers)
print(r.content.decode('utf-8'))    # decode 自动解码编码格式


url1 = 'http://japi.juhe.cn/qqevaluate/qq'
par = {
    'key': '03af13597f058c3edd9ebc51cf6e6512',
    'qq': '295424589'
}
r = requests.get(url1, params=par)

# 1.response的返回内容还有其它更多信息

print(r.status_code)            # 响应状态码
print(r.content)                # 字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
print(r.headers)                # 以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
print(r.json())                 # Requests中内置的JSON解码器 ,json转成python的字典了
print(r.url)                    # 获取url
print(r.encoding)               # 编码格式
print(r.cookies)                # 获取返回的cookie
print(r.text)                   # 字符串方式的响应体，会自动根据响应头部的字符编码进行解码
print(r.raise_for_status())     # 失败请求(非200响应)抛出异常
print(r.history)                # 查看重定向记录
print(dict(r.cookies))          # 将jar的cookise转化为字典
print(r.content.decode('utf-8'))  # utf-8格式打印
