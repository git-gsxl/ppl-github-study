from python_study.zentao.common.base import Base

class login(Base):

    loc_user = ('css selector', '#account')
    loc_pwd = ('css selector', '[type="password"]')
    loc_login = ('css selector', '#submit')
    res = ('css selector', '#userMenu')

    def send_user(self, user = 'admin'):
        self.send(self.loc_user, user)

    def send_pwd(self, pwd = '123456'):
        self.send(self.loc_pwd, self.loc_pwd)

    def click_login(self):
        self.click(self.loc_login)

    def login(self, user='admin', pwd='123456'):
        self.send(self.loc_user, user)
        self.send(self.loc_pwd, pwd)
        self.click(self.loc_login)

    def res_text(self):
        '''获取登录名'''
        try:
            text = self.get_text(self.res)
        except:
            text = ''
        return text

if __name__ == '__main__':
    from python_study.zentao.common.URL import url, dr
    driver = dr()
    driver.get(url())
    b = login(driver)
    b.login()
    import time
    time.sleep(3)
    aa = b.res_text()
    time.sleep(1)
    print(aa)
    time.sleep(2)
