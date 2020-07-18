from requests_toolbelt import MultipartEncoder
import re, requests

url = 'http://47.104.190.48:8000/xadmin/hello/teacherman/add/'

def add_token(s):
    r = s.get(url)
    try:
        to = re.findall('name="csrfmiddlewaretoken" value="(.+?)"', r.text)
        token = to[0]
        print('成功，add_token值为：%s' % token)
    except:
        print('获取add_token失败：%s' % token)
    return token

def add_data(s, token):
    body = MultipartEncoder(
        fields=[
            ('csrfmiddlewaretoken', token),
            ('csrfmiddlewaretoken', token),
            ('teacher_name', '龙老师'),
            ('tel', '13378896589'),
            ('mail', '13378896589'),
            ('sex', 'M'),
            ('_save', ''),
        ]
    )
    r = s.post(url, data=body, headers={'Content-Type': body.content_type})
    exp_name = ''
    try:
        exp_name = re.findall('update/">(.+?)</a>', r.text)
        print('成功，获取name为：%s' % exp_name[0])
    except:
        print('获取name失败：%s' % exp_name[0])
    return exp_name[0]

if __name__ == '__main__':
    from study.study_api.day_12 import token, login
    s = requests.session()
    b = login(s, token=token(s))
    s.get('http://47.104.190.48:8000/xadmin/')
    d = add_data(s, token=add_token(s))




