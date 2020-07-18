from study.study_api.day_12 import login, token, home
import requests, re
from requests_toolbelt import MultipartEncoder

s = requests.session()
b = login(s, token=token(s))
home(s)
b = s.get('http://47.104.190.48:8000/xadmin/hello/uploadimage/')

token = re.findall('hidden" name="csrfmiddlewaretoken" value="(.+?)">', b.text)
print('上传图片token为：', token[0])

h = {"Content-Type": "multipart/form-data", }

body = MultipartEncoder(
    fields=[
        ("csrfmiddlewaretoken", token[0]),
        ("csrfmiddlewaretoken", token[0]),
        ("name", "今晚我分手了"),
        ("image", (u"1.png", open("C:\\Users\\Administrator\\Desktop\\1.png", "rb"), "image/png")),
        ("_save", ""),
        ("add_time_0", "2019/09/06"),
        ("add_time_1", "23:00"),
        ("initial-add_time_0", "2019/09/06"),
        ("initial-add_time_1", "23:00"),
    ]
)

url = 'http://47.104.190.48:8000/xadmin/hello/uploadimage/add/'
bb = s.post(url, data=body, headers={'Content-Type': body.content_type})
print(bb.text)


