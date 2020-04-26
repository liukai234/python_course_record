'''
@Description: 
@LastEditors: liukai
@Date: 2020-04-22 18:05:21
@LastEditTime: 2020-04-26 14:32:14
@FilePath: /pyFile/文件操作/文件和异常.py
'''
# 操作模式: r (读取 默认) w(写入 截断之前内容) x(写入 如果文件已存在会产生异常) 
# a(追加) b(二进制模式) t(文本模式 默认) +(更新 可读可写)

def main():

    # If file not exist, then
    # FileNotFoundError: [Errno 2] No such file or directory: 'input.txt'
    # FileNotFoundError 为对应异常, 然后来捕获这个异常
    try:
        f = open('input.txt', 'r', encoding='12306') # 指定未知编码是会直接导致 f 没有被赋值 utf-8 gb2312
        # 文件对象的read方法可以直接读取全部文件
        print(f.read())

    except FileNotFoundError as e:
        print('FileNotFoundError -> 文件不存在或文件无法打开', e)
        
    except LookupError as e:
        # for example, 上面这行写为 f = open('input.txt', 'r', encoding='12306')
        print('LookupError -> 指定了未知的编码', e)

    except UnicodeDecodeError as e:
        #注：测试此项时，记得设置input.txt文件的编码方式
        print('UnicodeDecodeError -> 读取文件时解码错误', e)

    finally:
        try:
            if f:
                f.close()
        except UnboundLocalError as e:
            print('UnboundLocalError -> 变量未被赋值', e)

# 采用上下文管理器 with
# 由于finally块的代码不论程序正常还是异常都会执行到（甚至是调用了sys模块的exit函数退出Python环境，
# finally块都会被执行，因为exit函数实质上是引发了SystemExit异常），因此我们通常把finally块称为“
# 总是执行代码块”，它最适合用来做释放外部资源的操作。
def main2():
    try:

        # 通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源
        # with 上下文管理协议 dosomething 等待补充
        # with表达式其实是try-finally的简写形式
        '''
        # 我们把
        try:
            f = open('')
        finily:
            f.close()
        // dosomething 貌似with被异常捕获后不会继续执行f.close，上边讲的太官方，没理解
        # 写为
        with open('') as f:
            f.close()
        '''

        '''
        with open('input.txt', 'r', encoding='12306') as f:
            print('通过read全部读取')
            print(f.read())
            f.close()
        '''

        with open('input.txt', 'r', encoding='gb2312') as f:
            print('通过for-in逐行读取')
            for line in f:
                print(line, end='')
            print()

        with open('input.txt', 'r', encoding='gb2312') as f:
            print('读取文件按行读取到\'列表\'中')
            lines = f.readlines() # 读取全部多行
            # lines = f.readline() # 只读取一行
        print(lines)

    except FileNotFoundError as e:
        print('文件不存在或文件无法打开', e)
    except LookupError as e:
        print('指定了未知的编码', e)
    except UnicodeDecodeError as e:
        print('读取文件时解码错误', e)

# 向文件写入
def main3():
    try:
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write('小猫猫\n')
            f.write('猫猫倒过来读也是猫猫')
            f.close()
    except IOError as e: # 写错误异常触发在文件和异常扩展中补充
        print('写错误', e) 

if __name__ == "__main__":
    main3()