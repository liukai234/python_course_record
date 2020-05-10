'''
迭代器
要实现迭代器，需要实现两个方法：
1、__iter__(self):该方法返回一个迭代器（iterator）,迭代器必须包含__next__()方法，
    该方法返回迭代器的下一个元素。
2、__reserved__(self):实现迭代器的反转。
'''


# 定义一个斐波那契数列的迭代器 f(n+2) = f(n+1) + f(n)

class Fibs:
    def __init__(self, len):
        self.first = 0
        self.sec = 1
        self.__len = len

    def __next__(self):
        # 如果len为0，结束迭代
        if self.__len == 0:
            raise StopIteration
        # 完成数列计算
        self.first, self.sec = self.sec, self.first + self.sec
        # 数列长度减1
        self.__len -= 1
        return self.first

    def __iter__(self):
        return self


# 创建对象
f = Fibs(20)
# 获取迭代器的下一个元素
print(next(f))
# 循环遍历迭代器
for i in f:
    print(i, end=' ')