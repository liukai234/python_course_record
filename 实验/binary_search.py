def binary_search(array, index):
    length = len(array)
    if length > 0:
        mid = length // 2
        if array[mid] == index:
            return True
        elif array[mid] < index:
            return binary_search(array[mid + 1:], index)
        else:
            return binary_search(array[:mid], index)
    return False

if __name__ == '__main__':
    array = []
    for i in range(0, 10):
        array.append(i)
    print("array: ", array)
    find_num = 0
    print(find_num, " exist: ", binary_search(array, find_num))
    find_num = 10
    print(find_num, " exist: ", binary_search(array, find_num))


