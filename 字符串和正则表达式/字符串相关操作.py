# topical: 字符串
# author: Liu Xiaoxia
# time: 2020.07.03

# 字符串也可以切片
# 比较操作符 逻辑操作符 成员操作符都可用
# 和列表、元组并列，都是序列

# 首字符大写
str1 = "xiaoxie"
str1 = str1.capitalize()
print(str1) #Xiaoxie

# 字符串全部小写
str1 = "DA Xie He XIAO XIe"
str1 = str1.casefold()
print(str1) #da xie he xiao xie

# 转换字符串中所有大写字符为小写
str1 = "DA Xie He XIAO XIe"
str1 = str1.lower()
print(str1) #da xie he xiao xie
# 转换字符串中所有小写字符为大写
str1 = "da Xie He Xiao XIe"
str1 = str1.upper()
print(str1) #DA XIE HE XIAO XIE

# 翻转字符串中的大小写
str1 = 'Hello WORld'
str2 =  str1.swapcase()
print(str2) #hELLO worLD

# 字符串居中，使用空格填充至给定长度
str2 = str1.center(25)
print(str2) #       Hello WORld

# 返回一个左对齐的字符串，并用空格填充至长度为width
str2 = str1.ljust(20)
print(str2) #Hello WORld         
# 返回一个右对齐的字符串，并用空格填充至长度为width
str2 = str1.rjust(20)
print(str2) #         Hello WORld

# 返回长度为width的字符串，原字符串右对齐，前边用0填充
str2 = str1.zfill(30)
print(str2) #0000000000000000000Hello WORld

# 返回子字符串sub在字符串中出现的次数，start和end表示范围
# count(sub[,start [,end]])
num = str1.count('xie')
print(num) #0

# 判断字符串是否以sub子字符串结束
# endswith(sub[,start [,end]])
flag = str1.endswith('haha')
print(flag) #False
# 判断字符串是否以prefix子字符串开始
# startwith(prefix[,start [,end]])
flag = str1.startswith('haha')
print(flag) #False

# 将字符串中的tab符号(\t)转换为空格，默认空格数tabsize = 8
# expandtabs([tabsize=8])
str1 = 'shu\tjia\tlai\tla!'
str1 = str1.expandtabs()
print(str1) #shu     jia     lai     la!

# 检测sub是否包含在字符串中，有则返回索引值，否则返回-1
# find(sub[,start [,end]])
num = str1.find('jia')
print(num) #8
# rfind(sub[,start [,end]])
# 类似find，不过是从右边开始查找
num = str1.rfind('jia')
print(num) #8
# index(sub[,start [,end]])
# 和find一样，不过，如果sub不在字符串中会产生一个异常
num = str1.index('la')
print(num) #16
# rindex(sub[,start [,end]])
# 和index一样，不过是从右边开始
num = str1.rindex('la')
print(num) #24

# 检测字符串中是否包含至少一个字符，且所有的字符都是字母或者数字，是则返回True，否则False
flag = str1.isalnum()
print(flag) #False

# 字符串中至少有一个字符且所有字符都是字母则返回True，否则False
flag = str1.isalpha()
print(flag) #False

# 判断字符串只包含十进制数字则返回True，否则返回False
flag = str1.isdecimal()
print(flag) #False

# 判断字符串只包含数字则返回True，否则返回False
flag = str1.isdigit()
print(flag) #False

# 判断字符串中只包含数字字符，则返回True，否则返回False
flag = str1.isnumeric()
print(flag) #False

# 字符串中至少包含一个区分大小写的字符，且这些字符都是小写，则返回True，否则False
flag = str1.islower()
print(flag) #True
str2 = '哈哈哈'
flag = str2.islower()
print(flag) #False

# 字符串中至少包含一个区分大小写的字符，且这些字符都是大写，则返回True，否则False
flag = str1.isupper()
print(flag) #False

# 字符串只包含空格，则返回True，否则返回False
flag = str1.isspace()
print(flag) #False

# 判断字符串标题化(所有单词有且仅有首字符大写)，则返回True，否则False
flag = str1.istitle()
print(flag) #False

# 返回标题化的字符串
str2 = str1.title()
print(str2) #Shu     Jia     Lai     La!

# 以字符串作为分隔符，插入到sub中所有的字符之间
str2 = str1.join('哈哈哈哈哈')
print(str2) #哈shu     jia     lai     la!哈shu     jia     lai     la!哈shu     jia     lai     la!哈shu     jia     lai     la!哈

# 删除字符串左右的所有空格，chars参数可以指定删除的字符
# strip([chars])
str1 = '    aaabbbaaa    '
str2 = str1.strip('a')
print(str2) #    aaabbbaaa    
# 去掉字符串左边所有空格
str1 = '    just a test'
str1 = str1.lstrip()
print(str1) #just a test
# 去掉字符串末尾所有空格
str1 = 'just a test    '
str1 = str1.rstrip()
print(str1) #just a test

# 找到子字符串sub，把字符串分成一个3元组(pre_sub, sub, fol_sub)
# 如果字符串中不包含sub则返回('源字符串', '', '')
str2 = str1.partition('te')
print(str2) #('just a ', 'te', 'st')
# rpartition(sub)
# 类似patition，从右边开始查找
str2 = str1.rpartition('te')
print(str2) #('just a ', 'te', 'st')

# 把字符串中的old子字符串替换成new子字符串，count指定替换次数
# replace(old, new[count])
str2 = str1.replace('test', 'joke')
print(str2) #just a joke

# 不带参数默认是以空格作为分隔符切片字符串
# 如果maxsplit参数有设置，则仅分隔maxsplit个字符串，返回切片后的子字符串拼接的列表
# split(sep = None, maxsplit = -1)
list1 = str1.split()
print(list1) #['just', 'a', 'test']

# 按照'\n'分隔，返回一个包含各行作为元素的列表
# 如果keepends参数指定，则返回前keepends行
# splitlines(([keepends]))
str1 = ('just\na\ntest')
str2 = str1.splitlines()
print(str2) #['just', 'a', 'test']

# 根据table的规则(可以由str.maketrans('a', 'b')定制)转换字符串中的字符
# translate(table)
str1 = 'just a test'
str2 = str1.translate(str.maketrans('s', 'b'))
print(str2)                    #jubt a tebt
print(str.maketrans('s', 'b')) #{115: 98}
