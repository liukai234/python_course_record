'''
@Description: 
@LastEditors: liukai
@Date: 2020-05-15 21:02:38
@LastEditTime: 2020-05-15 21:10:20
@FilePath: /pyFile/圆圆的py/max_score.py
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

max_score = 0
for ite in name_dict:
    if(name_dict[ite][1] > max_score):
        max_score = name_dict[ite][1]
        max_index = ite

print("姓名:%s 学号: %s 成绩: %.1f" % (max_index, name_dict[max_index][0], name_dict[max_index][1]))
