'''
一、模块导入
顺序：①内置模块；②扩展模块；③自定义模块
import后做的事情：
1.modules里查找是否存在模块，存在即被导入，否则sys.path依次查找模块,找到导入，否则找不到调用时会报错
2.创建这个模块的命名空间
3.把文件的名字放到命名空间
'''
# # 1、import后导入的模块直接被执行
# import test

# # 2、模块起别名
# import test as t
# print(t.f())

# # 起别名的好处例子：提高兼容性，调用的时候全用：db.xxx
# if db == 'mysql':
#     import pymysql as db
# elif db == 'sqlsv':
#     import sqlsv as db
# else:import nodb db

# 3、modules 里是被导入的模块，path是python的环境变量
# import sys
# print(sys.modules.keys())
# print(sys.path)


# 4、form导入,根据sys.path找
# time 将不能使用,可以import多个
# from time import sleep,time,gmtime
# sleep(1)
# print(gmtime())

# # 4、import * 不推荐用
# from time import *
# sleep = 1           # 万一方法与变量命名重复会报错
# sleep(1)

'''
所有的模块导入都应该尽量往上写
    内置模块
    扩展模块
    自定义模块
模块不会重复被导入 ： sys.moudles
从哪儿导入模块 : sys.path
import
import 模块名
    模块名.变量名 和本文件中的变量名完全不冲突
import 模块名 as 重命名的模块名 ： 提高代码的兼容性
import 模块1，模块2

from import
from 模块名 import 变量名
    直接使用 变量名 就可以完成操作
    如果本文件中有相同的变量名会发生冲突
from 模块名 import 变量名字 as 重命名变量名
from 模块名 import 变量名1，变量名2
from 模块名 import *
    将模块中的所有变量名都放到内存中
    如果本文件中有相同的变量名会发生冲突
from 模块名 import * 和 __all__ 是一对
    没有这个变量，就会导入所有的名字
    如果有all 只导入all列表中的名字
__name__
在模块中 有一个变量__name__，
当我们直接执行这个模块的时候，__name__ == '__main__'
当我们执行其他模块，在其他模块中引用这个模块的时候，这个模块中的__name__ == '模块的名字'
'''