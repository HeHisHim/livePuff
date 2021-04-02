import time
import asyncio


# 写一个装饰器打印函数的运行时间
def record_time(func):
    def wraps(*args, **kwargs):
        begin = time.time()
        res = func(*args, **kwargs)
        print("record time: {}".format(time.time() - begin))
        return res

    return wraps


# 写一个洗牌程序 不用random.shuffle()实现
@record_time
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


# 写一个并发三个协程, 打印时间
async def task1():
    print("task1: {}".format(time.time()))


async def task2():
    print("task2: {}".format(time.time()))


async def task3():
    print("task3: {}".format(time.time()))


# 字符串反转
def reverse_str(s):
    # return s[::-1]
    if 1 == len(s) or not s:
        return s
    left = 0
    right = len(s) - 1
    s = list(s)
    while right > left:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return "".join(s)


if "__main__" == __name__:
    # arr = [1, 2, 3, 4, 5]
    # print(shuffle(arr))

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.wait([task1(), task2(), task3()]))
    # loop.run_until_complete(asyncio.gather(task1(), task2(), task3()))

    print(reverse_str("abcde"))
