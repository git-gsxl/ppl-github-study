
'''
yaml支持的三种数据结构：
1.键值对（dict字典）
2.数组（dict/字典、list/列表）
3.纯量（字符串、布尔值、整数、时间日期）
'''

import yaml
import os

def read_page_loctor(pagename='Mypage', locname='分类按钮'):
    cur_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))     # 当前目录
    ymPath = os.path.join(cur_path, "mypage.yaml")                              # 文件名称
    f = open(ymPath, "r", encoding='utf-8')                                 # 打开文件
    cfg = f.read()                                                           # 读取文件
    f.close()                                                                # 关闭文件
    a = yaml.load(cfg, Loader=yaml.FullLoader)                               # 读取yaml文件，转为字典，忽略警告：Loader=yaml.FullLoader

    for i in a[pagename]['locators']:
        if i['name'] == locname:
            return i

if __name__ == '__main__':
    print(read_page_loctor())
