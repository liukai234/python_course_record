'''
@Description: 
@LastEditors: liukai
@Date: 2020-04-24 19:40:51
@LastEditTime: 2020-05-08 20:19:57
@FilePath: /pyFile/test.py
'''
# x = map (lambda x: x * x if x % 2 == 0 else 0 , range(10))
# print([y for y in x])

if __name__ == "__main__":
    list = []
    for i in range(10):
        list.append(int(input()))
    list.sort(reverse=True)
    print(list[0:1])

def test():
    print("Hello python")