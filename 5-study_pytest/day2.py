'''
allure报告：
一、环境搭建：
1.pip install allure-pytest
2.插件下载：https://github.com/allure-framework/allure2/releases
3.解压插件后，bin目录添加至环境变量

二、运行pytest生成allure报告：
1.生成原始文件需带路径：pytest --alluredir ./report/allure_raw
2.渲染原始文件：allure serve report/allure_raw

'''