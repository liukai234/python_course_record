'''
@Description: 模块和函数
@LastEditors: liukai
@Date: 2020-04-19 19:45:44
@LastEditTime: 2020-04-19 19:45:45
@FilePath: /pyFile/模块和函数.py
'''
 
import random # 随机数
sum = 0
answer = random.randint(1, 100)
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()

# 从模块'完数'中导入call函数
from 完数 import call # 模块导入，如果模块中有主函数，会自动执行模块
n = 100
for ite in range(1, n + 1, 1):
        if call(ite) == True:
            print(ite)
