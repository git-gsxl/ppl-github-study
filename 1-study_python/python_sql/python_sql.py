
# 1、sql查询账号密码，登录例子
import pymysql
user=input('username：')
pwd=input('password：')

conn =pymysql.connect(
        host='47.97.194.84',
        port=3306,
        user='root',
        passwd='123456',
        db='dba',
        charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = "select * from userinfo where user=%s and password=%s;"
cursor.execute(sql,(user,pwd))       # (user,pwd):传%s里面的变量，防止sql注入
result = cursor.fetchone()           # 返回一条结果
# result = cursor.fetchall()         # 返回全部结果
cursor.close()
conn.close()
if result:
    print('登录成功')
else:
    print('登录失败')

# # 2、sql插入数据
# use = 'gsxl'
# pwd = '123456'
# import pymysql
# conn =pymysql.connect(
#         host='47.97.194.84',
#         port=3306,
#         user='root',
#         passwd='123456',
#         db='dba')
# cursor = conn.cursor()
# sql = "insert into userinfo(user,password)values(%s,%s);"
# cursor.execute(sql,(use,pwd))
# r = cursor.lastrowid
# print('自增ID：%s'%r)
# conn.commit()
# cursor.close()
# conn.close()
# print('受影响的行数：%s'%r)

# 2、插入多行数据:executemany
# import pymysql
# conn =pymysql.connect(
#         host='47.97.194.84',
#         port=3306,
#         user='root',
#         passwd='123456',
#         db='dba')
# cursor = conn.cursor()
# sql = "insert into userinfo(user,password)values(%s,%s);"
# r = cursor.executemany(sql,[('asd','123'),('das','456')])
# print('受影响的行数：%s'%r)     # 那返回值
# conn.commit()                   # commit：增、删、改都需要提交事务
# cursor.close()
# conn.close()

# 3、删除：delete
# import pymysql
# conn =pymysql.connect(
#         host='47.97.194.84',
#         port=3306,
#         user='root',
#         passwd='123456',
#         db='dba')
# cursor = conn.cursor()
# sql = "delete from userinfo where user='gsxl';"
# r = cursor.execute(sql)
# print('受影响的行数：%s'%r)     # 拿返回值
# conn.commit()                   # commit：增、删、改都需要提交事务
# cursor.close()
# conn.close()

# 3、修改：update
# import pymysql
# conn =pymysql.connect(
#         host='47.97.194.84',
#         port=3306,
#         user='root',
#         passwd='123456',
#         db='dba')
# cursor = conn.cursor()
# sql = "update userinfo set `password`='666' where `user`='gsxl';"
# r = cursor.execute(sql)
# print('受影响的行数：%s'%r)     # 拿返回值
# conn.commit()                   # commit：增、删、改都需要提交事务
# cursor.close()
# conn.close()