import requests

# # get 请求 url + 请求参数
# url = 'http://japi.juhe.cn/qqevaluate/qq?key=03af13597f058c3edd9ebc51cf6e6512&qq=295424589'
#
# r = requests.get(url)
# print(r.status_code)    # 状态码
# print(r.text)           # raw 响应文本
# print(r.headers)        # 响应头部

url = 'http://japi.juhe.cn/qqevaluate/qq'

par = {
    'key': '03af13597f058c3edd9ebc51cf6e6512',
    'qq': '295424589'
}

r = requests.get(url, params=par)
# print(r.status_code)
# print(r.text)
# print(r.headers)            # 字典
# print(r.headers['Date'])
# print(r.json())             # 字典
print(r.content.decode("utf-8"))
