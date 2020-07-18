
# 功能讲解
# f = open("log", "r+", encoding="utf-8")
# a = f.read()        # 默认读全部
# print(a)
# f.seek(6)           # 按照字节指定光标开始读位置
# c = f.read(6)       # 指定读 N 个字符
# print(c)
# f.close()

# # 追加 小龙女，调节光标获取后面的9个字节
# f = open("log", "a+", encoding="utf-8")
# f.write('小龙女')
# count = f.tell()     # 查看光标的位置
# f.seek(count-9)      # 按照字节指定光标开始读位置
# c = f.read()
# print(c)
# f.close()

#
# f = open("log", "a+", encoding="utf-8")
# f.seek(0)
# # c = f.readline()     # 一行一行读
# d = f.readlines()   # 每行当成一个列表，添加到list中
# # print(c)
# print(d)
# f.close()

# f.truncate(5)       # 截取多少个字符


# 推荐：with 不用 close 关闭,可读多个
# a = open('log', "r+", encoding="utf-8")
# b = open('log', "r+", encoding="utf-8")
# with a as f, b as f1:
#     print(f.read())
#     print(f1.read())



# 修改文件实战（实则新增文件）
f = open('log1', encoding='utf-8')
f1 = open('log1.bak', 'w+', encoding='utf-8')

with f, f1:
    for i in f:
        if '欣欣' in i:
            i = i.replace('欣欣', '小龙')  # 更改为小龙
        f1.write(i)                         # 写入f1文件中

import os
os.remove('log1')                   # 删除源文件
os.rename('log1.bak', 'log1')      # 更改文件名称


