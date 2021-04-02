import time

def shuffle(arr):
    res = []
    length = len(arr)
    while length:
        t = time.time() * 1000000
        remove_idx = int(t % length)
        # remove_idx = random.randint(0, length - 1)
        res.append(arr[remove_idx])
        arr.remove(arr[remove_idx])
        length -= 1
    return res


if "__main__" == __name__:
    arr = [1, 2, 3, 4, 5]
    print(shuffle(arr))