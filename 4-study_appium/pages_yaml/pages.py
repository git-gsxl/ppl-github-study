# -*- coding: utf-8 -*-
from python_study.study_appium.pages_yaml import tools
pages = tools.pages_yaml()
def get_locater(clazz_name, method_name):
    locators = pages[clazz_name]['locators']
    for locator in locators:
        if locator['name'] == method_name:
          return locator

class Mypage:
    删除订单 = get_locater('Mypage', '删除订单')
    提交订单 = get_locater('Mypage', '提交订单')
    
class QiTapage:
    我的 = get_locater('QiTapage', '我的')
    我的_出行 = get_locater('QiTapage', '我的_出行')
    
class qitaMypage:
    qita_删除订单 = get_locater('qitaMypage', 'qita_删除订单')
    qita_提交订单 = get_locater('qitaMypage', 'qita_提交订单')
    

if __name__ == '__main__':
    print(qitaMypage.qita_删除订单)