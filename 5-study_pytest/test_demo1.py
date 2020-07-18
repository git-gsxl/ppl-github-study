class Test_api():
    ''' pytest不需要用初始化，直接写用例 '''

    def test_a(self):
        a = 1
        print('\n我是用例：a')       # pytest -s 显示打印内容
        assert a > 0

    def test_b(self):
        b = 1
        print('\n我是用例：b')
        assert b < 2, '失败原因：b 不小于 0'
