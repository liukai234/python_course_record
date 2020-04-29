import sqlite3

'''
创建自定义比较函数：create_collation(name,callable)
    name:自定义函数名
    callable:对应函数。该函数包含两个参数，两个参数进行比较，返回正数则第一个大，返回负数，第二个大，返回0，两个相等
'''

# 比较字符串的第一个字符
def compare_s(s1, s2):

    if s1[0] == s2[0]:
        return 0
    elif s1[0] > s2[0]:
        return 1
    else:
        return -1

# 打开数据库
conn = sqlite3.connect('first.db')
# 注册自定义比较函数
conn.create_collation('compare_s', compare_s)
# 获取游标
c = conn.cursor()
# 执行自定义比较函数
c.execute('select * from user_tb order by name collate compare_s')
# 遍历游标(可迭代对象)
for r in c:
    print(r)
conn.commit()
c.close()
conn.close()
