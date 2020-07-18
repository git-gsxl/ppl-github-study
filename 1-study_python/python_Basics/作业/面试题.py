# int 正反向排序
li = [1,5,6,2,8,7,9]
li.sort()             # 正向排序
print(li)

li = [1,5,6,2,8,7,9]  # 反向排序
li.sort(reverse=True)
print(li)

# 反转
li = [1,5,6,2,8,7,9]
li.reverse()
print(li)



# 面试题
a = 1
b = 2
# 用一行代码使a=b,b=a,并打印
a, b = b, a
print(a, b)
