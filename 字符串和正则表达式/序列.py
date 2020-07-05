# topical: 序列
# author: Liu Xiaoxia
# time: 2020.07.05

# 列表、元组和字符串的共同点：
# -都可以通过索引得到每一个元素
# -默认索引值总是从0开始
# -可以通过分片的方法得到一个范围内的元素的集合
# -有很多共同的操作符(重复操作符、拼接操作符、成员关系操作符)

# list()把一个可迭代对象转换为列表
a = list()
print(a)
b = "shu jia kai shi la!"
b = list(b)
print(b)
c = (1, 1, 2, 3, 5, 8, 13, 21, 34)
c = list(c)
print(c)

# tuple()把一个可迭代对象转换为元组
# 和list()类似

# str(obj)把obj对象转换为字符串

# len(sub)返回sub的长度

# max()返回序列或者参数集合中的最大值
# 空序列会报错
# 保证元素是同一种类型，否则报错
tuple1 = (1, 2, 3, 4, 5, 9, 0)
print(max(tuple1))
print(max('s', 'h', 'u', ' ', 'j', 'i', 'a'))
numbers = [2, 52, 61, 15, 8, -45]
print(max(numbers))
chars = '154236890'
print(max(chars))

# min()返回序列或者参数集合中的最小值
# 和max()使用方法相同，作用相反

# sum(iterable[, start = 0]) 返回序列iterable和可选参数start的总和
tuple2 = (1.2, 3.2, 5.6)
print(sum(tuple2))
print(sum(tuple2, 10))

# sorted()返回排好序的列表，默认从小到大
# 和list.sort()类似
print(sorted(numbers))

# reversed()返回迭代器对象
# list.reverse()逆转列表元素
print(numbers)
print(reversed(numbers))
print(list(reversed(numbers)))

# enumerate()生成由每个元素的索引值和本身值组成的元组
print(enumerate(numbers))
print(list(enumerate(numbers)))

# zip(a, b)返回由各个参数的序列组成的元组
a = [2, 5, 6, 1, 4, 7, 9]
b = [11, 41, 51, 61, 71]
print(zip(a, b))
print(list(zip(a, b)))
