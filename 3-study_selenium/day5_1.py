import unittest
# unittest用例框架

# def add(a, b):
#     c = a+b
#     return c
class TestAdd(unittest.TestCase):

    # def test_add(self):
    #     r = add(2, 4)   # 测试数据，2+4 实际结果=6
    #     exp = 6         # 期望结果
    #     self.assertEquals(r, exp)

    def test_add2(self):
        q = '123'
        w = '123'
        e = '123456'
        r = '88888'

        self.assertEquals(q, w)    # q == w
        # self.assertTrue(q == w)  # q == w
        # self.assertTrue(q in e)  # q 匹配 e
        # self.assertIn(q, e)      # q 匹配 e



if __name__ == "__main__":
    unittest.main()

