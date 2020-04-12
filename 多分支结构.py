'''
@Author: your name
@Date: 2020-03-30 17:55:53
@LastEditTime: 2020-04-03 15:06:09
@LastEditors: Please set LastEditors
@Description: 2. 多分支结构语句
@FilePath: /pyFile/test.py
'''
#!/usr/bin/python3
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

def printf(a, b):
    "print"
    print('maxValue is:', a,' minValue is:', b); 
    return 0

if a > b:
    if b > c:
        print('a > b > c')
        printf(a, c)
    elif a > c:
        print('a > c > b')
        printf(a, b)
    else:
        print('c > a > b')
        printf(c, b)
elif a < b:
    if b < c:
        print('c > b > a')
        printf(c, a)
    elif c > a:
        print('b > c > a')
        printf(b, a)
    else:
        print('b > a > c')
        printf(b, c)
