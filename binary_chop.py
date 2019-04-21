# python实现二分查找

def binary_chop(arr, data):
    """
    非递归解决二分查找
    :param list:
    :return: Bool
    """
    arr.sort()
    length = len(arr)
    first = 0
    last = length - 1
    while first <= last:
        mid = (last + first) // 2
        if arr[mid] > data:
            last = mid - 1
        elif arr[mid] < data:
            first = mid + 1
        else:
            return True
    return False

if __name__ == "__main__":
    arr = [58, 23, 72, 14, 70, 81, 61, 10, 80, 42]
    data = 61
    print(binary_chop(arr, data))
