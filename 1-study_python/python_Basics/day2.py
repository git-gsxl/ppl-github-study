
# # 1.使用 while 循环输出 1 2 3 4 5 6 8 9 10
# count = 0
# while count < 10:
#     count += 1
#     if count == 7:
#         continue
#     print(count)

# 2.求1-100的所有数之和
# conut = 1
# sum = 0
# while conut <= 100:
#     sum = conut + sum
#     conut += 1
# print(sum)

# 3.输出 1-100 内所有的奇数 和 偶数
# conut = 1
# while conut <=100:
#     if conut % 2 == 0:
#         print('偶数：', conut)
#     elif conut % 2 == 1:
#         print('奇数：', conut)
#     conut += 1

# 4.求1-2+3-4+5-6...99所有数的和
conut = 1
sum = 0
while conut < 100:
    if conut % 2 == 0:
        sum = sum - conut
    else:
        sum = sum + conut
    conut += 1
print(sum)

# 5.用户登录（三次机会重试）
# count = 0
# while count < 4:
#     username = input('请输入您的账号：')
#     password = input('请输入您的密码：')
#     a = 3 - int(count)
#     if username == 'gsxl' and password == '123':
#         print('登录成功！')
#         break
#     else:
#         if a != 0:
#             print('登录失败，剩余%s次机会' % a)
#         elif a == 0:
#             print('您的密码已被锁定，请于24小时候再试！！！')
#     count += 1


