'''
一、collections 模块
在内置数据类型（dict、list、set、tuple）的基础上，collections模块还提供了几个额外的数据类型：Counter、deque、defaultdict、namedtuple和OrderedDict等。

1.namedtuple: 生成可以使用名字来访问元素内容的tuple
2.1 queue:队列先进先出
2.2 deque: 双端队列，可以快速的从另外一侧追加和推出对象
3.OrderedDict: 有序字典
4.defaultdict: 带有默认值的字典
5.Counter: 计数器，主要用来计数
'''
# 1、namedtuple 生成可以使用名字来访问元素内容的tuple
# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y', 'z'])
# p = Point(1, 6, 5)
# print(p.x)
# print(p.y)
# print(p.z)
# print(p)

# 2、queue: 队列先进先出
# import queue
# q = queue.Queue()
# q.put(10)
# q.put(4)
# q.put(6)
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())      # 最后取不到一直在等待，直到有新的值进来
# print(q.qsize())     # 查看还有多少个值可以取

# 3、dueue双端队列，可以快速的从另外一侧追加和推出对象
# from collections import deque
# dq = deque([2, 3])
# dq.append(4)          # 从后面放数据
# dq.appendleft(1)      # 从前面放数据
# dq.insert(4, 5)       # index插入数据
# print(dq)
# print(dq.pop())       # 从后面取数据
# print(dq.popleft())   # 从前面取数据
# print(dq)

# 4、OrderedDict的Key是有序的
# from collections import OrderedDict
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# print(od['a'])
# for k in od:
#     print(od[k])

# 5、defaultdict，实例，将大于55放入k1，否则放入k2
# from collections import defaultdict
# values = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# my_dict = defaultdict(list)
# for value in values:
#     if value>55:
#         my_dict['k1'].append(value)
#     else:
#         my_dict['k2'].append(value)
# print(my_dict)

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
# from collections import defaultdict
# d = defaultdict(lambda: 5)
# print(d['k'])

# Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）。Counter类和其他语言的bags或multisets很相似。
# from collections import Counter
# c = Counter('zz')
# print(c)


'''
二、time模块
python当中，和时间有关系的通常用time模块有这三种方式：
1.格式化的时间字符串
2.时间戳
3.结构化时间，元组()

%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''

# 1、strftime:格式化的时间字符串:年月日 时间
# import time
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(time.strftime('%Y-%m-%d %H:%M'))
# print(time.strftime('%Y-%m-%d'))
# print(time.strftime('%H:%M'))
#
# # 2、时间戳:time.time()
# import time
# print(time.time())
#
# # 3、localtime:结构化时间，元组()
# import time
# loc_time = time.localtime()
# print(loc_time)
# print(loc_time.tm_year)

# 时间转换
# 1、时间戳转换结构化时间转换
# import time
# t = time.time()
# print(time.localtime(t))
# print(time.gmtime(t))
#
# # 2、结构化时间转换转换时间戳
# import time
# q = time.localtime()
# print(time.mktime(q))
#
# # 3、字符串格式化时间转换结构化时间
# import time
# print(time.strptime('2020.3.8', '%Y.%m.%d'))
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(3500000000)))
#
# asctime、ctime转换
import time
print(time.asctime())   # 结构化时间转字符串格式化时间Sun Mar  8 22:27:26 2020
print(time.ctime())     # 时间戳转字符串格式化时间： Sun Mar  8 22:27:26 2020


