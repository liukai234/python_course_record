import sqlite3

'''
executemany()方法，多次执行同一条SQL语句---insert
'''
# 打开数据库
conn = sqlite3.connect('first.db')
# 获取游标
c = conn.cursor()
# 执行executemany()方法:第二个参数是一个元组
c.executemany('insert into user_tb values(null,?,?,?)',
              (('Alice', '123456', 'female'),
              ('Bob', '123456', 'male'),
              ('Cindy', '123456', 'female'),
              ('David', '123456', 'male')))
# 提交记录
conn.commit()
c.close()
conn.close()
