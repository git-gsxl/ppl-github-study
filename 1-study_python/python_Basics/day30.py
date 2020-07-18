'''
一、hashlib：md5加密，提供摘要算法的模块。
不管算法多么不同，摘要的功能始终不变。
对于相同的字符串使用同一个算法进行摘要，得到的值总是不变的。
使用不同算法对相同的字符串进行摘要，得到的值应该不同。
不管使用什么算法，hashlib的方式永远不变。
'''
# import hashlib
# md5=hashlib.md5()
# md5.update(b'gsxl')
# print(md5.hexdigest())

'''
加密作用：
1、密码的密文存储
2、文件的一致性验证
    在下载的时候 检查我们下载的文件和远程服务器上的文件是否一致
    两台机器上的两个文件 你想检查这两个文件是否相等
'''
# 注册账号时加密密码，写入文件
# import hashlib
# user=input('输入你注册的账号：')
# passwd=input('设置你的密码：')
# with open(r'G:\Python_projects\python_study\study\study_python\python_Basics\userinfo','a')as f:
#     md5=hashlib.md5()
#     md5.update(bytes(passwd,encoding='utf-8'))
#     f.write(user+'|')
#     f.write(md5.hexdigest())
#     f.write('\n')
#
# # 登录账号时读取密码与输入密码进行对比，正确就登录成功。
# user_name=input('登录账号：')
# password=input('登录密码：')
# use=''
# pwd=''
# with open(r'G:\Python_projects\python_study\study\study_python\python_Basics\userinfo')as f:
#     for i in f:
#         i=i.strip()
#         use,pwd=i.split('|')
# if user_name==use:
#     md5=hashlib.md5()
#     md5.update(bytes(password,encoding='utf-8'))
#     md5_pwd = md5.hexdigest()
#     if user_name == use and md5_pwd == pwd:
#         print('登录成功')
#     else:print('账号或密码错误！')
# else:print('账号不存在！')

# # 3、md5可动静态加盐，提高安全性
# import hashlib
# md5=hashlib.md5(bytes('gsxl',encoding='utf-8')+b'123456')
# md5.update(b'123456')
# print(md5.hexdigest())


'''
二、logging模块
能够“一键”控制
排错的时候需要打印很多细节来帮助我排错
严重的错误记录下来
有一些用户行为 有没有错都要记录下来
'''
# 1、logging五个级别：
# import logging
# logging.debug('debug--低级别')             # 低级别排错信息
# logging.info('info--正常信息')             # 正常信息
# logging.warning('warning--警告信息')      # 警告信息
# logging.error('error--错误信息')          # 错误信息
# logging.critical('critical--严重错误')   # 高级别严重错误信息


# 2、实例
# %a, %d %b %Y %H:%M:%S
# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s'
#                            '[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',)
# try:
#     int(input('请输入你的密码：'))
# except ValueError:
#     logging.error('pwd_type error')

# basicconfig 简单 能做的事情相对少
    # 中文的乱码问题
    # 不能同时往文件和屏幕上输出

'''
一、logging.  basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有：
filename：用指定的文件名创建FiledHandler，这样日志会被存储在指定的文件中。
filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
format：  指定handler使用的日志显示格式。
datefmt： 指定日期时间格式。
level：   设置rootlogger（后边会讲解具体概念）的日志级别
stream：  用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件(f=open(‘test.log’,’w’))，默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。

二、format参数中可能用到的格式化串：
%(name)s            Logger的名字
%(levelno)s         数字形式的日志级别
%(levelname)s       文本形式的日志级别
%(pathname)s        调用日志输出函数的模块的完整路径名，可能没有
%(filename)s        调用日志输出函数的模块的文件名
%(module)s          调用日志输出函数的模块名
%(funcName)s        调用日志输出函数的函数名
%(lineno)d          调用日志输出函数的语句所在的代码行
%(created)f         当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d     输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s         字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d          线程ID。可能没有
%(threadName)s      线程名。可能没有
%(process)d         进程ID。可能没有
%(message)s         用户输出的消息
'''

# 3、定制化logging
# 能写入中文了
import logging
log = logging.getLogger()                             # 实例化一个对象
f = logging.FileHandler('py.log', encoding='utf-8')  # 文件句柄
h = logging.StreamHandler()                           # 创建一个控制台对象句柄
format_f=logging.Formatter(                           # 输出格式
    '%(asctime)s %(filename)s''[line:%(lineno)d] %(levelname)s %(message)s')
f.setFormatter(format_f)                              # 给f传一个格式化输出对象
h.setFormatter(format_f)                              # 给h传一个格式化输出对象
log.addHandler(f)                                     #
log.addHandler(h)

logging.debug('debug--低级别')             # 低级别排错信息
logging.info('info--正常信息')             # 正常信息
logging.warning('warning--警告信息')      # 警告信息
logging.error('error--错误信息')          # 错误信息
logging.critical('critical--严重错误')   # 高级别严重错误信息

