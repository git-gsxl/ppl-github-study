'''

                第1课-http协议

一、http：基于请求与响应模式、无状态的应用层协议(tcp/ip)；
  ① http 协议     ② https 协议
  除了这两个还有其他的协议：head、delete、put等

二、例子：http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html
1.协议类型：http
2.host域名：127.0.0.1
3.端口号：81
4.path路径：/zentao/user-login-L3plbnRhby8=.study_html
5.？：分隔符
6.参数：xxx=int
7.多个参数：&

三、请求方式
1.get  2.post
3.Get、post区别：
①get肯定没有请求body，post不一定要有请求body可以为空；
四.请求、响应消息
1.请求行（request line）、请求头部（header）、空行和请求数据四个部分组成。
2.响应：状态行、消息报头、空行和响应正文。

四、fiddler原理
1.原理：作为一个代理，fiddler拦截请求和响应（可篡改请求、响应），如中学时期传情书。
2.设置能看到git、post请求，设置抓https请求；
3.手机设置允许远程连接，默认端口：8888，手机连接同局域网，修改手机代理ip为电脑的IP地址；
4.设置过滤后，需要重启fiddler
5.保存会话为text文件，有问题就先保存下来（右键，Save，as text）
6.设置断点，篡改请求断点、篡改响应返回的断点；

五、如何判断前后端问题
1.先看入参是否正确，如果入参正确说明服务端问题，反之是前端问题；
2.看返回结果，如果是返回结果有问题，那么就是后端问题；


















'''