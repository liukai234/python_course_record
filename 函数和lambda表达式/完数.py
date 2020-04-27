'''
@Description: 完数
@LastEditors: liukai
@Date: 2020-04-19 19:45:57
@LastEditTime: 2020-04-22 17:58:11
@FilePath: /pyFile/完数.py
'''

n = 100

def call(x):
    "判断此数是否为完数"
    sum = 0
    factor = 0
    for factor in range(x - 1, 0, -1):
        if x % factor == 0:
            # print(factor)
            sum += factor
    if x == sum:
        return True
    return False
if __name__ == '__main__': # 如果被test中的模块调用，此时的名字为'完数'，不为main，所以不会执行
    for ite in range(1, n + 1, 1):
        if call(ite) == True:
            print(ite)

