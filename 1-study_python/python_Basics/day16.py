'''
一、re模块
什么是正则呢？既是我们可以定义一些规则，从而对字符串进行过滤。
python语言当中用re模块来操作正则，是匹配字符串的一种规则。
必须掌握方法：①findall ②search ③match
'''
# 1、findall：返回所有满足匹配条件的结果,放在列表里
# import re
# ret = re.findall('[a-z|A-Z]+', 'Java Python C C# Go')
# print(ret)


# 2、search：只要找到符合规则的第一个就直接返回
# ①需要调用group()才能拿到结果。
# ②没有找到方方方None，调用group会报错。
# import re
# ret = re.search('Q', 'Java Python C C# Go')
# print(ret)                   # 拿到的是一个对象
# print(ret.group())          # 这样写匹配不到字符,会报错


# 一般是这样用解决会报错，if ret：
# import re
# ret = re.search('Q', 'Java Python C C# Go')
# # print(ret)
# if ret:
#     print(ret.group())


# 3、match：从前往后找到第一个就返回
# ①调用group才能拿到结果。
# ②没有找到方方方None，调用group会报错。
# import re
# ret = re.match('Ja', 'Java Python C C# Go')
# if ret:
#     print(ret.group())

# 4、split：切割字符串
# import re
# ret = re.split('[Ja]', 'Java Python C C# Go')
# # 先按J分割，得到['', ava Python C C# Go],再按a分割，得到['', '', 'v', ' Python C C# Go']
# print(ret)


# 5、sub、subn：替换
# import re
# # 将字符串的数字替换成空字符，得到：ABCD
# ret = re.sub('\d', '', 'A1B2C3D', 3)   # 参数3表示只替换3个
# print(ret)
# ret = re.subn('\d', '', 'A1B2C3D')     # 返回元组(替换的结果,替换了多少次)
# print(ret)


# 6、compile：将正则表达式编译成为一个对象，需写入匹配规则
# import re
# comp = re.compile('gs(.+?)l')
# ret = comp.findall('gs963lol')
# print(ret)

# 7、finditer：拿到的是一个迭代器，也需group才能拿到值
# import re
# ret = re.finditer('\d', 'asd46sad78asd6564')
# print(ret)                           # 迭代器
# print(next(ret).group())            # 查看第一个值
# print(next(ret).group())            # 查看第二个值
# print([i.group() for i in ret])    # 查看剩下所有值









# 1、实例1，匹配现在主流手机号的规则，如11位数，13等等主流开头的手机号
# import re
# phone = input('请输入您的手机号：')
# if re.match('^(13|14|15|18)[0-9]{9}$', phone):
#         print('是合法的手机号码')
# else:
#         print('不是合法的手机号码')


# 实例2，身份证号码匹配，还可以分组
# import re
# ret = re.search('([1-9]{2})([0-9]{4})(199|200|210|202)([0-9x]{9}$)', '440121202001024522')
# print(ret.group())
# print(ret.group(1))     # 分组查看
# print(ret.group(2))     # 分组查看
# print(ret.group(3))     # 分组查看
# print(ret.group(4))     # 分组查看


# 实例3，findall 分组优先：?:
import re
ret = re.findall('www.(baidu|gsxl).com', 'www.gsxl.com')
print(ret)
ret = re.findall('www.(?:baidu|gsxl).com', 'www.gsxl.com')  # 分组优先：?:
print(ret)

# split 分组优先，加个括号
ret = re.split('\d', 'www1gsxl2com')
print(ret)
ret = re.split('(\d)', 'www1gsxl2com')  # 分组优先：()
print(ret)
