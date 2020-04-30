import mysql.connector  # 导入访问MySQL的模块

'''
callproc(self,procname,args=())方法：用于调用数据存储过程。
procname：存储过程名字
args：传入参数
需要先在MySQL命令行中链接数据库，然后输入以下脚本来创建存储过程：
delimiter //
 create procedure add_pro(a int , b int, out sum int)
 begin
 set sum=a+b;
 end;
 //
 之后就可以调用该存储过程了。
'''

# 连接数据库
conn = mysql.connector.connect(user='root', password='tcoghwf6241',
                               host='localhost', port='3306',
                               database='python', use_unicode=True)
'''下面的语句会自动提交'''
conn.autocommit = True
# 获取游标
c = conn.cursor()
# 调用callproc()方法执行数据存储过程.
# 一下调用的存储过程就是开头注释中写的存储过程，需要3个参数，
# 最后一个参数程序不会使用它的值，所以用0来占位
s = c.callproc('add_pro', (78, 100, 0))
print(s)
c.close()
conn.close()


