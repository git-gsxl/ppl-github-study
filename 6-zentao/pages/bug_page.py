from python_study.zentao.common.base import Base
from python_study.zentao.common.URL import url, dr


class Bug(Base):

    loc_cs = ('link text', '测试')
    loc_bug = ('link text', 'Bug')
    loc_tj = ('id', 'createActionMenu')
    loc_bb = ('css selector', '[class="chosen-choices"]')
    loc_zg = ('xpath', '//*[@id="openedBuild_chosen"]/div/ul/li')
    loc_bt = ('id', 'title')
    frame = ('css selector', '[class="ke-edit-iframe"]')
    loc_sr = ('css selector', '[class="article-content"]')
    loc_bc = ('css selector', '#submit')
    loc_img = ('xpath', '//*[@id="dataform"]/table/tbody/tr[6]/td/div[2]/div[1]/span[18]/span')
    loc_ly = ('xpath', '/study_html/body/div[4]/div[1]/div[2]/div/div[3]/form/div/div')
    loc_qd = ('xpath', '/study_html/body/div[4]/div[1]/div[3]/span[1]/input')

    def bug_tj(self, title='123456', zhengwen='456789'):
        self.click(self.loc_cs)
        self.click(self.loc_bug)
        self.click(self.loc_tj)
        self.click(self.loc_bb)
        self.click(self.loc_zg)
        self.send(self.loc_bt, title)

        # 切换iframe
        f = self.find(self.frame)
        self.driver.switch_to_frame(f)

        self.send(self.loc_sr, zhengwen)


        # 切回
        self.driver.switch_to_default_content()
        self.click(self.loc_img)
        self.click(self.loc_ly)

        # windowns cmd 打开这个exe文件
        import os
        import time
        time.sleep(1)
        png_path = 'G:\\project_lyl\\zentao\\excel_data\\test1.png'
        os.system('G:\\project_lyl\\zentao\\excel_data\\au3_test.exe %s' % png_path)
        time.sleep(1)

        self.click(self.loc_qd)
        self.click(self.loc_bc)

if __name__ == '__main__':
    from study.zentao.pages.login_page import login
    driver = dr()
    driver.get(url())
    t = login(driver)
    t.login()

    b = Bug(driver)
    b.bug_tj()
