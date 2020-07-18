import pytest

@pytest.fixture(scope='session')    # scope='session' 任何文件共享
def setu_login():
    print('\n用例先登录')

@pytest.fixture()
def open_html():
    print('\n打开页面')

    # 后置操作
    yield
    print('\n测试数据最后执行清理')
