'''
@函数修饰器：使用 @ 符号引用已有的函数，可用于修饰其他函数。（比如：@staticmethod、@classmethod）
            当 @函数A 修饰 函数B ，中间过程如下：
            1、被修饰的函数 B 作为参数传给 函数 A
            2、函数 B 替换成 函数 A 的返回值
'''

# 将函数赋值给变量，函数本身也是对象
if __name__ == "__main2__":    
    def greet(name):
        return "hello" + name
    greet_someone = greet
    print(greet_someone("将函数赋值给变量"))

# 函数内定义函数
if __name__ == "__main3__":
    def greet(name):
        def get_message():
            return "hello"

        result = get_message() + name
        return result

    print (greet("函数内定义参数"))

# 函数作为参数传递给其他函数
# 函数可以返回其他函数

# 函数修饰器语法糖
if __name__ == "__main1__":
    def funA(fn): 
        print("This is A")
        fn()
        return "XYZ"

    @funA # 修饰器本身
    def funB(): # 被修饰的函数
        print("This is B")

    print(funB)

# 有参函数修饰器
if __name__ == "__main4__":
    def funA(fn): 
        print("This is A")
        def param(name):
            print("This is param start")
            fn(name)
            print("This is param end")
        return param

    @funA # 修饰器本身
    def funB(name): # 被修饰的函数
        print("This is B", name, sep=',')

    funB("来自funB的参数")
    
# 有参数的修饰器
if __name__ == "__main5__":
    def args(name):
        def funA(fn): 
            print("This is A")
            def param(name):
                print("The code create by", name, sep=":")
                fn()
                print("This is param end")
            return param(name) # 不return的话，定义的代码段不会执行
        return funA
        

    @args("来自修饰器的参数") # 修饰器本身
    def funB(): # 被修饰的函数
        print("This is B")

    funB


# 多个参数的函数
if __name__ == "__main__":
    def w2(fun):
        def wrapper(*args,**kwargs):
            print("this is the wrapper head")
            fun(*args,**kwargs)
            print("this is the wrapper end")
        return wrapper

    @w2
    def hello(name,name2,name3):
        print("hello"+name+name2+name3)

    hello("world","!!!", "777")