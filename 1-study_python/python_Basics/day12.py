
#只要含有yield关键字的函数都是生成器函数
# yield不能和return共用且需要写在函数内
# def generator():
#     print(1)
#     yield 'a'
# ret = generator()       #生成器函数 ： 执行之后会得到一个生成器作为返回值
# print(ret)
# print(ret.__next__())

# # 也是可一个一个取值，yield 一次就取一次
# def generator():
#     yield 'a'
#     yield 'b'
#     yield 'c'
# g = generator()         # 得到生成器作为返回值
#
# ret = g.__next__()
# print(ret)
# ret = g.__next__()
# print(ret)
# ret = g.__next__()
# print(ret)

# # 来 200万 个数字
# def func():
#     for i in range(2000000):
#         yield '200万个数字:%s' % i
# g = func()
#
# # 取50个
# count = 0
# for i in g:
#     count += 1
#     if count > 50:
#         break
#     print(i)
#
# # 我只喜欢第100个
# for i in g:
#     count += 1
#     if count > 100:
#         print('我只喜欢：', i)
#         break
#
# print(g.__next__())     # +1
# print(g.__next__())     # +1
# print(g.__next__())     # +1 = 103

# 2、生成器进阶
def func():
    print(1)
    qq = yield 11
    print(qq)
    print(2)
    gg = yield 22
    res = True
    print(res, gg)

    yield

g = func()
print(g.__next__())
print(g.send('send===='))
print(g.send('send222===='))

# send 获取基本和 next 方法一致
# send 只是在获取下一个值的时候，给上一个值传一个实参
# 使用send注意事项：
#     第一次 yield 必须用 next
#     最后一个 yield 不能接受外部的值，既不能用 send


# def func():
#     a = '123456'
#     b = 99999
#     yield from (a, b)
# g = func()
# print(g.__next__())
# print(g.__next__())



