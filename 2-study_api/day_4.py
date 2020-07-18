'''
一、cookies讲解，有如下特点：

1·保存在客户端，一般由浏览器负责存储在电脑本地。

2·通常是加密存储的，不过由于存储在本地，很难保证数据不被非法访问，并不怎么安全，
所以cookies中不宜保存敏感信息，如密码等。

3·哪些信息需要保存作为cookie保存在客户端本地，保存多长时间，一般是由服务器（开发）决定的，
所以HTTP协议中通过服务器返回的响应报文头中，有一个Set-Cookie域来指示浏览器或者其他客户端，在本地保存cookie信息。

4·cookie保存在客户端本地的目的是为了下次访问网站的时候可以直接取出来，上送服务器，
所以HTTP协议中通过客户端发送给服务器的请求报文头中，有一个cookies域专门用于存放这个信息，
以便客户端将cookie信息发送给服务器。

cookise在哪？
1. cookies在返回url上
2. cookie藏在返回内容里
3. cookies在返回的头部
(类似token，就像登录一个app，不能直接用里面的聊天功能，因为还没有登录，而接口就是没有登录的token)

二、Session“会话”
1.session：与Cookies将数据保存在客户端本地不同的是，Session的数据保存在服务器端，一般放在服务器的内存里。
s = requests.session()
s 为上下文管理,相当于保存前面的会话，请求带上 s 就行了

'''

# import re
# import requests
# s = requests.session()
#
# # 禅道登录
# url = 'http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html'
# par = 'account=admin&password=e10adc3949ba59abbe56e057f20f883e&keepLogin%5B%5D=on&referer=%2Fzentao%2F'
# r = s.post(url, params=par)
#
# # 查需求的 kuid 接口
# r2 = s.get('http://127.0.0.1:81/zentao/story-close-2.html?onlybody=yes')
# b = r2.content.decode('utf-8')
# kuid = re.findall('kuid = "(.+?)"', b)     # 注意编码格式，否则乱码
# print('获取的kuid为：%s' % kuid[0])        # kuid[0]则是提供下一个接口关联的参数
#
# # 关闭需求，%s 格式化输出，关联上面接口获取的kuid
# url = 'http://127.0.0.1:81/zentao/story-close-4.html?onlybody=yes'
# par1 = 'closedReason=done&duplicateStory=&childStories=&comment=&uid=%s' % kuid[0]
# print(par1)
# r3 = s.post(url, params=par1)



import re
st = "我是一只小小鸟，怎么飞也飞不高？"

# 取前，逗号前面的全部。
s = re.findall('^(.+?)，', st)
print(s[0])


# 取中间“小鸟”,取出来的是list。
# s = re.findall('小(.+?)，', st)
# print(s[0])


