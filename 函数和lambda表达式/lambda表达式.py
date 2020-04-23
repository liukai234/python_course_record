'''
lambda表达式：lambda [parameter_list] : 表达式
语法格式要点：1、必须要lambda关键字来定义
            2、lambda之后、冒号左边是参数列表，可以没有参数或者多个参数，右边是表达式的返回值
            3、只能是单行表达式，本质上是匿名的、单行函数体
'''
#  lambda表达式代替局部函数
def get_math_func(type):
    '''
    def square(n):       # 求平方
        return n*n

    def cube(n):         # 求立方
        return n * n * n

    def sum(n):         # 求1+2+3+...+n
        return (1 + n) * n / 2
    '''
    if type == 'square':
        return lambda n: n * n
        # return square
    if type == 'cube':
        return lambda n: n * n * n
        # return cube
    if type == 'sum':
         return lambda n: (1 + n) * n / 2
        # return sum

def test():
    #  返回一个嵌套函数
    math_func=get_math_func('cube')
    print(math_func(5))
    #  lambda 表达式调用内置函数map()
    x = map (lambda x: x * x if x % 2 == 0 else 0 , range(10))
    print([y for y in x])
