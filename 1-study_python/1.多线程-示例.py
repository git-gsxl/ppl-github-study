'''
多线程跑注册:
'''
import random
from threading import Thread

_phone = ''     # 声明全局变量，让能拿到返回值： global _phone

def func(s):
    global _phone
    _phone = '137'+''.join(random.sample('1234567890', 8))

    # 注册的接口参数
    url = 'http://www.xxx.com/userx/loginOneByPhonePwd'
    data = {
            "phone": _phone,
            "pwd": "123456", }

    # res = s.post(url, json=data)
    # if '注册成功' in res.text:
    #     return phone
    # else:return 'ERROR phone：%s' % phone
    return _phone

if __name__ == '__main__':
    import time
    import requests

    s_time = time.time()
    s = requests.session()
    f = open('../../phone.txt', 'w')

    for i in range(10000):
        thread = Thread(target=func, args=(s,))
        thread.start()
        f.write(_phone + '\n')

    end_time = time.time() - s_time
    print(end_time)


