
''' 运用 fixtures 定义的顺序 '''
def test_001(setu_login):
    print('\n上面是登录，我现在点击进入home')

def test_002(open_html):
    print('\n没登录，打开html')

def test_003(setu_login, open_html):
    print('\n登录后，打开html')

def test_data(open_html):
    print('测试数据1')

def test_data1(open_html):
    print('测试数据122')