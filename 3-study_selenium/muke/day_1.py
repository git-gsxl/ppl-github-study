import random

# 批量生成号码、邮箱号进行注册

''' 生成邮箱号 '''
for i in range(5):
    ra = ''.join(random.sample('1234567890', 8))+'.163@.com'
    print(ra)

''' 生成手机号 '''
for i in range(10):
    rb = ''.join(random.sample('1234567890', 8))
    print('137'+rb)

