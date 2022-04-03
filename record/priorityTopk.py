"""
topk问题 使用优先队列解决
"""

from queue import PriorityQueue

pro = PriorityQueue()

"""
因为PriorityQueue默认是取出最小值
但是需求是每次取出最大值
所以对存储的数据取反后再放进去
"""


def init(pro, k, arr):
    for x in range(k):
        pro.put(~arr[x])


def topk(pro, num):
    tmpList = []
    while not pro.empty():
        curMaxNum = ~pro.get()  # 取出数据, 然后取反, 相当于取出最大值
        if num >= curMaxNum:
            # 如果这时已经为空, 说明是curMaxNum是队列里最小的了, 直接替换
            if pro.empty():
                pro.put(~num)
                break
            # 否则替换队列里最小值
            else:
                pro.queue.pop()
                pro.put(~num)
                tmpList.append(curMaxNum)
                break
        tmpList.append(curMaxNum)

    # 把数据放回
    for x in tmpList:
        pro.put(~x)


if __name__ == "__main__":
    arr = [363, 637, 755, 361, 34, 965, 458, 659, 483, 372, 766, 385, 979, 912, 87, 942, 951, 260]

    k = 5
    init(pro, k, arr)

    for x in range(k, len(arr)):
        topk(pro, arr[x])

    while not pro.empty():
        print(~pro.get())