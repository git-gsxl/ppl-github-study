# 1、lis = [[1, 2], (3, 4), 5, 6, 7]， 如何得出数字类型 1234567 ?
# 因为嵌套的是int类型，不能用join拼接，join适合用于str，所以用转换为str拼接。
lis = [[1, 2], (3, 4), 5, 6, 7]
st = ''
for i in lis:
    try:
        for s in i:
            st += str(s)
    except:st += str(i)
print(type(int(st)), int(st))

# 2、将 efgh_789_456_abcd 转换为：abcd_456_789_efgh，有两种法子：
# ①切片：切为列表再切片+拼接
lis = 'efgh_789_456_abcd'
lis = lis.split('_')
lis = '_'.join(lis[::-1])
print(lis)

# ②反转：切为列表，反转+拼接
lis = 'efgh_789_456_abcd'
lis = lis.split('_')
lis = '_'.join(list(reversed(lis)))
print(lis)

# 3、将‘ac’去除, replace 替换为空字符串
lis = ['过ac三ac八cca的人I', 'LcaIaKacE', 'aYacOcUac跑ac来ac说aca溜溜溜一ac吃点ac语ac法糖']
new_lis = []
for iss in lis:
    remove_a = iss.replace('a', '')
    remove_b = remove_a.replace('c', '')
    new_lis.append(remove_b)
print(new_lis)


# 4、lis = [1,2,3, 11,2,5,3,2,5,3]，用一行代码得出[11,1,2,3,5]
# 自动去重，set
lis = [1, 2, 3, 11, 2, 5, 3, 2, 5, 3]
print(list(set(lis)))

# 5、写一个函数，将列表最大值以及下标打印出来
def func(lis):
    max_num = lis[0]
    index = 0
    for i in range(len(a)):
        if lis[i] > max_num:
            max_num = lis[i]
            index = i
        # else:
        #     min_num = a[i]
        #     min_index = i
    return '最大值为：%s，下标为：%s' % (max_num, index)
a = [2, 3, 4, 80, 5, 6, 7]

print(func(a))
# 1、冒泡排序
# ''' 思路：
# 1.len(lst)，得到长度
# 2.for循环去遍历对比
# 3.if A > B，那么改变它们的位置
# '''
# lst = [50, 4, 10, 12, 34, 20, 6, 9, 13, 1]
# for i in range(len(lst)):
#     for j in range(len(lst)-1):
#         if lst[j] > lst[j+1]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]
#     # print(lst)
#
# # 切片：
# # 2、取abcd，那么切片步长为2
# a = 'axbscsd'
# print(a[::2])
# print(a[:4:2])
#
# # 3、切割与拼接
# b = 'hello word haha'
# c = b.split(' ')     # 空格切割
# print(c)
# print(' '.join(c))   # 拼接回来
#
# # 4、列表表达式
# # 1-2+3-4+5-6....-100
# num = [i * ((-1)**(i+1)) for i in range(1, 101)]
# print(sum(num))
#
# # 5、递归思想,交互
# a = 0
# b = 1
# s = []
# while b < 100:
#     s.append(b)
#     a, b = b, a+b
# print(s)
#
# # 求10的阶乘
# qiu = 10
# num = 1
# for i in range(1, qiu+1):
#     num = num*i
# print(num)


def find(lis, num, start=0, end=None):
    index_num = len(lis)//2 +start
    print(index_num)
    if num < index_num:
        new_lis = lis[:num]
        find(new_lis, num)
    elif num > lis[num]:
        new_lis = lis[num+1:]
        find(new_lis, num)
    return print('最终找到：', num)


def new_find(lst, aim, start=0, end=None):
    end = len(lst) if end is None else end
    mid_index = (end-start) // 2 + start
    if start < end:
        if aim < lst[mid_index]:
            return find(lst, aim, start=start, end=mid_index-1)
        elif aim > lst[mid_index]:
            return find(lst, aim, start=mid_index+1, end=end)
        else:return'最终找到：%s，下标为：%s' % (aim, mid_index)
    else:return '找不到该值：%s' % aim


lst = [1, 2, 4, 6, 12, 23, 33, 56, 66, 67, 89, 92, 105]
ret = new_find(lst, 33)
# print(ret)

