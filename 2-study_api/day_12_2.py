import unittest, requests
from study.study_api.day_12 import login, token, home
from study.study_api.mysql import dle_sql
from study.study_api.day_12_1 import add_token, add_data

class Test_tj(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        login(cls.s, user='test', pwd='123456', token=token(cls.s))
        cls.b = home(cls.s)
        if '后台页面' in cls.b:
            print('已进入首页')
        else:
            print('进入首页失败')

    @classmethod
    def tearDownClass(cls):
        sql = "delete from hello_teacher where teacher_name='龙老师';"
        dle_sql(sql)
        cls.s.close()

    def setUp(self):
        sql = "delete from hello_teacher where teacher_name='龙老师';"
        dle_sql(sql)

    def test_001(self):
        res = add_data(self.s, add_token(self.s))
        exp = '龙老师'
        self.assertEqual(res, exp)



