from flask import Flask, url_for, request, render_template, redirect, Response, jsonify
from werkzeug.routing import BaseConverter

app = Flask(
    __name__, )


class PhoneConverter(BaseConverter):
    # 自定义数据长度类型：phone
    regex = r'1[345789]\d{9}'


class ListConverter(BaseConverter):

    def to_python(self, value):
        # 拼接url
        return value.split('+')

    def to_url(self, value):
        # 反拼接url
        return '+'.join(value)


'''
class JsonResponse(Response):
    # 自定义响应json对象
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, dict):
            response = jsonify(response)
        return super(JsonResponse, cls).force_type(response, environ)
app.response_class = JsonResponse                    # 自定义响应json对象
'''

app.config.from_pyfile('config.py', silent=True)  # 加载config文件

# 1、自定义处理数据
app.url_map.converters['phone'] = PhoneConverter
app.url_map.converters['list'] = ListConverter


# 2、动态传参：<xx>，必须对应参数
@app.route('/list/<phone:user_phone>/')
def user(user_phone):
    # 访问：http://127.0.0.1:5000/list/18777568589
    return 'user phone：%s' % user_phone


# 3、拼接url
@app.route('/posts/<list:boards>/')
def posts(boards):
    return '你提交的模板是：%s' % boards


# 4、反拼接url
@app.route('/')
def for_url():
    print(url_for('posts', boards=['a', 'b', 'c']))
    return 'for url'


# 5、login：GET/POST请求
@app.route('/login/', methods=['GET', 'POST'])
def login():
    context = {
        'biaoti': '请先登录',
        'title': '广深小龙',
        'id': {
            'name': 'gsxl',
            'age': 18,
            'kg': '55kg'
        },
        'num': -9,
        'qianming': '',
    }
    if request.method == 'GET':
        return render_template('login.html', **context)
    else:
        return 'success'


# 6、重定向
@app.route('/profile/')
def profile():
    if request.args.get('name'):
        # http://127.0.0.1:5000/profile/?name=asd
        return '个人中心页面'
    else:
        return redirect(url_for('login'))


# 7、自定义响应信息
@app.route('/list2/')
def list2():
    # res = Response(response='hello', status=200, content_type='text/html; charset=utf-8')
    return 'hello list2', 200, {'token': 'asdasdasdadasdasd'}


# 8、返回json格式数据
@app.route('/list3/')
def list3():
    return {'name': 'gsxl', 'age': 24}


# 9、返回html
@app.route('/html/')
def my_html():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=9090,
    )
