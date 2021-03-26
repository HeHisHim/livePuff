from re import S


def gen():
    x = 0
    y = 1
    while True:
        yield y
        x, y = y, x + y


class Gen:
    def __init__(self, end=6) -> None:
        self.start = 0
        self.end = end
        self.x = 0
        self.y = 1
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            self.start += 1
            res = self.y
        # else:
        #     raise StopIteration()
        self.x, self.y  = self.y, self.x + self.y
        return self.x

class T:
    def __init__(self):
        self.x = [1, 2, 3]

    def __iter__(self):
        for _ in self.x:
            yield _


if "__main__" == __name__:
    # for g in gen():
    #     print(g)
    #     import time
    #     time.sleep(1)
    for g in Gen():
        print(g)