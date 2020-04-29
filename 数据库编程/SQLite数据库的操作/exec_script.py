import sqlite3

'''
使用executescript()方法执行一段SQL脚本（SQL脚本是由SQL语句构成。）
'''
# 打开数据库
conn = sqlite3.connect('first.db')
# 获取游标
c = conn.cursor()
# 使用executescript()方法执行一段SQL脚本
c.executescript('''
    insert into user_tb values(null, '埃里克', '123456', 'male') ; 
    insert into user_tb values(null, '弗雷迪', '123456', 'male');
    create table item_tb(_id integer primary key autoincrement,
    name,
    price);
    ''')
conn.commit()
c.close()
conn.close()
