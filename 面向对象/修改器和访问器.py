'''
@Description: 修改器和访问器
@LastEditors: liukai
@Date: 2020-04-21 18:57:32
@LastEditTime: 2020-04-21 20:50:43
@FilePath: /pyFile/面向对象/面向对象进阶.py
'''

'''
虽然我们不建议将属性设置为私有的，但是如果直接将属性暴露给外界也是有问题的，
比如我们没有办法检查赋给属性的值是否有效。我们之前的建议是将属性命名以单下划线开头，
通过这种方式来暗示属性是受保护的，不建议外界直接访问，
那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作。
如果要做到这点，就可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便
'''

class Person(object):
    def __init__(self, str):
        self._str = str

    # 访问器 - getter方法
    @property
    def str(self):
        return self._str

    # 修改器 - setter方法
    @str.setter
    def str(self, str): 
        self._str = str
    
    # 不使用访问器和修改器时，在类中写
    # def get_str(self):
        # return self._str

    # def set_str(self, str):
        # self._str = str

def main():
    person = Person('init_string')
    person.str = 'modify_string' # 使用修改器
    # person.set_score('modify_string') # 不使用修改器
    print(person.str) # 使用访问器 意义在于不直接访问受保护成员 
    # person.get_score() # 不使用访问器
    print(person._str) # 直接访问受保护成员，不建议这种写法

if __name__ == "__main__":
    main()