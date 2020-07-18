'''
day1：python简介
day2：if、while语句练习题
day2_1：格式化输出
day3：str 常用操作方法与format格式化输出
day3_1:数据结构与类型转换
day3_2：字符串索引与切片
day4：列表的增删改查
day4_1：列表、元组嵌套
day5：字典的增删改查
day5_1：字典的嵌套
day6：集合增删查
day7：文件操作
day8：初识函数
day8_1：命名空间和作用域
day8_2：函数嵌套和作用链
day9：装饰器/完美装饰器
day10：装饰器进阶，带参数、调用多个装饰（俄罗斯套娃）
day11：迭代器
day12：生成器及生成器进阶
day13：生成器表达式和列表等各种推导式
day14： 内置函数和匿名函数
day15： 初识递归函数与算法
day16： re模块
day17： 其他常用模块 collections/time模块
day18： 其他常用模块 random/os/sys模块
day19： 三种序列化
day20： 模块导入
day21： 异常处理
day22： 初识面向对象与类
day23： 类的组合与初识继承
day24： 继承进阶
day25： 接口类与抽象类
day26： 多态与初识封装
day27： 封装进阶与property装饰器函数、类方法、静态方法
day28：反射、isinstance、issubclass
day29：几个内置方法
day30：md5加密：hashlib、日志模块logging
day31：初识socket与struct
day32：struct模块定制报头ftp实战
day33：hmac的检验客户端合法性和socketserver模
'''

'''
3、元素分类
    有如下值li= [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}


'''
# li= [11,22,33,44,55,66,77,88,99,90]
# da = []
# xo = []
# dic = {}
#
# for i in li:
#     if i>66:
#         da.append(i)
#     elif i<66:
#         xo.append(i)
#     else: continue
# print(da)
# print(xo)
# dic.setdefault('k1',da)
# dic.setdefault('k2',xo)
# print(dic)

'''
4、输出商品列表，用户输入序号，显示用户选中的商品
    商品 li = ["手机", "电脑", '鼠标垫', '游艇']
要求：1：页面显示 序号 + 商品名称，如：
      	1 手机
	   	2 电脑
     		 …
     2： 用户输入选择的商品序号，然后打印商品名称
  3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
4：用户输入Q或者q，退出程序。

'''
# flag = True
# while flag:
#     li = ["手机", "电脑", "鼠标垫", "游艇"]
#     for i in li:
#         print('{}\t\t{}'.format(li.index(i)+1,i))
#     num_of_chioce = input('请输入选择的商品序号/输入Q或者q退出程序：')
#     if num_of_chioce.isdigit():
#         num_of_chioce = int(num_of_chioce)
#         if num_of_chioce > 0 and num_of_chioce <= len(li):
#             print(li[num_of_chioce-1])
#         else:print('请输入有效数字')
#     elif num_of_chioce.upper() == 'Q':break
#     else:print('请输入数字')

# while 1:
#     li = ["手机", "电脑", "鼠标垫", "游艇"]
#     for i in li:
#         print(li.index(i)+1, i)
#     code = input('请输入选择的商品序号/输入Q或者q退出程序：')
#     if code.upper() == 'Q':break
#     elif code.isdigit():
#         code = int(code)
#         if code>0 and code<=len(li):
#             print(li[code-1])
#         else:
#             print('请输入有效数字')
#     else:
#         print('请输入数字')
