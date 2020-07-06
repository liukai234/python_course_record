# topical: 元组学习
# author: Liu Xiaoxia
# time: 2020.07.03

#创建一个元组(tuple是一个函数名,不能作为变量名)
tuple1 = (1, 5, 4, 8, 7)

#访问元组与访问列表类似，可用下标
print(tuple1[2])  #4
print(tuple1[3:]) #(8, 7)

#拷贝元组
tmp = tuple1[:]
print(tmp) #(1, 5, 4, 8, 7)

#元组不可以被修改
#tuple1[2] = 9
#会报错

#元组的标识符：逗号‘,’是关键，下面的temp仍然是元组
temp = 1, 5, 6, 10

#元组的乘法
tuple2 = 5 * (2, )
print(tuple2) #(2, 2, 2, 2, 2)

#增加元素(逗号和括号缺一不可)
tuple1 = tuple1[:2] + ("hahaha",) + tuple1[2:]
print(tuple1) #(1, 5, 'hahaha', 4, 8, 7)

#删除整个元组
del tuple2

#元组相关操作符
#拼接+  重复*  关系操作符< > =  逻辑操作符not and or  成员操作符in和not in
