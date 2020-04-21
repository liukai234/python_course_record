'''
@Description: 
@LastEditors: liukai
@Date: 2020-04-21 09:05:13
@LastEditTime: 2020-04-21 09:28:07
@FilePath: /pyFile/面向对象/test.py
'''

class Student(object):
    def __init__(self, a, b): # 构造函数
        self.a = a # self表示为数据成员
        self.b = b
    def num1(self, c, d): # 成员函数
        self.c = c # self表示为数据成员
        self.__d = d # 私有成员 format: __var
        return self.c

def main():
    stu1 = Student('a', 'b')
    print(stu1.a, stu1.b)
    print(stu1.num1('c', 'd')) # 先对c进行定义才能访问
    print(stu1.c)
    # print(stu1.__d) # Error __d为私有成员


if __name__ == '__main__':
    main()