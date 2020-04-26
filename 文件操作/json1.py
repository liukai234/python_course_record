'''
@Description: 
@LastEditors: liukai
@Date: 2020-04-23 09:10:49
@LastEditTime: 2020-04-26 15:24:26
@FilePath: /pyFile/文件操作/json1.py
'''

# 把一个列表或者一个字典中的数据保存到json文件中
import json

# dump - 将Python对象按照JSON格式序列化到文件中
# dumps - 将Python对象处理成JSON格式的字符串
# load - 将文件中的JSON数据反序列化成对象
# loads - 将字符串的内容反序列化成Python对象

# 序列化（serialization）在计算机科学的数据处理中，
# 是指将数据结构或对象状态转换为可以存储或传输的形式，
# 这样在需要的时候能够恢复到原先的状态，而且通过序列化
# 的数据重新获取字节时，可以利用这些字节来产生原始对象
# 的副本（拷贝）。与这个过程相反的动作，即从一系列字节
# 中提取数据结构的操作，就是反序列化（deserialization）

def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')

if __name__ == '__main__':
    main()