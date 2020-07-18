
# # 1、首个字母大写
# s = 'xiao long'
# s1 = s.capitalize()
# print(s1)


# # 2、全大写、全小写
# s = 'xiao long'
# s2 = s.upper()
# s21 = s.lower()
# print(s2)
# print(s21)

# # 3、不区分大小写写法
# s = 'xiao long'
# s_str = 'ABcd'
# p = input('请输入验证码，不区分大小写：')
# if s_str.upper() == s_str.upper():
#     print('验证码正确！')
# else:
#     print('验证码错误，请重新输入')

# # 4、大小写对换，如A换为a，b换为B
# s = 'Ab'
# s3 = s.swapcase()
# print(s3)

# # 5、有间隔（特殊字符或数字隔开）的首字母大写
# s = 'xiao long'
# s4 = s.title()
# print(s4)

# # 6、居中，空白填充
# s = 'xiao long'
# s5 = s.center(20, '-')
# print(s5)

# # 7、len，查看长度
# s = 'xiao long'
# print(len(s))

# # 8、find 通过元素找索引，找到返回下标，找不到返回-1
# s = 'xiao long'
# s1 = s.find('l')
# print(s1)

# 9、index,通过元素找索引，找到返回下标，找不到报错
# s = 'xiao long'
# s1 = s.index('i')
# print(s1)

# 10、默认前后去空格,可用来输入账号时有空格可以剔除做到无影响。
# s = '   xiao long    '
# s1 = s.strip()
# print(s1)

# # 11、统计某个元素数量
# s = 'xiao long'
# s1 = s.count('o')
# print(s1)

# # 12、切割,左右分割 str ---> list
# s = 'xiao long'
# s1 = s.split(' ')
# print(s1)

# # format 三种玩法
# msg = '我叫{}，今年{}，工作行业{}'.format('小龙', '22', 'IT')
# print(msg)

# msg = '我叫{1}，今年{0}，工作行业{2}'.format('22', '小龙', 'IT')
# print(msg)

# msg = '我叫{name}，今年{age}，工作行业{job}'.format(age=22, name='小龙', job='IT')
# print(msg)

# 13、替换
# s = '123asd2'
# s1 = s.replace('2', '二')
# s2 = s.replace('2', '二', 1)     # 1 表示替换 1个，有序的。
# print(s1)
# print(s2)

# is系列  用来判断某些地方输入的数据类型是否对应
s = '123asd2'
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())


# for 有限循环
# s = '123asd2'
# for i in s:
#     if '3' in i:
#         print(i)
