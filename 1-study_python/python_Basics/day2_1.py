
# # 1、格式化输出
# name = input('请输入您的名字')
# age = input('请输入您的年龄')
# job = input('请输入您的工作')
#
# msg = '我叫%s，今年%s岁，我的工作是%s行业' % (name, age, job)
# print(msg)

# # 2、%s 字符串类型str、%d 数字类型int
# name = input('请输入您的名字')
# age = int(input('请输入您的年龄'))
# job = input('请输入您的工作')
# msg = '''
# name : %s
# age : %d
# job : %s
#  ''' % (name, age, job)
# print(msg)

# # 3、% 占位符，格式化里面也有70%等百分号会导致报错，我们加个转义%即可
# name = input('请输入您的名字')
# age = input('请输入您的年龄')
# job = input('请输入您的工作')
#
# msg = '我叫%s，今年%s岁，我的工作是%s行业，70%%业绩是我开创的！' % (name, age, job)
# print(msg)

count = 6
while count < 5:
    count += 1
    if count == 3:
        break
    print(count)

else:
    print("循环出现异常！！！")
