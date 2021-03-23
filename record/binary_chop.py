# python实现二分查找

def binary_chop_recursive(arr, data):
    """
    递归解决二分查找
    :param arr:
    :return:
    """
    arr.sort()
    length = len(arr)
    if 1 > length:
        return False
    mid = length // 2
    if arr[mid] > data:
        return binary_chop(arr[:mid-1], data)
    elif arr[mid] < data:
        return binary_chop(arr[mid+1:], data)
    else:
        return True

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
    print(binary_chop_recursive(arr, data))
