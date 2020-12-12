"""
一、初识算法
    1.算法是什么？
        ①数据结构和算法是一名程序员必备的基本功
        ②算法是独立存在的一种解决问题的方法与思想
        ③能够让我们开发效率提高/程序性能提高(写着少而又高质量的代码)
"""

# 1.如果a+b+c=1000，且a^2+b^2=c^2（a,b,c均为自然数），求出所有的可能组合？

# 正常解法：枚举法，每一个数去试
# import time
#
# start_time = time.time()
# for a in range(1001):
#     for b in range(1001):
#         for c in range(1001):
#             if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
#                 print(a, b, c)
# end_time = time.time()
# print('times：%s' % (end_time - start_time))

# 分析改动后
import time

start_time = time.time()
for a in range(1001):
    for b in range(1001):
        c = 1000 - (a + b)
        if a ** 2 + b ** 2 == c ** 2:
            print(a, b, c)
end_time = time.time()
print('times：%s' % (end_time - start_time))


"""
所消耗的时间从小到大

O(1) < O(logn) < O(n) < O(nlogn) < O(n2) < O(n3) < O(2n) < O(n!) < O(nn)
"""