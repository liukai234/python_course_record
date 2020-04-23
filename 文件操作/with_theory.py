"""
with 语句
功    能：管理资源关闭（可以帮助自动关闭文件，不需要显式关闭文件）
实现原理：使用 with 语句管理的资源必须是一个实现 上下文管理协议 的类，该类的对象成为 上下文管理器（context_manager）。eg:File类、FileInput类
        要实现上下文管理协议，必须实现两个方法:
         1、context_manager.__enter__() 进入上下文管理器自动调用的方法，在with代码块执行之前执行
         2、context_manager.__exist__(exc_type,exc_value,exc_traceback)
                                        退出----------------------，在-------------后----
            with代码块成功执行：三个参数均为None; with代码块异常终止，sys.exc_info得到的信息为参数
"""

#  自定义一个实现上下文管理协议的类，并使用with管理
class Fruits:
    def __init__(self, name):
        self.name=name

    def __enter__(self):
        print("%s进来啦"% self.name)
        return 0

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("%s出去啦"% self.name)
        if exc_tb is None:  # 无异常
            print("无异常关闭！")
        else:
            print("遇异常关闭！")
            return False

def test():
    with Fruits("红苹果") as one:
        print("Red Apple")
        print(one)  # __enter__()返回值会赋值给as后的变量

    print("-----------------")

    with Fruits("牛顿的苹果"):
        print("Newton's apple")
        raise Exception

if __name__ =="__main__":
    test()
