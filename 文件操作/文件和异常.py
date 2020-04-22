'''
@Description: 
@LastEditors: liukai
@Date: 2020-04-22 18:05:21
@LastEditTime: 2020-04-22 18:54:14
@FilePath: /pyFile/文件操作/文件和异常.py
'''
# 操作模式: r (读取 默认) w(写入 截断之前内容) x(写入 如果文件已存在会产生异常) 
# a(追加) b(二进制模式) t(文本模式 默认) +(更新 可读可写)

def main():

    # If file not exist, then
    # FileNotFoundError: [Errno 2] No such file or directory: 'text.txt'
    # FileNotFoundError 为对应异常, 然后来捕获这个异常
    try:
        f = open('text.txt', 'r', encoding='12306') # 指定未知编码是会直接导致 f 没有被赋值 utf-8 gb2312
        # 文件对象的read方法可以直接读取全部文件
        print(f.read())

    except FileNotFoundError:
        print('FileNotFoundError -> 文件不存在或文件无法打开')
        
    except LookupError:
        # for example, 上面这行写为 f = open('text.txt', 'r', encoding='12306')
        print('LookupError -> 指定了未知的编码')

    except UnicodeDecodeError:
        #注：测试此项时，记得设置text.txt文件的编码方式
        print('UnicodeDecodeError -> 读取文件时解码错误')

    finally:
        try:
            if f:
                f.close()
        except UnboundLocalError:
            print('UnboundLocalError -> 变量未被赋值')

# 由于finally块的代码不论程序正常还是异常都会执行到（甚至是调用了sys模块的exit函数退出Python环境，
# finally块都会被执行，因为exit函数实质上是引发了SystemExit异常），因此我们通常把finally块称为“
# 总是执行代码块”，它最适合用来做释放外部资源的操作。
def main2():
    try:

        # 通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源
        # with 上下文管理协议 dosomething 等待补充
        # with表达式其实是try-finally的简写形式
        with open('text.txt', 'r', encoding='12306') as f:
            print(f.read())
            f.close()
    except FileNotFoundError:
        print('文件不存在或文件无法打开')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')

if __name__ == "__main__":
    main2()