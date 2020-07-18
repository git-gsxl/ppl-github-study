
# content = input(">>>")
# con = content.split('+')
# print(content)
# print(con)
#
# num = 0
# for i in con:
#     num += int(i)
# print(num)


# content = input('>>>').strip()
# index = content.find('+')
# a = int(content[0: index])
# b = int(content[index+1:])
# print(content)
# print(a)
# print(b)


# s = input('>>>')
# count = 0
# for i in s:
#     if i.isdigit():
#         count += 1
# print(count)


# 1、列表的增删改查

# 一、增
# li = ['XL', [3, 2, 1], '小龙', 'aiya', 'lushen']
# print(li[0])

# 取列表里面的列表值
# print(li[1])
# print(li[1][0])

# 取前两个
# print(li[0:2])

# append 增
# li = ['XL', [3, 2, 1], '小龙', 'aiya', 'lushen']
# li.append('FPX')
# print(li)

# 例子
# while 1:
#     username = input('>>>')
#     if username.lower().strip() == 'q':
#         break
#     else:
#         li.append(username)
# print(li)

#
# # 2、insert 指定下标插入
# li = ['XL', [3, 2, 1], '小龙', 'aiya', 'lushen']
# li.insert(0, 'FPX')
# print(li)

# 3、元素迭代,int无法迭代
# li = ['XL', [3, 2, 1], '小龙', 'aiya', 'lushen']
# li.extend('小龙')
# print(li)
#
#
# # 二、删
# # 1、pop 删除
# li = ['XL', [3, 2, 1], '小龙', 'aiya', 'lushen']
# name = li.pop(2)   # 有返回值
# name1 = li.pop()    # 默认删除最后一个
# print(name)
# print(li)
#
# # 2、remove：按元素清除
# li = ['XL', [3, 2, 1], '小龙', 'aiya', 'lushen']
# li.remove('小龙')
# print(li)

# # 3、clear：清空
# li = ['XL', [3, 2, 1], '小龙', 'aiya', 'lushen']
# li.clear()
# print(li)

# # 4、切片删除
# # del li
# li = ['XL', [3, 2, 1], '小龙', 'aiya', 'lushen']
# del li[0:3]
# print(li)

# 三、修改
# # 1、下标直接赋值修改
# li = ['XL', [3, 2, 1], '小龙', 'aiya', 'lushen']
# li[0] = '男人'
# print(li)

# # 2、切片会迭代处理
# li = ['XL', [3, 2, 1], '小龙', 'aiya', 'lushen']
# li[1:2] = '123456'
# print(li)

# # 传列表
# li = ['XL', [3, 2, 1], '小龙', 'aiya', 'lushen']
# li[1:3] = ['后裔', '鲁班']
# print(li)

# 四、查
# li = ['XL', [3, 2, 1], '小龙', 'aiya', 'lushen']
# for i in li:
#     print(i)
# print(li[0:2])

# 公共方法
li = ['XL', [3, 2, 1], '小龙', 'aiya', 'lushen']
l = len(li)                   # 长度
print(l)
num = li.count('小龙')        # 统计某个元素总数
print(num)
print(li.index('小龙'))       # index 索引找下标

# # int 正反向排序
# # li = [1,5,6,2,8,7,9]
# # li.sort()             # 正向排序
# # print(li)
# #
# # li = [1,5,6,2,8,7,9]  # 反向排序
# # li.sort(reverse=True)
# # print(li)
# #
# # # 反转
# # li = [1,5,6,2,8,7,9]
# # li.reverse()
# # print(li)

