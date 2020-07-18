#
# '''
# 数据类型划分：
# 1.可变数据类型：list列表、dcit字典、set集合      不可哈希
# 2.不可变数据类型：元组、bool、int、str           可哈希
#
# dict 字典：
# 1.dict key 必须是不可变数据类型，可哈希
#   value：任意数据类型
# 2.dict优点：二分查找去查询
#             存储大量的关系型数据
#             无序的，通过key查找
# 可哈希：类型猜数字，二分查找。
# '''
#
# # dict 字典
#
# # 1、增
# # 第一种
# dic = {"name": "小龙", "age": 22, "job": "IT"}
#
# dic["high"] = 175   # 没有key时则新增
# dic["age"] = 16     # 有key时，value被覆盖
# print(dic)

# # 第二种
# dic = {"name": "小龙", "age": 22, "job": "IT"}
#
# dic.setdefault('sex', 'man')    # 没有key时则新增
# dic.setdefault('age', '22')     # 有key时，不做任何改变
# print(dic)

# 2、删
# # 第一种
# dic = {"name": "小龙", "age": 22, "job": "IT"}
#
# name = dic.pop('age')       # 按key删除，有返回值
# print(dic)
# print(name)

# 第二种,常用
# dic = {"name": "小龙", "age": 22, "job": "IT"}
# name = dic.pop('sex', '没有key')       # 可设置返回值，避免报错
# print(dic)
# print(name)

# # 第三种清空dict
# dic = {"name": "小龙", "age": 22, "job": "IT"}
# dic.clear()
# print(dic)

# # 第四种，没有返回值
# dic = {"name": "小龙", "age": 22, "job": "IT"}
# del dic['name']
# print(dic)
# del dic         # 删除整个dict

# 3、改
# # 第一种
# dic = {"name": "小龙", "age": 22, "job": "IT"}
# dic['age'] = 18
# print(dic)

# # 第二种 update,覆盖添加
# dic = {"name": "小龙", "age": 22, "like": "IT"}
# dic1 = {"name": "玲玲", "age": 18, "job": "大宝剑"}
# dic1.update(dic)
# print(dic)
# print(dic1)

# # 4、查
# dic = {"name": "小龙", "age": 22, "like": "IT"}
# print(dic['name'])                                  # 查看name对应的value，没有找到会报错
# print(dic.get('name1', '没有这个value'))           # 可设置返回值，推荐
# print(dic.keys())       # key
# print(dic.values())     # value
# print(dic.items())      # 元组的键值
dic = {"name": "小龙", "age": 22, "like": "IT"}
for i in dic:           # 默认打印 key
    print(i)

for i in dic.values():  # 打印value
    print(i)

for i in dic.items():   # 打印元组的每一个键值对
    print(i)

for k, v in dic.items():   # 打印去掉元组的每一个键值对
    print(k, v)
#
#
#
# # 面试题
# # a = 1
# # b = 2
# # # 用一行代码使a=b,b=a,并打印
# # a, b = b, a
# # print(a, b)
#
#
