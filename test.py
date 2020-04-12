'''
@Author: your name
@Date: 2020-04-03 15:32:52
@LastEditTime: 2020-04-11 17:22:25
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /pyFile/test.py
'''
sum = 0
'''
range(1, 100, 2)可以产生一个1到99的奇数序列，
其中2是步长，即数值序列的增量。
'''
'''
for x in range(101):
    sum += x
print(sum)
'''

import random

answer = random.randint(1, 100)


for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()