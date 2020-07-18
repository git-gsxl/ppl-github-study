'''

一、安装部署环境
1.下载地址：https://jenkins.io/zh/
2.运行安装后，打开127.0.0.1:8080，如果长时间提示：Please xxxxx to work...，就把 hudson.model.UpdateCenter.xml 里面的URL替换为：http://mirror.xmission.com/jenkins/updates/update-center.json
3.下载推荐插件，可翻墙不翻墙，失败的可后面再添加。
4.节点管理：
5.定时构建五个参数：*****
H/5 * * * *（每5分钟执行一次）
H 2 * * * （每天2:00执行一次）
H H/2 * * * （每2小时执行一次）
①第一个参数代表的是分钟 minute，取值 0~59；
②第二个参数代表的是小时 hour，取值 0~23；
③第三个参数代表的是天 day，取值 1~31；
④第四个参数代表的是月 month，取值 1~12；
⑤第五个参数代表的是星期 week，取值 0~7，0 和 7 都是表示星期天。

二、linux部署(docker)
https://www.cnblogs.com/gsxl/p/12129333.html
'''