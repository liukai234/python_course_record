import mysql.connector

'''
插入、查询等操作基本跟SQLite一样，注意占位符不同
'''
# 连接数据库
conn = mysql.connector.connect(user='root', password='6241',
                               host='localhost', port='3306',
                               database='python', use_unicode=True)
'''下面的语句会自动提交'''
conn.autocommit = True
# 获取游标
c = conn.cursor()

''' 执行插入操作: %s为占位符'''
c.executemany('insert into user_tb values(null,%s,%s,%s)',
              (('三毛', '123321', 'female'),
               ('徐志摩', '123321', 'male'),
               ('白落梅', '123321', 'female')))
c.execute('select * from user_tb where user_id > %s', (0,))
# 通过游标获取列消息
for col in c.description:
    print(col[0], end='  ')
print('\n-----------------------------')
for r in c:
    print(r)

c.close()
conn.close()