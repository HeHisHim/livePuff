import threading
import time
import multiprocessing

class SingleTon:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            print("not hasattr")
            cls._instance = object().__new__(cls, *args, **kwargs)
        return cls._instance

def func():
    s = SingleTon()
    print(id(s))

if "__main__" == __name__:
    # idx = [SingleTon() for _ in range(10)]
    # idx = set(idx)
    # assert 1 == len(idx)
    
    thread_list = list()
    for _ in range(1, 10):
        # _ = multiprocessing.Process(target=func)
        _ = threading.Thread(target=func)
        _.start()
        thread_list.append(_)

    for _ in thread_list:
        _.join()
    
    print(thread_list)