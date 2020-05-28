'''
@Description: 
@LastEditors: liukai
@Date: 2020-05-08 21:54:57
@LastEditTime: 2020-05-09 10:08:11
@FilePath: /pyFile/2.py
'''

# sum = 0
# for x in range(10):
#     sum += x
# print(sum)

sum = 0
num = 1
while num < 10:
    sum += num
    num += 1
    # num ++ # python不能 num ++
print(sum)