
# filter 内置函数
def is_str(s):
    return s and str(s).strip()


lis = [1, 'hello', '', '  ', None, [], 6, 7, 'world', 12, 17]
ret = filter(is_str, lis)
# for i in ret:
#     print(i)

ret = map(lambda x: x**2, [1, -4, 6, -8])
print(ret)
for i in ret:
    print(i)


# filter 执行了filter之后的结果集合 <= 执行之前的个数
# filter只管筛选，不会改变原来的值
# map 执行前后元素个数不变
# 值可能发生改变
