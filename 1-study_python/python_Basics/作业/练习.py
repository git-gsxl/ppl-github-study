
import os

# with open('log1', encoding='utf-8') as f, open('log.bak', 'w', encoding='utf-8') as f1:
#     for line in f:
#         print(line, type(line))
#         if '星儿' in line:
        # f1.write(line)
# os.remove('log1')
# os.rename('log.bak', 'log1')
line = '星儿'
line.replace('星儿', '123')
print(line)


f = open('log1', encoding='utf-8')
f1 = open('log1.bak', 'w+', encoding='utf-8')

with f, f1:
    for i in f:
        if '欣欣' in i:
            i = i.replace('欣欣', '小龙')  # 更改为小龙
        f1.write(i)                         # 写入f1文件中

import os
os.remove('log1')                   # 删除源文件
os.rename('log1.bak', 'log1')      # 更改文件名称