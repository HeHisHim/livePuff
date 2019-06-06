# 使用两个栈来实现先进先出(FIFO)队列

class DoubleStack_Queue:
    def __init__(self):
        self.firstStack = []
        self.secondStack = []

    def put(self, item):
        self.firstStack.append(item)

    def get(self):
        if self.secondStack:
            return self.secondStack.pop()
        
        while self.firstStack:
            self.secondStack.append(self.firstStack.pop())
        else:
            return self.secondStack.pop()

    def qsize(self):
        return len(self.firstStack) + len(self.secondStack)

if __name__ == "__main__":
    q = DoubleStack_Queue()

    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    q.put(5)

    while q.qsize():
        print(q.get())