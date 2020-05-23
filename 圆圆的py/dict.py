'''
@Description: 
@LastEditors: liukai
@Date: 2020-05-15 20:52:51
@LastEditTime: 2020-05-15 21:03:06
@FilePath: /pyFile/圆圆的py/dict.py
'''

name_dict = {}
while True:
    info_list = []
    name = input("姓名：")
    if name == "":
        break
    else:
        num = int(input("学号："))
        info_list.append(num)
        score = float(input("成绩："))
        info_list.append(score)
        name_dict[name] = info_list

for key in name_dict:
    print("姓名:%s 学号: %s 成绩: %.1f" % (key, name_dict[key][0], name_dict[key][1]))

find = input("输入查找姓名")
if find in name_dict:
    print("姓名:%s 学号: %s 成绩: %.1f" % (find, name_dict[find][0], name_dict[find][1]))
