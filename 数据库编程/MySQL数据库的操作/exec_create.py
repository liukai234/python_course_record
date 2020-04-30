import mysql.connector  # 导入访问MySQL的模块                                                                            M

'''
MySQL的安装教程：https://www.cnblogs.com/xiaokang01/p/12092160.html
'''
# 1、连接数据库,！！！跟SQLite不同
conn = mysql.connector.connect(user='root', password='tcoghwf6241',
                               host='localhost', port='3306',
                               database='python', use_unicode=True)
# 2、获取游标
c = conn.cursor()
# 3、执行创建数据表
c.execute('''create table user_tb(
            user_id int primary key auto_increment,
            name varchar(255),
            pass varchar(255),
            gender varchar(255))''')
# 执行创建数据表
c.execute('''create table order_tb(
            order_id int primary key auto_increment,
            item_name varchar(255),
            item_price double,
            item_number double,
            user_id int,
            foreign key(user_id) references user_tb(user_id))''')
# 4、关闭游标
c.close()
# 5、关闭数据库
conn.close()

'''
运行结束后，打开数据库就会发现数据库中多了两个数据表
'''