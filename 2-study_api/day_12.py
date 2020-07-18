# coding:utf-8
from lxml import etree

def token(s):
    url = 'http://47.104.190.48:8000/login'
    r = s.get(url)
    xlml = etree.HTML(r.text)
    token = ''
    try:
        nodes = xlml.xpath('//*[@name="csrfmiddlewaretoken"]')
        token = nodes[0].attrib['value']
        print('成功，token值为：%s' % token)

    except:
        print('token值获取失败：%s' % token)

    return token

def login(s, user='test', pwd='123456', token=''):
    url = "http://47.104.190.48:8000/login_test/"
    h ={"Content-Type": "application/x-www-form-urlencoded"}
    body = {
        "username": user,
        "password": pwd,
        "csrfmiddlewaretoken": token,
    }

    r = s.post(url, headers=h, data=body)

     # 如果.text出现乱码
    # print(r.content.decode("utf-8"))
    return r.content.decode("utf-8")

def home(s):
    url = 'http://47.104.190.48:8000/xadmin/'
    r = s.get(url)
    return r.text

if __name__ == "__main__":
    import requests
    s = requests.session()
    b = login(s, 'test', '123456', token(s))
    print(b)
    # d = s.get('http://47.104.190.48:8000/xadmin/')


