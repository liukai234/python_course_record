'''
@Description: 
@LastEditors: liukai
@Date: 2020-04-27 10:02:03
@LastEditTime: 2020-04-27 10:20:04
@FilePath: /pyFile/文件操作/反序列化/反序列化.py
'''

# 尝试将vscode的 cxx_extension/launch.json 文件文件反序列化

import json

def main():
    data_src = json.load(open('test.json', 'r'))
    print(data_src)

if __name__ == "__main__":
    main()