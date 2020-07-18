
# 格式讲解

a = 'hello word! '  # 字符串

b = None             # 空

c = True             # 布尔值

d = ''               # 空格

e = [1, a, b, c, d, a[0]]    # 这是list

f = (a, '1', c, d)           # 这是元组

# 字典操作
g = {a: 1, b: True}         # 这是字典，键值对，key唯一的

g['ab'] = 'hello'   # 新增一个
print(g)

del g[a]             # 删除一个
print(g)

g['ab'] = '123'     # 修改 ab 变量为 123
print(g)

print(g['ab'])      # 查询



