'''
@Author: your name
@Date: 2020-04-06 17:06:11
@LastEditTime: 2020-04-06 17:12:04
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /pyFile/lyy2.py
'''

n = int(input("输入数字："))
fac = 1
for i in range(1, n + 1): # 前闭后开
    fac *= i;
print(fac)
