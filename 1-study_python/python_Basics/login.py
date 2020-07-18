# 注册
while 1:
    user = input("请输入你的手机号进行注册:")
    pwd1 = input('请设置你的登录密码:')
    pwd2 = input('请再次输入设置登录的密码:')
    if pwd1 == pwd2:
        with open('user', 'w', encoding='utf-8') as f:
            f.write('%s\n%s' % (user, pwd1))
        print('恭喜您：%s 账号注册成功！' % user)
        break
    elif pwd1 != pwd2:
        print('两次输入的密码不一致，请重新输入')
# 三次机会登录
lis = []
count = 3
while 1:
    u = input('请输入你的账号：')
    p = input('请输入你的密码：')
    # 读取账号密码
    with open('user', 'r+', encoding='utf-8') as user_pwd:
        for i in user_pwd:
            lis.append(i)
    if u == lis[0].strip() and p == lis[1].strip():
        print('登录成功')
        break
    else:
        if count == 0:
            print('你的密码已被锁定')
            break
        else:
            print('账号或密码错误，剩余%s次机会' % count)
            count = count - 1

