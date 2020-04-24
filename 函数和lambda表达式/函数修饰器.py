'''
@函数修饰器：使用 @ 符号引用已有的函数，可用于修饰其他函数。（比如：@staticmethod、@classmethod）
            当 @函数A 修饰 函数B ，中间过程如下：
            1、被修饰的函数 B 作为参数传给 函数 A
            2、函数 B 替换成 函数 A 的返回值
'''
def funA(fn):
    print("This is A")
    fn()
    return "XYZ"

@funA
def funB():
    print("This is B")

print(funB)