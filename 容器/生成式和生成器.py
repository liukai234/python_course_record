'''
@Description: 生成式和生成器
@LastEditors: liukai
@Date: 2020-04-20 12:10:58
@LastEditTime: 2020-04-21 08:32:23
@FilePath: /pyFile/容器/生成式和生成器.py
'''

import sys

f = [x for x in range(1, 10)]
print('[x for x in range(1, 10)] =', f)
f = [x + y for x in 'ABC' for y in '123']
print('[x + y for x in \'ABC\' for y in \'123\'] =', f)
# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f1 = [x ** 2 for x in range(1, 10)]
print('sizeof(f1) =', sys.getsizeof(f1))  # 查看对象占用内存的字节数
print('f1 =', f1) #
# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f2 = (x ** 2 for x in range(1, 10))
print('sizeof(f2) =', sys.getsizeof(f2))  # 相比生成式生成器不占用存储数据的空间
print('f2 =', f2) #
for val in f2:
    print(val, end=' ')
print()