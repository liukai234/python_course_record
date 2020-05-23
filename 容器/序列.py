'''
 序列相关方法
__len__(self):
__getitem__(self, key):
__contains__(self, item):
__setitem__(self, key, value):
__delitem__(self, key):
'''

'''
定义一个序列，该序列按顺序包含52张扑克牌，分别是黑桃、红心、梅花、方块的2-A。
'''

def check_key(key):
    if not isinstance(key, int): raise TypeError("索引值必须是整数")
    if key < 0: raise IndexError("索引值必须是非负数")
    if key >= 52: raise IndexError("索引值不能超过%d" % 52)


class squeezer:
    def __init__(self):
        self.flowers = ('♠', '♥', '♣', '♦')
        self.values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        # 用于存储被修改的数据
        self.changed = {}
        # 用于存储已删除的数据
        self.deleted = []

    def __len__(self):
        return 52

    def __getitem__(self, item):
        check_key(item)
        # 如果在self.changed中找到，就返回修改后的值
        if item in self.changed:
            return self.changed[item]
        # 如果在self.deleted中找到，说明该元素被删除
        if item in self.deleted:
            return None
        # 否则根据推算返回序列元素
        flower = item // 13  # 取整获得花色0、1、2、3
        value = item % 13  # 取余获得点数
        return self.flowers[flower] + self.values[value]

    def __setitem__(self, key, value):
        check_key(item)
        self.changed[key] = value

    def __delitem__(self, key):
        check_key(item)
        if key not in self.deleted:
            self.deleted.append(key)
        if key in self.changed:
            del self.changed[key]


if __name__ == '__main__':
    # 创建实例
    s = squeezer()
    print(len(s))
    for i in range(13):
        print(s[i], end=' ')

