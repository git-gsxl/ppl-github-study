
h = {"a": "a",
        "da": [{"data": "2019-04-05", "city": "广州"}, {"data": "2019-04-04", "city": "佛山"}]
        }

a = h['da']                 # 拿到“da”
print(a)

e = len(a)                  # 查询多少个list
print(e)

b = a[0]['data']           # 取值data=2019-04-05
print(b)

c = a[1]['data']           # 取值data=2019-04-04
print(c)

# 不知道len的个数取值
for i in a:
    if i['data'] == '2019-04-05':
        print(i)
        print(i['city'])
    else:
        print('没有这个参数')
