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
print(a) #[]
b = "shu jia kai shi la!"
b = list(b)
print(b) #['s', 'h', 'u', ' ', 'j', 'i', 'a', ' ', 'k', 'a', 'i', ' ', 's', 'h', 'i', ' ', 'l', 'a', '!']
c = (1, 1, 2, 3, 5, 8, 13, 21, 34)
c = list(c)
print(c) #[1, 1, 2, 3, 5, 8, 13, 21, 34]

# tuple()把一个可迭代对象转换为元组
# 和list()类似

# str(obj)把obj对象转换为字符串

# len(sub)返回sub的长度

# max()返回序列或者参数集合中的最大值
# 空序列会报错
# 保证元素是同一种类型，否则报错
tuple1 = (1, 2, 3, 4, 5, 9, 0)
print(max(tuple1))  #9
print(max('s', 'h', 'u', ' ', 'j', 'i', 'a')) #u
numbers = [2, 52, 61, 15, 8, -45]
print(max(numbers)) #61
chars = '154236890'
print(max(chars))   #9

# min()返回序列或者参数集合中的最小值
# 和max()使用方法相同，作用相反

# sum(iterable[, start = 0]) 返回序列iterable和可选参数start的总和
tuple2 = (1.2, 3.2, 5.6)
print(sum(tuple2))     #10.0
print(sum(tuple2, 11)) #21.0

# sorted()返回排好序的列表，默认从小到大
# 和list.sort()类似
print(sorted(numbers)) #[-45, 2, 8, 15, 52, 61]

# reversed()返回迭代器对象
# list.reverse()逆转列表元素
print(numbers)                 #[2, 52, 61, 15, 8, -45]
print(reversed(numbers))       #<list_reverseiterator object at 0x03EE3478>
print(list(reversed(numbers))) #[-45, 8, 15, 61, 52, 2]

# enumerate()生成由每个元素的索引值和本身值组成的元组
print(enumerate(numbers))       #<enumerate object at 0x03EE0DA8>
print(list(enumerate(numbers))) #[(0, 2), (1, 52), (2, 61), (3, 15), (4, 8), (5, -45)]

# zip(a, b)返回由各个参数的序列组成的元组
a = [2, 5, 6, 1, 4, 7, 9]
b = [11, 41, 51, 61, 71]
print(zip(a, b))       #<zip object at 0x03EE0DA8>
print(list(zip(a, b))) #[(2, 11), (5, 41), (6, 51), (1, 61), (4, 71)]
