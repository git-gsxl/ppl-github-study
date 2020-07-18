from selenium import webdriver

def url():
    '''url=" " '''
    # host = 'http://127.0.0.1:81/'   # 81端口
    # # host = 'http://127.0.0.1/'
    # test_url = host + 'zentao/user-login-L3plbnRhby8=.study_html'

    test_url = 'http://127.0.0.1:81/zentao/user-login.html'
    return test_url

def dr():
    '''dr = webdriver.Chrome()'''           # 普通模式
    driver = webdriver.Chrome()
    return driver


# def dr():
#     '''dr = webdriver.Chrome()'''           # 静默模式
#     option = webdriver.ChromeOptions()
#     option.add_argument('headless')
#     driver = webdriver.Chrome(chrome_options=option)
#     return driver
