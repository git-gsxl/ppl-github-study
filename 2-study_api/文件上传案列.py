from requests_toolbelt import MultipartEncoder
import requests

# 登录
s = requests.session()
login_url = 'http://127.0.0.1/zentao/user-login.html'
data = 'account=admin&password=e10adc3949ba59abbe56e057f20f883e&keepLogin%5B%5D=on&referer=http%3A%2F%2F127.0.0.1%2Fzentao%2Fdoc-browse-1-byModule-0-id_desc-doc.study_html'
login_r = s.post(login_url, params=data)  # 传 params 参数

# 断言是否登录成功
r1 = s.get('http://127.0.0.1/zentao/doc-browse-1-byModule-0-id_desc-doc.html')
if '产品主库' in r1.content.decode('utf-8'):
    print('登录成功')
else:print('登录失败')

# 文件上传保存
# 传参数，name 对应 value，注意图片路径的填写。为空的一些参数不影响的去前提下可以删除。
s_url = 'http://127.0.0.1/zentao/doc-create-1-0.html'
body = MultipartEncoder(
    fields=[
        ('lib', '1'),
        ('uid', '5dec436e32b85'),
        ('module', '0'),
        ('title', '我的一个title'),
        ('type', 'text'),
        ('contentType', 'study_html'),
        ('files[]', ('test.png', open('C:\\Users\\Administrator\\Desktop\\test.png', 'rb'), 'image/png'))
    ])
r2 = s.post(s_url, data=body, headers={'Content-Type': body.content_type})      # Content-Type 自动获取

# 检查是否成功上传图片
res = s.get('http://127.0.0.1/zentao/doc-browse-1.html')
if '我的一个title' in res.content.decode('utf-8'):
    print('已上传成功')
else:print('上传失败')
