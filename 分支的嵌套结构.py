'''
@Description: 分支的嵌套结构
@LastEditors: liukai
@Date: 2020-04-19 19:44:34
@LastEditTime: 2020-04-19 19:44:34
@FilePath: /pyFile/分支的嵌套结构.py
'''

#!/usr/bin/python3
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))


def printf(a, b):
    "print"
    print('maxValue is:', a, ' minValue is:', b)
    print(printf.__doc__) #输出函数注释
    return 0


if a > b:
    if b > c:
        print('a > b > c')
        printf(a, c)
    else:
        if a > c:
            print('a > c > b')
            printf(a, b)
        else:
            print('c > a > b')
            printf(c, b)
else:
    if b < c:
        print('c > b > a')
        printf(c, a)
    else:
        if c > a:
            print('b > c > a')
            printf(b, a)
        else:
            print('b > a > c')
            printf(b, c)
