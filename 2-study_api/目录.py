'''
day_1:    http协议简介及fiddler环境；
day_2:    get简单请求；
day2_1:   get简单请求自动解码编码格式，返回内容；
day2_2:   请求头部、body；
day_3:    post请求类型格式；
day_3_1:  简单MJJ登录案列, json转换取里面的值为断言；
day_4:    cookies讲解、Session关联讲解；
day_5:    格式转换讲解；
day_5_1:  json讲解；
day_5_2:  取值案列；
day_6:    参数、正则取值参数化关联（可用切割）、解析urlencode；
day_7:    unittest框架；
day_8:    unittest框架api常用断言方法；
day_9:    report生成html测试报告，可邮件发报告；
day_10:   lxml解析html，类似爬虫找id、token或其他的值；
day_10_1：requests_html库,set集合
day_10_2：requests_html库,xpath、CSS获取值
day_10_3：requests_html库,案列渲染html
day_11  ：参数化与封装,ddt数据驱动
day_12  ： lxml实战获取token
day_12_1： multipart/form-data表单提交案例
day_12_2： unittest表单提交案例
day_12_3： 文件上传案列

建议底层封装：
①切换环境的Host  ②re获取token   ③数据库连接操作


注意：
1.链接带参数就用params = {}
2.显示有json就用：json = {}
3.没有显示json就用：data = {}
头部：headers=h
全局设置：s.verify=False
html中的动态token用xlml 或者 re库获取
'''