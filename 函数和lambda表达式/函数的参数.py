'''
关键字参数：根据参数名来传入参数，无序遵循定义形参列表顺序
'''
def index_BMI(height, weight):
    print("weight", weight)
    print("height", height)
    return weight/(height**2)

#  根据位置传入参数
print(index_BMI(1.8, 65))
#  根据关键字参数传入参数,可交换位置
print(index_BMI(weight=65, height=1.8))
#  部分使用关键字参数,位置参数必须在关键字参数前
print(index_BMI(1.8, weight=65))

'''
参数默认值：要求定义在形参列表的最后
'''
#  定义一个打印三角形的函数
def print_triangle(char, high=6):
    for i in range(1,high+1):
        #  先打印一排空格
        for j in range(high-i):
            print(' ', end='')
        for j in range(2*i-1):
            print(char, end='')
        print()

#  不使用默认值
print_triangle("*", 7)
#  使用默认值参数
print_triangle("#")


'''
参数收集（个数可变的参数）：
1、在形参前面添加 一个 *，就意味这该参数可以接受多个参数值，多个参数值被当成 元组 传入。
2、可以位于形参列表的任意位置。若可变个数参数在前，则其后的参数只能使用关键字参数传入。
3、一个函数最多只能带一个“普通”参数收集的形参。
4、可以 收集 关键字参数  成 字典。需要在前面加 两个 *
'''
def test(num,*books, **scores):
    print(books)
    print(scores)
    print(num)
test(3, "海蒂和爷爷", "穆斯林的葬礼", "呼啸山庄", 语文=88, 数学=99)

'''
逆向参数收集：
1、在程序已有列表、元组、字典等对象的前提下，把他们的元素“拆开”后传递给函数的参数
2、需要在传入的列表、元组参数之前加 一个*，在字典参数前加 两个*
'''
def test_1(name, nums):
    print(name)
    print(nums)
my_tuple=("海洋", "很多")
test_1(*my_tuple)

def test_2(weather, date):
    print("日期：", date)
    print("天气：", weather)
my_dict={'date': 'Wednesday', 'weather': 'rainy'}
test_2(**my_dict)