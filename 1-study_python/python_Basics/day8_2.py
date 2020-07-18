# # 函数嵌套例子：
# def max(a, b):
#     return a if a > b else b
#
# def the_max(x, y, z):
#     c = max(x, y)
#     return max(c, z)
#
# print(the_max(2,3,4))


def func():
    a = 1
    def f():
        # a = 1
        def q():
            nonlocal a
            a += 1
            print(a)
        return q
    return f
f = func()()()