'''

1.Json是一种数据交换格式
2.只有双引号，没有元组

'''

import json

h = {
    'a': 1,
    'b': True,
    'c': (1, 2),
    'd': {'a': '2'},
    'e': [11, 12],
    'f': None
}

# 转为 Json
dict_json = json.dumps(h)     # indent=x 表示前面空多少行
print(type(dict_json))
print(dict_json)

# json 转为 dict
json_dict = json.loads(dict_json)
print(type(json_dict))
print(json_dict)

# 这种类型的 str 转为 json，不是字符串会报错
w = '{"a": None, "b":True}'
d = eval(w)
print(d)
print(type(d))
