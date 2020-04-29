import sqlite3

'''
向exec_create.py中创建的两个数据表中分别插入一条数据
'''
# 打开数据库
conn=sqlite3.connect('first.db')

# 获取游标
c = conn.cursor()

# 执行insert语句插入数据：第二个参数是元组，元组中的而每个元素为insert语句中的占位符？赋值
c.execute('insert into user_tb values(null,?,?,?)',
          ('孙悟空', '123456', 'male'))
c.execute('insert into order_tb values(null,?,?,?,?)',
          ('鼠标', '34.2', '3', 1))

# 提交记录
conn.commit()
c.close()
conn.close()