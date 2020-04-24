'''
@Description: 
@LastEditors: liukai
@Date: 2020-04-23 09:09:54
@LastEditTime: 2020-04-24 19:21:17
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
import datetime
# athlib 提供了一组类，以简单并且面向对象的方式提供了路径上的大多数常见的操作。使用 pathlib
# 比起使用 os 中的函数更加有效。和 os 相比，使用 pathlib 的另一个好处是减少了操作文件系统路
# 径所导入包或模块的数量
# 转载自 https://zhuanlan.zhihu.com/p/56909212

print('->pathlib.Path')
entries = Path('scandir')
for entry in entries.iterdir(): 
    # 由.iterdir()生成的每个条目都包含文件或目录的信息
    # 为文件系统提供了面向对象的接口
    if entry.is_file(): # 进行文件过滤
        print(entry.name)

"""                                                                           
转换 UNIX 时间戳为 datetime对象                                                       
:param timestamp: 时间戳                                                         
:param convert_to_local: 是否转为本地时间                                             
:param utc: 时区信息，中国为utc+8                                                     
:param is_remove_ms: 是否去除毫秒                                                   
:return: datetime 对象                                                          
"""                                                                           
def timestamp2datetime(timestamp, convert_to_local=True, utc=8, is_remove_ms=True):
    if is_remove_ms:
        timestamp = int(timestamp)                                                
    dt = datetime.datetime.utcfromtimestamp(timestamp)                            
    if convert_to_local:                                                          
        dt = dt + datetime.timedelta(hours=utc)                                   
    return dt                                                                     

# dosomething 补充时间格式转换
def convert_date(timestamp, format='%Y-%m-%d %H:%M:%S'):                          
    dt = timestamp2datetime(timestamp)                                            
    return dt.strftime(format)             

# 通过生成器来将上述更加简化一些
print('->生成器和生成式')
# 检测文件为entry.is_file() 检测目录为entry.is_dir()
files_in_entries = (entry for entry in entries.iterdir() if entry.is_dir())
for item in files_in_entries:
    print('目录名：{} 最后修改时间：{}'.format(item.name, timestamp2datetime(item.stat().st_mtime)))

# 创建单个目录
p = Path('sub4')
try:
    p.mkdir()
    # p.mkdir(exist_ok=True) 通过exist_ok来忽略异常
except FileExistsError as e:
    print(e)

# #
# 后边留着我接着补
