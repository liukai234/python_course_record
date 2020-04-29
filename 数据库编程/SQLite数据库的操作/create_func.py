import sqlite3

'''
创建自定义函数：
数据库连接对象提供了一个create_func(name ,num_paras,func)方法，用于创建自定义函数
name:自定义函数的名字
num_paras:自定义函数所需要的参数个数
func:对应函数
'''
# 先定义一个函数
def split_exec(s):
    # 对字符串进行截取
    return s[1:]

# 打开数据库
conn = sqlite3.connect('first.db')
# 注册自定义函数
conn.create_function('split_exec', 1, split_exec)
# 获取游标
c = conn.cursor()
# 使用自定义函数
c.execute('insert into user_tb values(null,split_exec(?), ?, ?)',
          ('憨豆', '123456', 'male'))
conn.commit()
c.close()
conn.close()