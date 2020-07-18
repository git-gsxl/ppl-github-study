'''
一、json
1.通用的序列化格式，http中常见的一种数据结构
2.但是python中只有部分数据类型能够进行序列化转换成字符串
'''
# 1.dumps序列化 和 loads反序列化
# import json
# dic = {'k': 'v'}
# print(dic, '序列化前的类型：', type(dic))
# ret_str = json.dumps(dic)
# print(ret_str, '序列化后的类型：', type(ret_str))
# ret_dic = json.loads(ret_str)
# print(ret_dic, '反序列化后：', type(ret_dic))
# # 序列化的类型有：str、int、list、dict、tuple

# 2、dump 和 load 对一个对象进行序列化和反序列化
# import json
# dic = {'k': '中国'}
# with open('fff', 'w', encoding='utf-8')as f:
#     json.dump(dic, f, ensure_ascii=False)
#     json.dump(dic, f, ensure_ascii=False)
# with open('fff', encoding='utf-8')as f:
#     print(json.load(f))

# 3、使用 dumps 换行写入文件：
# import json
# dic = [{'k1': 1}, {'k2': 2}, {'k3': 3}]
# f = open('test', 'w')
# for i in dic:
#     str_dic = json.dumps(i)
#     print(type(str_dic), str_dic)
#     f.write(str_dic+'\n')
# f.close()
#
# # loads 一行一行读
# lis = []
# f = open('test')
# for i in f:
#     dic = json.loads(i)
#     print(type(dic), dic)
#     lis.append(dic)
# print(lis)
# f.close()


''' 
二、pickle
1.所以的python中的数据类型都可以转化为字符串形式
2.它只能在python语言中能理解，反序列需依赖python代码
'''
# 1、和json拥有的方法相同。
# 什么数据类型都可以，与文件需要加b，如rb、wb
# 支持分次dumps和loads
# dumps和loads：
# import pickle
# dic = [{'k1': 1}, {'k2': 2}, {'k3': 3}]
# str_dic = pickle.dumps(dic)
# print(str_dic)
# dic1 = pickle.loads(str_dic)
# print(dic1)


'''
三、shelve
1.只提供一个open方法，序列化句柄
2.使用句柄操作，非常方便
'''
import shelve
f = shelve.open('test')
f['k'] = {'k': '广深小龙'}
f.close()

f1 = shelve.open('test', writeback=True)     # writeback=True会记录所操作的增删改
dic = f1['k']
print(type(dic), dic)
f1.close()
