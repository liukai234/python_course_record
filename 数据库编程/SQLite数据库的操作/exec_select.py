import sqlite3

'''
使用select语句执行查询：
执行select后，可以通过游标实现fetchone()、fetchmany()、fetchall()来获得查询结果
'''
# 打开数据库
conn = sqlite3.connect('first.db')
# 获取游标
c = conn.cursor()
# 执行select查询语句:查询所有_id大于2的记录
c.execute('select * from user_tb where _id > ?', (2,))

# 通过description属性获取所有列信息
for col in c.description:
    print(col[0], end='  ')
print('\n=======================')
while True:
    '''
    # 获取一条记录，每行数据都是一个元组
    row = c.fetchone()
    # 如果row为None,就退出循环
    if not row:
        break
    print(row)
    '''
    # 每次获取3条记录，返回一个由3条记录组成的列表
    rows = c.fetchmany(3)
    # 如果rows为None,就退出循环
    if not rows:
        break
    for r in rows:
        print(r)

c.close()
conn.close()
