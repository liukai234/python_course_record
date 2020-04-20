'''
@Description: 判断三个数的最大值和最小值
@LastEditors: liukai
@Date: 2020-04-19 19:44:07
@LastEditTime: 2020-04-20 09:49:52
@FilePath: /pyFile/多分支结构.py
'''
#!/usr/bin/python3
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

def printf(a, b):
    "print"
    print('maxValue is:', a,' minValue is:', b); 
    return 0

# 多分支结构即使用if-elif，类似C/C++分割中的switch-case语句
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
