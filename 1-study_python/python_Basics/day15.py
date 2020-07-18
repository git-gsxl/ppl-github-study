
'''
一、初识递归函数：在函数内调用自己。
1.如果是这样子，那么就停不下来，但python为了杜绝无限调用，就做了限制。
2.限制默认为：998，如下面函数所示。
RecursionError:递归错误，超出了递归的最大深度
'''

# # 1、简单递归函数：
# n = 0
# def func():
#     global n
#     n += 1
#     print(n)
#     func()
# func()


# 2、修改递归最大的深度:sys.setrecursionlimit
# import sys
# sys.setrecursionlimit(100000)
# n = 0
# def func():
#     global n
#     n += 1
#     print(n)
#     func()
# func()

# 3、递归实例
'''
A:我家比B多三头，你们猜我家有几头猪？  n=1   head(1)=head(2)+2 =head(n+1)+2
B:我家比C家多三头。                  n=2   head(2)=head(3)+2 =head(n+1)+2
C:我家比D家多三头。                  n=3   head(3)=head(4)+2 =head(n+1)+2
D:我家有15头猪                      n=4   head(4)=15
'''

# def head(n):
#     if n == 4:
#         return 15
#     elif n>0 and n<4:
#         return head(n+1)+3
#
# print('n=1:', head(1))
# print('n=2:', head(2))
# print('n=3:', head(3))
# print('n=4:', head(4))


# 4、看懂递归
# def head(1):                 # 我自己的函数传参是：1，所以先将 n=1 传入head函数内。
#     if 1 == 4:
#         return 15
#     elif 1>0 and 1<4:
#         return head(1+1)+3   # head(1+1)，到这一步调用了 head(2)
#
# def head(2):                 # head(2) ，所以将2传入下面的函数n
#     if 2 == 4:
#         return 15
#     elif 2>0 and 2<4:
#         return head(2+1)+3   # head(2+1)，到这一步调用了 head(3)
#
# def head(3):                 # head(3) ，所以将3传入下面的函数n
#     if 3 == 4:
#         return 15
#     elif 3>0 and 3<4:
#         return head(3+1)+3   # head(4) ，所以将4传入下面的函数n
#
# def head(4):
#     if 4 == 4:               # 4 == 4，所以知道了，head(4)=15，将15返回给上一次调用的head(3)中
#         return 15
#     elif 4>0 and 4<4:
#         return head(4+1)+3
#
# print('n=1:', head(1))



'''
二、初识算法
1.学习的算法都是成为过去时了。
2.但我们也应了解基础的算法，才能创新出更好的算法。
3.不是所有的程序都能套用现成等等算法来解决的，但可以解决一些我问题。
'''
# 1、二分查找算法 特点：必须处理有序的列表，每次处理中间值来判断大了还是小了，对应放向再次处理中间值...。

# 查找我输入的数字，每次该向哪边找？
# def find(lst, aim):
#     mid = len(lst) // 2
#     if aim < lst[mid]:
#         print(aim,'小于了中间值%s所以向左继续找' % lst[mid])
#         new = lst[:mid]
#         find(new, aim)
#     elif aim > lst[mid]:
#         print(aim,'大于了中间值%s所以向右继续找' % lst[mid])
#         new = lst[mid+1:]
#         find(new, aim)
#     else:print('最终找到：', aim)
#
# lst = [1, 2, 4, 6, 12, 23, 33, 56, 66, 67, 89, 92, 105]
# find(lst, 67)


# 我想知道这个索引的下标是多少
def find(lst, aim, start=0, end=None):
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
ret = find(lst, 33)
print(ret)

