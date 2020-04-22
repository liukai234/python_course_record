'''
@Description: 模块和函数
@LastEditors: liukai
@Date: 2020-04-19 19:45:44
@LastEditTime: 2020-04-22 18:01:57
@FilePath: /pyFile/模块和函数.py
'''

from 完数 import call  # 模块导入，如果模块中有主函数，会自动执行模块
import random  # 随机数
sum = 0
answer = random.randint(1, 100)

# 默认参数输出九九乘法表
def fac(a = 1, b = 10):
    for i in range(a, b):
        for j in range(1, i + 1):
            # print('%d*%d=%d' % (i, j, i * j), end='\t') # 方法一
            # print('{0} * {1} = {2}'.format(a, b, a * b)) # 方法二
            """
            Python 3.6以后，格式化字符串还有更为简洁的书写方式，
            就是在字符串前加上字母f，我们可以使用下面的语法糖来简化上面的代码
            """
            print(f'{i} * {j} = {i * j}', end='\t')
        print()

# 从模块'完数'中导入call函数
if __name__ == "__main__":
    fac(5) # 带有默认参数的函数
    n = 100
    for ite in range(1, n + 1, 1):
        if call(ite) == True:
            print(ite)
