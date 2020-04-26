'''
@Description: 
@LastEditors: liukai
@Date: 2020-04-26 14:26:03
@LastEditTime: 2020-04-26 15:01:53
@FilePath: /pyFile/文件操作/shutil1.py
'''

# shutil 是shell实用程序的缩写。 它为文件提供了许多高级操作，
# 来支持文件和目录的复制，归档和删除。 在本节中，你将学习如何移
# 动和复制文件和目录。
from pathlib import Path
import shutil

print('->删除目录树dir1')
p = Path('dir1/dir2/dir3')
p.mkdir(parents=True, exist_ok=True)
try:
    shutil.rmtree('dir1')
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')


print('->复制文件')
src_path='text.txt'
dst_path='dir1'
p=Path(src_path)
p.touch()
p=Path(dst_path)
p.mkdir()
shutil.copy(src_path, dst_path)

print('->复制目录')
shutil.copytree('scandir', 'dir1/scandir_backup') # 目标位置不能为已有目录

print('->移动文件或目录')
shutil.rmtree('dir1/scandir_backup')
shutil.rmtree('scandir/dir1')
shutil.move('dir1/', 'scandir/')
# 如果 scandir/ 存在，则将 dir1/ 移动到 scandir/
# 如果 scandir/ 不存在，则 dir_1/ 将重命名为 scandir

print('->重命名')
data_file = Path('scandir')
data_file.rename('scand')