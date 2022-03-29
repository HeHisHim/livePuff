import random


def interpolation_search(arr, theKey):
    """
    @param arr 待查列表
    @param theKey 查找元素
    """
    arr.sort()
    low = 0
    high = len(arr) - 1

    while arr[high] != arr[low] and theKey >= arr[low] and theKey <= arr[high]:
        # 根据theKey在low ~ high之间的大概位置来计算再赋值给mid
        mid = low + ((theKey - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if theKey > arr[mid]:
            low = mid + 1
        elif theKey < arr[mid]:
            high = mid - 1
        else:
            return mid

    if theKey == arr[low]:
        return low
    else:
        return -1


arr = []
for _ in range(100):
    arr.append(random.randint(0, 1000))
theKey = arr[19]

x = interpolation_search(arr, theKey)
print(x)
