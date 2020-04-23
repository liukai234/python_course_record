# zip(),可以压缩 N 个列表成为一个zip对象（可迭代对象）。
a =['a', 'b', 'c']
b =[1, 2, 3]
[x for x in zip(a, b)]  # [('a', 1), ('b', 2), ('c', 3)]

# 列表长度不等时，以短的为准
c =['x','y']
[x for x in zip(a, c)]  # [('a', 'x'), ('b', 'y')]

# 例子
books =['简爱','小王子','瓦尔登湖']
prices =[56, 78, 66]
for book, price in zip(books, prices):
    print("%s的价格是：%3.1f"% (book, price))

# reversed() 实现反向遍历,参数可以是各种序列
[y for y in reversed(b)]  # [3, 2, 1]

# sorted() 接受一个可迭代对象，返回其升序。可传参数，reverse=True,key=?(排序关键字)
for book in sorted(books, reverse=True, key=len):
    print(book)