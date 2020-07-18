'''
一、异常处理
BaseException           所有异常的基类
SystemExit              解释器请求退出
KeyboardInterrupt       用户中断执行(通常是输入^C)
Exception               常规错误的基类
StopIteration           迭代器没有更多的值
GeneratorExit           生成器(generator)发生异常来通知退出
StandardError           所有的内建标准异常的基类
ArithmeticError         所有数值计算错误的基类
FloatingPointError      浮点计算错误
OverflowError           数值运算超出最大限制
ZeroDivisionError       除(或取模)零 (所有数据类型)
AssertionError          断言语句失败
AttributeError          对象没有这个属性
EOFError                没有内建输入,到达EOF 标记
EnvironmentError        操作系统错误的基类
IOError                 输入/输出操作失败
OSError                 操作系统错误
WindowsError            系统调用失败
ImportError             导入模块/对象失败
LookupError             无效数据查询的基类
IndexError              序列中没有此索引(index)
KeyError                映射中没有这个键
MemoryError             内存溢出错误(对于Python 解释器不是致命的)
NameError               未声明/初始化对象 (没有属性)
UnboundLocalError       访问未初始化的本地变量
ReferenceError          弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError            一般的运行时错误
NotImplementedError     尚未实现的方法
SyntaxError Python      语法错误
IndentationError        缩进错误
TabError                Tab 和空格混用
SystemError             一般的解释器系统错误
TypeError               对类型无效的操作
ValueError              传入无效的参数
UnicodeError            Unicode 相关的错误
UnicodeDecodeError      Unicode 解码时的错误
UnicodeEncodeError      Unicode 编码时错误
UnicodeTranslateError   Unicode 转换时错误
Warning                 警告的基类
DeprecationWarning      关于被弃用的特征的警告
FutureWarning           关于构造将来语义会有改变的警告
OverflowWarning         旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning 关于特性将会被废弃的警告
RuntimeWarning          可疑的运行时行为(runtime behavior)的警告
SyntaxWarning           可疑的语法的警告
UserWarning             用户代码生成的警告
AttributeError      试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
IOError             输入/输出异常；基本上是无法打开文件
ImportError         无法引入模块或包；基本上是路径问题或名称错误
IndentationError    语法错误（的子类） ；代码没有正确对齐
IndexError          下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError            试图访问字典里不存在的键
KeyboardInterrupt   Ctrl+C被按下NameError 使用一个还未被赋予对象的变量
SyntaxError         Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError           传入对象类型与要求的不符合
UnboundLocalError   试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
ValueError          传入一个调用者不期望的值，即使值的类型是正确的
ArithmeticError
AssertionError
AttributeError
BaseException
BufferError
BytesWarning
DeprecationWarning
EnvironmentError
EOFError
Exception
FloatingPointError
FutureWarning
GeneratorExit
ImportError
ImportWarning
IndentationError
IndexError
IOError
KeyboardInterrupt
KeyError
LookupError
MemoryError
NameError
NotImplementedError
OSError
OverflowError
PendingDeprecationWarning
ReferenceError
RuntimeError
RuntimeWarning
StandardError
StopIteration
SyntaxError
SyntaxWarning
SystemError
SystemExit
TabError
TypeError
UnboundLocalError
UnicodeDecodeError
UnicodeEncodeError
UnicodeError
UnicodeTranslateError
UnicodeWarning
UserWarning
ValueError
Warning
ZeroDivisionError
'''
# 1、抛异常，ValueError
# try:
#     res = int(input('请输入您的手机号码：'))
# except ValueError:print('手机号码输入有误，请重新输入！')

# 2、IndexError
# try:
#     res = [][1]
# except IndexError:print('超出了列表最大长度')

# 3、Exception
# try:
#     res = [][1]
#     ret = {}
#     ret['k']
# except Exception as error:print('抛出了万能异常', error)

# 4、接else，既无异常会执行
# try:
#     res = int(input('请输入您的手机号码：'))
# except ValueError:print('手机号码输入有误，请重新输入！')
# else:print('手机号码正确！')

# 5、finally：不管有没有异常我都会继续执行
# try:
#     res = int(input('请输入您的手机号码：'))
# except ValueError:print('手机号码输入有误，请重新输入！')
# else:print('手机号码正确！')
# finally:print('不管有没有异常我都执行')

# finally的好处举例：
# 函数中用得比较多，做收尾工作，不管你怎么执行打开文件，最后finally都给你关闭文件close
# def func():
#     try:
#         f = open('test')
#         # f.close()           # 关闭文件
#         return True
#     except:
#         # f.close()           # 关闭文件
#         return False
#     finally:f.close()       # finally都会给你关闭文件close

