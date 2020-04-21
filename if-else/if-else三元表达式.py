'''
@Description: 三元表达式
@LastEditors: liukai
@Date: 2020-04-21 08:56:52
@LastEditTime: 2020-04-21 09:00:33
@FilePath: /pyFile/if-else/if-else三元表达式.py
'''

x = 1
y = 2

if x > y:
	a = x
else:
	a = y

# 上述语句可以简化为
a = x if x > y else y
print(a)

# 从列表中挑选对象，f为假时将x赋值给a，否则将y赋值给a
f = True
a = [x, y][f]
print(a)