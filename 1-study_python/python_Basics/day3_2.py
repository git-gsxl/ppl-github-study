# 切片对原来的值是不会改变
# # 1、索引
# a = 'ABCDPOM'
# s = a[0]
# s2 = a[2]
# print(s)
# print(s2)

# # 2、取ABC   切片 ： 顾头不顾尾
# a = 'ABCDPOM'
# a1 = a[0:3]
# print(a1)

# # 3、取尾：-1、-2类推
# a = 'ABCDPOM'
# print(a[-1])

# # 4、取全部的三种方式
# a = 'ABCDPOM'
# print(a)
# print(a[:])
# print(a[0:])

# # 5、跳着取值,[首:尾:步长]
# a = 'ABCDPOM'
# print(a[1:6:2])

# # 6、取 DCBA
# a = 'ABCDPOM'
# print(a[3::-1])

# # 7、取 DB
# a = 'ABCDPOM'
# print(a[3::-2])

# 7、倒着取全部，倒着取步长都是负号
a = 'ABCDPOM'
print(a[-1::-1])
print(a[::-1])


