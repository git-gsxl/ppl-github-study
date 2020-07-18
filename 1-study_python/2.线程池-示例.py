'''
线程池跑注册:
'''
import random
from concurrent.futures import ThreadPoolExecutor


def func(s):
    phone = '137'+''.join(random.sample('1234567890', 8))

    # 注册的接口参数
    url = 'http://restyl.maijju.com/services/userx/loginOneByPhonePwd'
    data = {
            "phone": phone,
            "pwd": "123456", }

    # res = s.post(url, json=data)
    # if '注册成功' in res.text:
    #     return phone
    # else:return 'ERROR phone：%s' % phone
    return phone

if __name__ == '__main__':
    import time
    import requests

    s_time = time.time()
    s = requests.session()
    f = open('../../phone.txt', 'w')

    tp = ThreadPoolExecutor()               # 默认为计算机本身的cpu个数
    for i in range(10000):
        t = tp.submit(func, s)              # 提交异步任务执行
        f.write(t.result() + '\n')
    tp.shutdown()                           # 相当于close+join：关闭接受任务
    f.close()

    end_time = time.time() - s_time
    print(end_time)


