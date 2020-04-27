'''
@Description: subprocess 子进程
@LastEditors: liukai
@Date: 2020-04-27 13:59:10
@LastEditTime: 2020-04-27 17:01:56
@FilePath: /pyFile/文件操作/反序列化/sub.py
'''

from subprocess import run
run('tree -N -L 1', shell=True)