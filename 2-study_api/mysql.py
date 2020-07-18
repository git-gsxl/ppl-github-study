import pymysql

def dle_sql(sql=""):
    ''' sql操作 '''
    db = pymysql.connect(
        host='47.104.190.48',
        port=3306,
        user='root',
        passwd='root',
        db='django'
    )

    # 使用 cursor() 方法创建一个游标对象cur
    cur = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cur.execute(sql)

    db.commit()     # 提交执行
    db.close()      # 关闭

if __name__ == '__main__':
    sql = "delete from hello_teacher where teacher_name='龙老师';"
    dle_sql(sql)
