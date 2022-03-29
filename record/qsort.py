import random


def _qsort(arr, left, right):
    if left > right:
        return
    low = left
    high = right
    key = arr[left]

    while low < high:
        while low < high and arr[high] > key:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] <= key:
            low += 1
        arr[high] = arr[low]
    arr[low] = key
    _qsort(arr, left, low - 1)
    _qsort(arr, low + 1, right)


def qsort(arr):
    _qsort(arr, 0, len(arr) - 1)


if "__main__" == __name__:
    for x in range(10):
        arr = [random.randint(0, 10000) for _ in range(10)]
        print(arr)
        arr_ = sorted(arr)
        qsort(arr)
        print(arr)
        print(arr_)
        assert arr == arr_
