'''
@Author: your name
@Date: 2020-04-06 17:04:58
@LastEditTime: 2020-04-06 17:05:43
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /pyFile/lyy.py
'''

year = int(input("输入年份："))
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 :
   print(year, '年，是闰年')
else:
   print(year, '年，不是闰年')