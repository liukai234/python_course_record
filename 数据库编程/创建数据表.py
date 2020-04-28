import sqlite3             # 导入访问SQLite的模块

print(sqlite3.apilevel)    # python自带的SQLite数据库模块遵守DB API2.规范
print(sqlite3.paramstyle)  # SQL语句中用问号做参数

'''
遵守DB API2.规范的SQLite数据库模块会提供一个connect()函数，用于连接数据库，并返回数据库连接对象
程序只需要通过数据库连接对象打开游标，接下来就可以用游标老执行DL语句（负责创建表、修改表、删除表）
'''
# 1、打开或者创建数据库
'''
数据库连接对象:（用于获取游标，控制事务）通常具有以下属性和方法：
cursor()：打开游标
commit():提交事务
rollback():回滚事务
close():关闭数据连接
isolation_level:返回或者设置数据库连接事务中的隔离级别
in_transaction:判断当前是否处于事务
'''
# （也可以使用特殊名称：memory：,代表创建内存中的数据库）
conn = sqlite3.connect('first.db')

# 2、获取游标
'''
游标对象：（执行各种SQL语句）具有的属性和方法：
execute(sql[,parameters]):执行SQL语句。parameters为参数指定值。
executemany(sql,seq_of_parameters):重复执行执行SQL语句。seq_of_parameters序列为参数指定值，该序列有多少个元素，就执行多少次
executescript(sql_script):直接执行包含多少条SQL语句的SQL脚本（惑也？？？）
fetchone():返回查询结果集的下一行。如果没有下一行，就返回None
fetchmany(size=cursor.arraysize):返回查询结果集的下N行组成的列表。如果没有更多行就返回一个空列表
fetchall():返回查询结果集的全部行组成的列表
close():关闭游标
rowcount:（只读属性）返回受SQL语句影响的行数。
lastrowid:（只读属性）最后修改的rowid
arraysize:设置或者返回fetchmany()方法默认获取的记录条数，默认值为1
description:（只读属性）最后一次查询返回的所有列的信息
connection:（只读属性）创建游标的数据库连接对象
'''
c = conn.cursor()

# 3、执行DL语句---创建数据表
c.execute('''create table user_tb(
            _id integer primary key autoincrement,
            name text,
            pass text,
            gender text)''')

# 执行DL语句---创建数据表
c.execute('''create table order_tb(
            _id integer primary key autoincrement,
            item_name text,
            item_price real,
            item_number real,
            user_id integer,
            foreign key(user_id) references user_tb(_id) )''')

# 4、关闭游标
c.close()

# 5、关闭连接
conn.close()