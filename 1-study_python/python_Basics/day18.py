'''
一、random：随机数模块
'''
# import random
# print(random.random())                          # 大于0且小于1之间的小数
# print(random.uniform(1, 3))                     # 大于1小于3的小数
# print(random.randint(1, 5))                     # 大于等于1且小于等于5之间的整数
# print(random.randrange(1, 10, 2))               # 大于等于1且小于10之间的奇数
# print(random.randrange(2, 11, 2))               # 大于等于2且小于等于10之间的偶数
# print(random.choice([1, '23', [4, 5]]))         # 1或者23或者[4,5])
# print(random.sample([1, '23', [4, 5]], 2))      # 列表元素任意2个组合,返回的个数为函数的第二个参数



# 自动生成6位随机验证码
# import random
# def v_code():
#
#     code = ''
#     for i in range(6):
#         num = random.randint(0, 9)
#         alf = chr(random.randint(65, 90))
#         add = random.choice([num, alf])
#         code = "".join([code, str(add)])
#     return code
#
# print(v_code())


'''
二、OS模块
python的 os 模块提供了非常丰富的方法用来处理目录文件
'''
import os
print(os.getcwd())                       # 获取当前目录
# os.chdir('..')                           # chdir()相当于 cd
# print(os.curdir)                         # 当前目前，相当于 .
# os.mkdir('dirname')                     # 创建单个目录
# os.makedirs('dirname1/dirname2')       # 创建多层目录
# os.rmdir('dirname')                     # 删除单个空目录，若目录不为空则无法删除会报错
# os.removedirs('dirname1')               # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.listdir('dirname')                   # 列出指定目录下的所有文件,并以列表方式打印
# os.remove('path')                       # 删除一个文件
# os.rename("oldname", "newname")        # 重命名文件/目录
# os.stat('path/filename')               # 获取文件/目录信息
# os.system("bash command")              # 运行dos/shell命令，直接显示
# os.popen("bash command").read()        # 运行dos/shell命令，获取执行结果
# os.path.abspath(path=os.getcwd())       # 返回path规范化的绝对路径
# os.path.split(os.getcwd())              # 将path分割成目录和文件名二元组返回
# os.path.dirname(os.getcwd())            # 返回path的目录。其实就是os.path.split(path)的第一个元素
# os.path.realpath(__file__)              # 获取当前的目录
# os.path.basename(os.getcwd())           # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
# os.path.exists(os.getcwd())             # 如果path存在，返回True；如果path不存在，返回False
# os.path.isabs(os.getcwd())              # 如果path是绝对路径，返回True
# os.path.isfile(os.getcwd())             # 如果path是一个存在的文件，返回True。否则返回False
# os.path.isdir(os.getcwd())              # 如果path是一个存在的目录，则返回True。否则返回False
# os.path.join('dirname1', 'dirname2')  # 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.getatime(os.getcwd())           # 返回path所指向的文件或者目录的最后访问时间
# os.path.getmtime(os.getcwd())           # 返回path所指向的文件或者目录的最后修改时间
# os.path.getsize(os.getcwd())            # 返回path的大小
# print(os.sep)                           # 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
# print(os.linesep)                       # 输出当前平台使用的行终止符，win下为"\r\n",Linux下为"\n"
# print(os.pathsep)                       # 输出用于分割文件路径的字符串 win下为;,Linux下为:
# print(os.name)                          # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'

'''
三、sys模块
'''
import sys

# print(sys.path)             # python模块目录路径(python环境变量)
# print(sys.path.clear())     # 清空python模块环境变量
# print(sys.version)          # 获取当前 python 版本信息
# print(sys.platform)         # 获取系统版本(不准确的)
# print(sys.argv)             # 命令行参数list
# print(sys.exit(0))          # 参数0正常退出，1异常退出

# import sys
# res_arvg = sys.argv
# name = res_arvg[1]
# pwd = res_arvg[2]
# print(type(name), name, type(pwd), pwd)
# if name == 'gsxl' and pwd == '123456':
#     print('登录成功！')
# else:print('账户或密码错误！！！')
