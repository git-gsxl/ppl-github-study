'''

1.第一种：application/json： {“key1“:”value1”,“keyt2":“value2"}
json=

2.第二种：application/x-www-form-urlencoded：name1=
data=

3.第三种：multipart/form-data:这一种是表单格式的
data=


4. Content-Type:octets/stream （文件下载）
data=

5.text/xml
data=


1.链接带参数就用params = {}
2.显示有json就用：json = {}
3.没有显示json就用：data = {}

'''

import requests

url = 'http://japi.juhe.cn/qqevaluate/qq'

par = {
    'key': '03af13597f058c3edd9ebc51cf6e6512',
    'qq': '772262624'
}

r = requests.get(url, params=par)   # URL带参数就用 params, 没有带参数就用 data
print(r.text)               # 通过返回的结果来断言
res = r.json()['reason']    # 实际结果
exp = 'success'             # 期望结果

# assert res == exp         # 1.此断言能抛异常

if res == exp:              # 2.python基础语法断言
    print('测试通过')
else:
    # pass
    print('测试不通过')


