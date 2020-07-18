# 一、列表推导式与生成器表达式
# 1、正常使用for循环：
# for i in range(10):
#     print('表白：%s'% i)

# 2、列表推导式：
# ret = ['表白：%s' % i for i in range(10)]
# print(ret)

# 1、生成器表达式
# g = ('表白：%s' % i for i in range(10))
# print(g)                            # 拿到的是：生成器
# print('我是next：%s' % next(g))    # 可用next一个一个取值，相当于 __next__ 方法。
# print('我是__next__：%s' % g.__next__())
# for i in g:
#     print(i)

# 2、生成器实列，如我们春节在家里做汤圆，加入面粉足量的情况下，你家里做了100个家人们一起能吃完吗？
# 显然是不可能那么快的，那么我们在家里就是这样做：先做20个吃完，再做，吃完再做，是不是很像生成器呢？
# 面粉 = ('面粉做汤圆：%s' % i for i in range(10))
# print(面粉)
# for 汤圆 in 面粉:
#     print(汤圆)

# 列表推导式 与 生成器表达式 对比：
'''
1、括号不一样，列表、元组。
2、返回值不一样，表达式几乎不占用内存
'''

# 3、完整推导式，if 判断过滤，类似筛选功能

# 如1:把 100 以内能被5整除的数
# g = [i for i in range(100) if i % 5 == 0]
# print(g)

# 如2:把 100 以内能被5整除的数，再乘以 2
# g = [i*2 for i in range(100) if i % 5 == 0]
# print(g)

# 3、多层嵌套的推导式，先for外面层次，一层一层for。
# names = [['xiag', 'ee', 'asde', 'asde'],
#      ['mina', 'andy', 'asdee', 'jenkinse']]
# ret = [name for lists in names for name in lists if name.count('a') >= 1]
# print(ret)


# 字典推导式
# 将 key 和 value 对调,变为{'23': 'a', '55': 'bb'}
# dic = {'a': '23', 'bb': '55'}
# ret = {dic[i]: i for i in dic}
# print(ret)

# 集合推导式，自带去重功能
# g = {'a', '23', 'bb', 'a'}
# ret = {i for i in g}
# print(ret)

# 二、各种推导式
# 1.推导式接if条件，筛选过滤功能：
# t = ['1ad', 'eeee', 'asd', 'asde']
# ret = [i for i in t if i.count('e') >= 1]
# print(ret)

# 2.嵌套列表筛选过滤：
# 先for循环大列表，再for循环小列表，不建议多次for循环，出错难排查。
# names = [['1ad', 'eeee', 'asd', 'asde'],
#          ['liqu', 'xiaee', 'lisi', 'zsan']]
# ret = [name for lst in names for name in lst if name.count('e') >= 1]
# ret = (name for lst in names for name in lst if name.count('e') >= 1)  改为生成器只需改变括号
# print(ret)

# 3.字典推导式 待续···（本地电脑已学习，未提交代码上git）
# 例一：将一个字典的key和value对调,{666:'XL' , 996:'you'}
# data = {'XL': 666, 'you': 996}
# data_vk = {data[k]: k for k in data}
# print(data_vk)

# 例二：合并大小写对应的value值，将k值统一改为小写
# mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# #{'a':10+7,'b':34,'z':3}
# mcase_frequency = {k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase}
# print(mcase_frequency)

# 集合推导式，自带去重功能
res = {x**2 for x in [1, -1, 2, -2, 3]}
print(res)
