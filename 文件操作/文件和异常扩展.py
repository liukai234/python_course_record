'''
@Description: 
@LastEditors: liukai
@Date: 2020-04-23 09:09:54
@LastEditTime: 2020-04-23 10:26:41
@FilePath: /pyFile/文件操作/文件和异常扩展.py
'''

# python 是一个鹅妹子嘤工具

'''
获取文件属性
创建目录
文件名模式匹配
遍历目录树
创建临时文件和目录
删除文件和目录
复制、移动和重命名文件和目录
创建和解压ZIP和TAR档案
使用fileinput 模块打开多个文件
'''

# 在现代Python版本中，可以使用 os.scandir() 和 pathlib.Path获取目录列表
# 使用os.scandir

import os
print('->os')
entries = os.scandir('scandir') # os.scandir() 调用时返回一个迭代器而不是一个列表
print('迭代器', entries)

with os.scandir('scandir') as entries:
    for entry in entries:
        print(entry.name)

# 使用pathlib.Path
from pathlib import Path

# athlib 提供了一组类，以简单并且面向对象的方式提供了路径上的大多数常见的操作。使用 pathlib
# 比起使用 os 中的函数更加有效。和 os 相比，使用 pathlib 的另一个好处是减少了操作文件系统路
# 径所导入包或模块的数量
# 转载自 https://zhuanlan.zhihu.com/p/56909212

print('->pathlib.Path')
entries = Path('scandir')
for entry in entries.iterdir(): 
    # 由.iterdir()生成的每个条目都包含文件或目录的信息
    # 为文件系统提供了面向对象的接口
    print(entry.name)