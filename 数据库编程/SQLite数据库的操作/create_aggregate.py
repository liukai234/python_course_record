import sqlite3

'''
创建聚集函数：
1、五个标准的聚集函数：
    sum():统计总数
    avg():统计平均值
    count():统计记录条数
    max():统计最大值
    min():统计最小值
2、自定义聚集函数 :create_aggregate(name,num_paras,aggregate_class) 
    name:自定义聚集函数名称
    num_paras：所需参数个数
    aggregate_class：指定聚集函数的实现类。该类必须实现step(self,params...)和finalize(self)方法
       1.step(self,params...) ：对查询所返回的每条记录各执行一次；
       2.finalize(self)：只在最后执行一次，该方法的返回值作为聚集函数的返回值
'''
# 假设要实现查询表中name最短的记录，就需要自定义一个聚集函数
# 先定义一个类
class MinString:
    def __init__(self):
        self.min_string=None

    def step(self, s):

        # 如果self.min_string为None,直接将当前值赋值给他
        if self.min_string is None:
            self.min_string=s
            return
        # 找更短的s
        if len(self.min_string) >len(s):
            self.min_string=s

    def finalize(self):
        return self.min_string
# 打开数据库
conn = sqlite3.connect('first.db')
# 注册自定义聚集函数
conn.create_aggregate('min_string', 1, MinString)
# 获取游标
c = conn.cursor()
# 使用自定义聚集函数
c.execute('select min_string(name) from user_tb')
print("shortest name:", c.fetchone()[0])
conn.commit()
c.close()
conn.close()
