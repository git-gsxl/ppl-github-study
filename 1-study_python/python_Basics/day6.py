'''
集合：可变的数据类型，但元素必须是不可变的数据类型，无序不重复，既可哈希
不可变数据类型：元组、bool、int、str     可哈希
'''

# set1 = {1, 2, 3, (True, False)}
# print(type(set1))

# 增
# # 1、add，无序的，随机
# set1 = {'tian', '小龙'}
# set1.add('long')
# print(set1)


# # 2、update
# set1 = {'tian', '小龙'}
# set1.update('ab')
# print(set1)

# 1、pop()删除
# set1 = {'tian', '小龙', 'xiao'}
# print(set1.pop())         # 随机删除,有返回值
# print(set1)

# # 2、remove 按元素删除
# set1 = {'tian', '小龙', 'xiao'}
# set1.remove('tian')
# print(set1)

# # 3、清空
# set1 = {'tian', '小龙', 'xiao'}
# set1.clear()
# print(set1)

# # 4、del 删除，没有返回值
# set1 = {'tian', '小龙', 'xiao'}
# del set1

# 没有改

# 查
# set1 = {4, 5, 6, 7, 8}
# set2 = {12, 1, 5, 7, 9}
# print(set1 & set2)          # 交集
#
# print(set1 | set2)          # 并集，去重
#
# print(set1 ^ set2)          # 反交集
#
# print(set1 - set2)          # 差集

# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# print(set1 < set2)          # 子集，set1 是 set2的子集
# print(set2 > set1)          # 超集，set2 是 set1的超集

#
# # 将列表的数字去重复，不能改变原来的列表的类型。
# li = [1,2,33,33,2,1,4,5,6,'a','a']
# # 将列表转换为集合，集合再转回列表即可
# s = set(li)
# print(list(s))

# 去重一步到位
li = []
s = frozenset([1,2,33,33,2,1,4,5,6,'a','a'])
print(s, type(s))
for i in s:
    li.append(i)
print(li)