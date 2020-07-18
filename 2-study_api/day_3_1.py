import requests

# 忽略https出现的报红色警告
import urllib3
urllib3.disable_warnings()

s = requests.session()
s.verify = False

url = 'https://adm_t.maijju.com/appweb/login/loginIn'

# fiddler抓包下来的 请求头部
h = {
'Host': 'adm_t.maijju.com',
'Connection': 'keep-alive',
'Content-Length': '74',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Origin': 'https://adm_t.maijju.com',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Referer': 'https://adm_t.maijju.com/',
"Accept-Encoding": "gzip, deflate, br",
'Accept-Language': 'zh,zh-CN;q=0.9,en;q=0.8',
'Cookie': 'com.session.id=bcbbc447-5c01-49f6-8bfd-ef1a5e62ee8d; fromUrl=https://adm_t.maijju.com/#/; user=',
}

# fiddler抓包下来的 请求参数
body = {
'username': 'admin',
'password2': 'tKd0Se12Kjy6vDU9tf3GCA==',
'captcha': '',
'loginType': '0',
}

# 要注意该请求是 get 还是 post
r = s.post(url, headers=h, data=body)  # verify=False 不然会报错，忽略https报错

res = r.json()['msg']       # json格式，取里面 msg 的值

assert '登录成功！' == res   # 断言


# h1 = {
# 'Content-Type': 'application/json'
# }
#
#
# data1 = {"strBeginDate": "", "strEndDate": "", "dstName": "", "phone": "", "remarksInfo": "", "page": '1', "pageSize": '10', "field": "", "lifting": ""}
# url1 = 'https://adm_t.maijju.com/appweb/exchangeYundou/selectGiveYundouList'
# r1 = s.post(url1, headers=h1, json=data1, verify=False)
# print(r1.text)
