'''
@Description: 字符串
@LastEditors: liukai
@Date: 2020-04-19 19:46:09
@LastEditTime: 2020-04-21 08:24:51
@FilePath: /pyFile/字符串.py
'''

#!/usr/bin/python3 # 默认使用python3解释器
#-*- coding: utf-8 -*- # 使用utf-8编码
import time # 时间库 time.sleep(time);

print('hello', 'python', sep=',', end='!\n') # sep是自动在元素之间补充的分隔字符

print("Loading", end = ""),

for i in range(20):
    print(".",end = '', flush = True) # end将替换末尾的'\n'为'', flush = True将print及时写入到终端
    time.sleep(0.05)

# 字符串切片
str = '123456'
print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str) 
print (str + "TEST") # 连接字符串
print()

str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1)) # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize()) # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title()) # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper()) # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or')) # 8
print(str1.find('shit')) # -1
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He')) # False
print(str1.startswith('hel')) # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!')) # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())

# 列表list
list1 = [1, 3, 5, 7, 100]
# 添加元素
list1.append(200)
list1.insert(1, 400)
# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]
print(list1) # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
print(len(list1)) # 9
# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
	list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1) # [1, 400, 5, 7, 100, 200, 1000, 2000]
# 从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1) # [400, 5, 7, 100, 200, 1000]
# 清空列表元素
list1.clear()
print(list1) # []

# 列表的排序操作
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)

# 嵌套列表的操作
lst = [['k', ['qqq', 20, {'k1': ['aa', 3, '1']}, 33], 'xx']]  # 例子
lst[0][1][2]['k1'][0] = lst[0][1][2]['k1'][0].upper()         # 将 aa 变成大写AA
lst[0][1][2]['k1'][1] = str(lst[0][1][2]['k1'][1])            # 将列表中的3变成字符串‘3’
print("修改后的列表：", lst)

# 字典的相关操作
dic = {'k1': 'v1', 'k2': ['sb', 'aa'], (1, 2, 3, 4, 5): {'k3': ['2', 100, 'wer']}}
dic['k2'].append(33)                                          # k2对应的值中添加33
dic['k2'].insert(0, 's')                                      # k2对应的值的第一个位置插入一个元素‘s’
dic[(1, 2, 3, 4, 5)]['k4'] = 'v4'                             # 将(1,2,3,4,5)对应的值添加一个键值对 ‘k4’:’v4’
dic[(1, 2, 3, 4, 5)][(1, 2, 3)] = 'ok'                        # 将(1,2,3,4,5)对应的值添加一个键值对(1,2,3)：‘ok’
dic[(1, 2, 3, 4, 5)]['k3'][2] = 'qq'                          # 将’k3’对应的值的‘wer’改为’qq’。
print("修改后的字典为：", dic)