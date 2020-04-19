'''
@Description: 字符串
@LastEditors: liukai
@Date: 2020-04-19 19:46:09
@LastEditTime: 2020-04-19 19:49:23
@FilePath: /pyFile/字符串.py
'''

#!/usr/bin/python3 # 默认使用python3解释器
#-*- coding: utf-8 -*- # 使用utf-8编码

import time # 时间库 time.sleep(time);

print("---testint ： Loading 效果---")
print("Loading", end = ""),
'''
for i in range(20):
    print(".",end = '',flush = True)
    time.sleep(0.5)
'''

# 字符串操作
str = '123456' 
print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str) 
print (str + "TEST") # 连接字符串
print()

# 数组list
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']

print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表

print('hello', 'world', sep='+', end='!') # sep是自动在元素之间补充的分隔字符