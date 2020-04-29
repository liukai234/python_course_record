import sqlite3

'''
executemany()方法,多次执行同一条SQL语句---update
'''
# 打开数据库
conn = sqlite3.connect('first.db')
# 获取游标
c = conn.cursor()
# update
c.executemany('update user_tb set name = ? where _id = ?',
              (('爱丽丝', 2),
               ('鲍勃', 3),
               ('森碟', 4),
               ('大卫', 5)))
conn.commit()
c.close()
conn.close()