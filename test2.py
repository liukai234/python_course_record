'''
@Author: your name
@Date: 2020-04-11 17:02:05
@LastEditTime: 2020-04-11 17:20:15
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /pyFile/test2.py
'''

while True:
    fun = int(input("计算法则："))
    if fun == 1:
        a = int(input("a = "))
        b = int(input("b = "))
        print(a + b)
    elif fun == 2:
        a = int(input("a = "))
        b = int(input("b = "))
        print(a - b)
    elif fun == 3:
        a = int(input("a = "))
        b = int(input("b = "))
        print(a * b)
    elif fun == 4:
        a = int(input("a = "))
        b = int(input("b = "))
        if b == 0:
            print("除数不能为0！")
            continue
        print(a / b)
    else:
        break
