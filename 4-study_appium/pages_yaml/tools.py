
import yaml
import os
import jinja2

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

def get_page_list(yamlpage):
    page_object = {}
    for page, names in yamlpage.items():
        loc_names = []
        # 获取loctors定位方法
        locs = names['locators']
        # 添加定位name到列表
        for loc in locs:
            loc_names.append((loc['name']))
        page_object[page] = loc_names
    return page_object

def creat_pages_py(pagelist):
    '''
    function：用jinja2把 templetpage 模板生成的pages.py文件
    args：传get_pages_list返回内容
        eg:
        'Mypage': {'desc': '订单模块', 'locators': [{'name': '删除订单', 'by': 'xpath', 'value': 'com.taobao.taobao:id/tab_title'}
    '''
    print(os.path.join(base_path, 'templetpage'))
    template_loader = jinja2.FileSystemLoader(searchpath=base_path)
    template_env = jinja2.Environment(loader=template_loader)
    templateVars = {'page_list': pagelist}
    template = template_env.get_template('templetpage')
    with open(os.path.join(base_path, 'pages.py'), 'w', encoding='utf-8')as f:
        f.write(template.render(templateVars))


if __name__ == '__main__':
    all = pages_yaml()
    page_list = get_page_list(all)
    print(page_list)
    creat_pages_py(page_list)
