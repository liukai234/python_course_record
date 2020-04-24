'''
metaclass： 可以在创建类时动态修改类的定义
            使用metaclass动态修改类定义，需要先定义metaclass，
            1、metaclass要继承type类
            2、必须重写__new__()方法
'''
#  定义ItemMetaclass,继承type类
class ItemMetaclass(type):
    # cls代表动态修改的类
    # name代表动态修改的类名
    # bases代表被修改类的所有父类
    # attrs代表被修改类的所有属性、方法、组成的字典
    def __new__(cls, name, bases, attrs):
        # 为该类动态添加一个get_price方法
        attrs['get_price']=lambda self : self.price * self.discount
        return type.__new__(cls, name, bases, attrs)

# 定义Clothes类
class Clothes(metaclass=ItemMetaclass):

    __slot__=('name', 'price', 'discount')  # 限制动态添加属性、方法

    def __init__(self, name, price):
        self.name=name
        self.price=price

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, discount):
        self.__discount =discount

# 定义Book类
class Book(metaclass=ItemMetaclass):
    __slot__ = ('name', 'price', 'discount')

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, discount):
        self.__discount = discount

def test():
    b=Book("Python讲义", 79)
    b.discount = 0.8
    print(b.get_price())  # 创建Book类的get_price方法
    c = Clothes("T-恤", 49)
    c.discount = 0.9
    print(c.get_price())  # 创建Clothes类的get_price方法

test()