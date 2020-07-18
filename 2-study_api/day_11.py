'''
一、参数化与封装
1.参数化，定义函数、传什么值，封装api、用例进行调用；
2.ddt数据驱动，也可以表格驱动，一般user、pwd、exp；
表格驱动需要调用封装好的类，列如：表格与ddt测试数据一致的；

'''
import requests, ddt, unittest

# ddt数据驱动所需准备的数据
test_data = [
    {'account': 'admin', 'pwd': '123465', 'exp': 'admin'},
    {'account': 'gsxl', 'pwd': '123321', 'exp': 'gsxl'},]

# 类需要ddt装饰器
@ddt.ddt
class Test_xl(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()
        self.s.verify = False

    def tearDown(self):
        self.s.close()

    @ddt.data(*test_data)   # 某个用例需要用到ddt的测试数据
    def test_001(self, data):
        # print('ddt测试数据是：%s' % data)
        user = data['account']
        pwd = data['pwd']
        exp = data['exp']
        print('这是账号：', user)
        print('这是密码：', pwd)
        print('这是期望结果：', exp)

if __name__ == '__main__':
    unittest.main()                 # 告诉解释器我是用unittest运行的!!!






# # 登录
# s = requests.session()
# login_url = 'http://127.0.0.1/zentao/user-login.html'
# pr = {
#     'account': 'admin',
#     'password': '123456',
# }
# login_r = s.post(login_url, params=pr)  # 传 params 参数
#
# # 断言是否登录成功
# r1 = s.get('http://127.0.0.1/zentao/doc-browse-1-byModule-0-id_desc-doc.html')
# if '产品主库' in r1.content.decode('utf-8'):
#     print('登录成功')
# else:print('登录失败')
