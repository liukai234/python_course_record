'''
@Description: 
@LastEditors: liukai
@Date: 2020-04-22 12:35:29
@LastEditTime: 2020-04-22 12:49:22
@FilePath: /pyFile/面向对象/继承和多态.py
'''

# 类之间的关系
# is-a关系也叫继承或泛化，比如学生和人的关系
# has-a关系通常称之为关联，比如部门和员工的关系
# use-a关系通常称之为依赖，比如司机的驾驶行为和汽车

# 继承和多态
from abc import ABCMeta, abstractmethod

# Python本身不提供抽象类和接口机制，要想实现抽象类，可以借助abc(Abstract Base Class)
# abc.ABCMeta这是用来生成抽象基础类的元类, 由它生成的类可以被直接继承
# abc.abstractmethod(function) 表明抽象方法的生成器

# 抽象类
class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    # 抽象方法
    # 通过@abc.abstractmethod 将方法声明为抽象方法
    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)

class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    # 多态
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()