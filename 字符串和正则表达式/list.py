# topic: 初学python之列表list
# author：Liu Xiaoxia
# time：2020/4/22 22:40

# 创建空列表
empty = []
print(empty) #[]

# 创建字符串列表
str_0 = ['abc', 'bcd', 'cde']
print(str_0) #['abc', 'bcd', 'cde']

# 创建数字列表
number = [1, 2, 3]
print(number) #[1, 2, 3]

# 创建混合列表
mix = ['abc', 2, 'def', 4]
print(mix) #['abc', 2, 'def', 4]

# 在列表最后添加有且仅有一个元素
str_0.append('英语好难')
print(str_0) #['abc', 'bcd', 'cde', '英语好难']
str_0[len(str_0):] = ['放暑假了']
print(str_0)
len(str_0)   #['abc', 'bcd', 'cde', '英语好难', '放暑假了']

# 用有且仅有一个列表扩展另一个列表，即同时在列表末尾添加多个元素
str_0.extend(['好好学习', '天天向上'])
print(str_0) #['abc', 'bcd', 'cde', '英语好难', '放暑假了', '好好学习', '天天向上']

# 在列表固定位置(下标从0开始)插入元素
str_0.insert(0, 'aaaaa')
print(str_0) #['aaaaa', 'abc', 'bcd', 'cde', '英语好难', '放暑假了', '好好学习', '天天向上']

# 从列表删除元素(方法)
str_0.remove('英语好难')
print(str_0) #['aaaaa', 'abc', 'bcd', 'cde', '放暑假了', '好好学习', '天天向上']

# 从列表删除元素(函数)
del str_0[0]
print(str_0) #['abc', 'bcd', 'cde', '放暑假了', '好好学习', '天天向上']

# 返回列表中要删除的元素值
# 删除最后一个元素
str_0.pop()
print(str_0) #['abc', 'bcd', 'cde', '放暑假了', '好好学习']
# 删除指定元素
str_0.pop(1)
print(str_0) #['abc', 'cde', '放暑假了', '好好学习']

# 列表切片(分片)，一次性获取多个元素， 原列表不变
# 元素1到元素3(不包含元素3)
print(str_0[1:3]) #['cde', '放暑假了']
# 从列表头到元素3(不包含元素3)
print(str_0[:3])  #['abc', 'cde', '放暑假了']
# 从元素3到列表末尾
print(str_0[3:])  #['好好学习']
# 输出整个列表
# 与str_1 = str_0不同
# str_1 = str_0时，str_0和str_1指向同一块空间；而str_0[:]仅仅是将值给了str_1一份，指向两块不同的空间
str_1 = str_0[:]
print(str_1)      #['abc', 'cde', '放暑假了', '好好学习']

# 拼接两个列表
str_0 = str_0 + number
print(str_0) #['abc', 'cde', '放暑假了', '好好学习', 1, 2, 3]

# 复制列表元素
# 复制后直接输出，原列表不变
print(number)      #[1, 2, 3]
print(number * 3)  #[1, 2, 3, 1, 2, 3, 1, 2, 3]
number_copy = number.copy()
print(number_copy) #[1, 2, 3]
# 复制后赋值给原列表
number *= 2
print(number)      #[1, 2, 3, 1, 2, 3]

# 判断元素是否在列表中
print('好好学习' in str_0)   #True
print('哈哈哈' not in str_0) #True

# 判断元素是否在列表中的列表中
str_0.extend([['哈哈哈', 'wuwuwu']])
print(str_0)                             #['abc', 'cde', '放暑假了', '好好学习', 1, 2, 3, ['哈哈哈', 'wuwuwu']]
print('哈哈哈' in str_0)                 #False
print('哈哈哈' in str_0[len(str_0) - 1]) #True

# 列表中的列表中的元素
print(str_0[7][1]) #wuwuwu

# 列表中数据出现的次数
print(number.count(2)) #2

# 返回参数在列表中第一次出现的位置
print(str_0.index('cde'))       #1
# 指定查找范围
print(str_0.index('cde', 0, 5)) #1

# 将整个列表翻转(无参数)
str_0.reverse()
print(str_0) #[['哈哈哈', 'wuwuwu'], 3, 2, 1, '好好学习', '放暑假了', 'cde', 'abc']

# sort排序
# 从小到大排序
number.sort()
print(number) #[1, 1, 2, 2, 3, 3]
# 从大到小排序
number.reverse()
print(number) #[3, 3, 2, 2, 1, 1]
number.sort(reverse=True)
print(number) #[3, 3, 2, 2, 1, 1]

#替换列表中的元素
str_0[0] = 'hahahha'
print(str_0) #['hahahha', 3, 2, 1, '好好学习', '放暑假了', 'cde', 'abc']
str_0[str_0.index('hahahha')] = "哈哈哈"
print(str_0) #['哈哈哈', 3, 2, 1, '好好学习', '放暑假了', 'cde', 'abc']
str_0[3:] = [54, 85, 95, 105]
print(str_0) #['哈哈哈', 3, 2, 54, 85, 95, 105]

#清空列表
str_0.clear()
print(str_0) #[]
