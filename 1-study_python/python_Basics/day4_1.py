
# # 列表的嵌套
# li = ['xiaolong', '小林', ['小龙', 'xiaol'], '咯']
# print(li[1][1])                 # 取li列表下标1的 下标1元素
# li[0] = li[0].capitalize()      # li列表下标0改为首字母大写
# print(li)
#
# li[1] = '小龙龙'                # li列表下标1重新赋值
# print(li)


# li = ['xiaolong', '小林', ['小龙', 'xiaol'], '咯']
# print(li[1].replace('小', '龙'))   # 1、替换，将li下标1的 小 替换为 龙
#
# li[1] = li[1].replace('小', '龙')  # 2、替换，将li列表下标1的 小 替换为 龙
# print(li)
#
# li[2][1] = li[2][1].upper()        # 3、全大写
# print(li)

# # 元组，只读列表，可循环查询，可切片。
# # 儿子不能改，孙子可能可以改
# tu = (1, 2, 'asd', [3, 'xiaolong', '小龙'], 'aiyi')
# tu[3][0] = '5'     # 改的是元组里面的列表
# print(tu)
#
# print(tu[0:3])      # 切片后是元组
# for i in tu:        # 查
#     print(i)

# # 元组嵌套列表，里面的列表可以改
# tu = (1, 2, 'asd', [3, 'xiaolong', '小龙'], 'aiyi')
# tu[3][1] = tu[3][1].upper()     # 元组里的列表1下标改为全大写
# print(tu)
#
# tu[3].append('sb')              # 元组里的列表新增一个：sb
# print(tu)

# jojn
# s = '545645611'
# s1 = " ".join(s)                # 每个元素有个空格，可设置其它
# print(s1)

# # 列表转换成字符串 join()，字符串转为列表用切割 split()
# li = ['xiaolong', '小林', '咯']
# s = '+'.join(li)
# print(s)
# print(type(s))

# range，python range() 函数可创建一个整数列表，一般用在 for 循环中。
for i in range(0, 11, 2):           # 顺序
    print(i)

for i in range(10, -1, -2):         # 倒序
    print("第二个:", i)


# # 练习。打印每一个值
# li = (1, 2, 'asd', [3, 'xiaolong', '小龙'], 'aiyi')
# for i in li:
#     if type(i) == list:
#         for k in i:
#             print(k)
#     else:
#         print(i)






