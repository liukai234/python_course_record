'''
@Description: 
@LastEditors: liukai
@Date: 2020-04-22 18:05:21
@LastEditTime: 2020-04-22 18:29:16
@FilePath: /pyFile/文件操作/test.py
'''
# 操作模式: r (读取 默认) w(写入 截断之前内容) x(写入 如果文件已存在会产生异常) 
# a(追加) b(二进制模式) t(文本模式 默认) +(更新 可读可写)

def main():

    # If file not exist, then
    # FileNotFoundError: [Errno 2] No such file or directory: 'text.txt'
    # FileNotFoundError 为对应异常, 然后来捕获这个异常
    try:
        f = open('text.txt', 'r', encoding='12306') # 指定未知编码是会直接导致 f 没有被赋值

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
                f.close
        except UnboundLocalError:
            print('UnboundLocalError -> 变量未被赋值')

if __name__ == "__main__":
    main()