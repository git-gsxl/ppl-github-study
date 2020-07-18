'''

2，python历史。

	宏观上：python2 与 python3 区别：
		python2 源码不标准，混乱，重复代码太多，
		python3 统一 标准，去除重复代码。
3，python的环境。

	编译型：一次性将所有程序编译成二进制文件。
		缺点：开发效率低，不能跨平台。
		优点：运行速度快。
		：C，C++等等。

	解释型：当程序执行时，一行一行的解释。
		优点：开发效率高，可以跨平台。
		缺点：运行速度慢。
		:python ,php,等等。

6，变量。
	变量：就是将一些运算的中间结果暂存到内存中，以便后续代码调用。
	1,必须由数字，字母，下划线任意组合，且不能数字开头。
	2，不能是python中的关键字。
	['and', 'as', 'assert', 'break', 'class', 'continue',
	'def', 'del', 'elif', 'else', 'except', 'exec',
	'finally', 'for', 'from', 'global', 'if', 'import',
	'in', 'is', 'lambda', 'not', 'or', 'pass', 'print',
	'raise', 'return', 'try', 'while', 'with', 'yield']
	3，变量具有可描述性。
	4,不能是中文。


9，用户交互。input
   1，等待输入，
   2，将你输入的内容赋值给了前面变量。
   3，input出来的数据类型全部是str
'''

a = 1        # int
b = '1'      # str
c = True     # bool:布尔值

print(a, type(a))
print(b, type(b))
print(c, type(c))