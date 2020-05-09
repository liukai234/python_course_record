'''
@Description: 三元表达式
@LastEditors: liukai
@Date: 2020-04-21 08:56:52
@LastEditTime: 2020-05-08 21:35:00
@FilePath: /pyFile/if-else/if-else三元表达式.py
'''

x = 1
y = 2

if x > y:
	a = x
else:
	a = y

print(a)










# 上述语句可以简化为
a = x if x > y else y
print(a)

# set4 = {num for num in range(1, 10) if num % 3 == 0 or num % 5 == 0}
# num for num in range(1, 10) 就是上边的x

# 从列表中挑选对象，f为假时将x赋值给a，否则将y赋值给a
f = True
a = [x, y][f]
print(a)