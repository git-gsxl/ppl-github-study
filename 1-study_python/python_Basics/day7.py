





# 一、只读
# # 1、r：str方式读，编码：UTF-8
# # bytes --》 str
# f = open('1.txt', 'r', encoding="UTF-8")
# c = f.read()
# print(c)
# f.close()
#
# 2、rb：bytes方式读，非文字的文件
# f = open('1.txt', 'rb')
# c = f.read()
# print(c)
# f.close()

# 二、只写
# # 1、w：写入，没有此文件是创建，有此文件会清空源文件再写
# f = open('log', 'w', encoding="utf-8")
# f.write('abc小龙abc')
# f.close()

# 2、wb：写入，没有此文件是创建，有此文件会清空源文件再写
# f = open('log1', 'wb')
# f.write('abc小龙abc'.encode("utf-8"))     # 以utf-8编码格式，写入东西
# f.close()

# # 3、a：追加写入
# f = open('log1', 'a', encoding="utf-8")
# f.write('abc小龙abc')
# f.close()

# 三、读写,常用：r+
# 1、先读再写，写了不能再读
# f = open('log', 'r+', encoding="utf-8")
# f.seek(0)
# print(f.read())
# f.write('小哥哥谈恋爱吗？我偷老公的钱养你')
# f.close()

# # 2、先写再读，不推荐
# f = open('log', 'r+', encoding="utf-8")
# f.write('小哥哥谈恋爱吗？我偷老公的钱养你')
# print(f.read())
# f.close()

# 3、r+b
# f = open('log', 'r+b')
# f.write('小哥哥谈恋爱吗？我偷老公的钱养你'.encode("utf-8"))
# print(f.read())
# f.close()


