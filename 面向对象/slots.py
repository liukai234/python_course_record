'''
@Description: 
@LastEditors: liukai
@Date: 2020-04-21 20:55:13
@LastEditTime: 2020-04-21 21:00:11
@FilePath: /pyFile/面向对象/slots.py
'''

'''
Python是一门动态语言，动态语言允许我们在程序运行时给对象绑定新的属性或方法，
也可以对已经绑定的属性和方法进行解绑定。
但是如果我们需要限定自定义类型的对象只能绑定某些属性，可以通过在类中定义\_\_slots\_\_变量来进行限定
需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用。
'''

class Person(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_class')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age



def main():
    person = Person('1', 1)
    person._class = 2
    # person._a = 3 # Error AttributeError: 'Person' object has no attribute '_a'

if __name__ == "__main__":
    main()