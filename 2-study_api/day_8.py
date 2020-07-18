import unittest
import requests

url = 'http://japi.juhe.cn/qqevaluate/qq'

par = {
    'key': '03af13597f058c3edd9ebc51cf6e6512',
    'qq': '772262624'
}


class TestAdd(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()
        self.s.verify = False

    def tearDown(self):
        self.s.close()

    def test_001(self):
        r = self.s.get(url, params=par)
        res = r.text
        exp = '看准方向就坚持到底'
        self.assertIn(exp, res)             # 期望结果 在 实际结果里面


    def test_002(self):
        r = self.s.get(url, params=par)
        res = r.json()['reason']
        # print(res)
        exp = 'success'
        self.assertEqual(exp, res)          # 期望结果 等于 实际结果


    def test_003(self):
        r = self.s.get(url, params=par)
        res = r.json()['reason']
        # print(res)
        exp = 'success'
        self.assertTrue(exp == res)         # # 期望结果 等于 实际结果

if __name__ == '__main__':
    unittest.main()
