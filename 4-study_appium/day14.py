
'''
yaml模板生成库：jinja2
三种语法：
1.控制结构：{%xxx%}
2.变量取值：{{xxx}}
3.注释：{#xxx#}

'''

import yaml
import os

base_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))  # 当前目录

def pages_yaml(yamlPath=base_path):
    pagesElements = {}
    for fpath, dirname, fnames in os.walk(yamlPath):
        for fname in fnames:
            yaml_file_path = os.path.join(fpath, fname)
            if ".yaml" in str(yaml_file_path):
                with open(yaml_file_path, "r", encoding="utf-8") as f:
                    page = yaml.load(f, Loader=yaml.FullLoader)
                    pagesElements.update(page)
    return  pagesElements

if __name__ == '__main__':
    all = pages_yaml()
    print(all)
    print(all['Mypage'])
    print(all['Mypage']['locators'])

