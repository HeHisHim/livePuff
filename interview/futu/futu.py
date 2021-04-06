import threading
import time
import multiprocessing

def synchronized(func):
    func.__lock__ = threading.Lock()
    def lock_func(*args, **kwargs):
        print(func.__lock__, id(func.__lock__))
        with func.__lock__:
            return func(*args, **kwargs)
    return lock_func

SingleTonLock = threading.Lock()

class SingleTon:
    # 线程锁也必须是单例的
    @synchronized
    def __new__(cls, *args, **kwargs):
        print(SingleTonLock, id(SingleTonLock))
        with SingleTonLock:
            if not hasattr(cls, "_instance"):
                time.sleep(1)
                print("not hasattr")
                cls._instance = object().__new__(cls, *args, **kwargs)
            return cls._instance

def func():
    s = SingleTon()
    print(id(s))

if "__main__" == __name__:
    # idx = [func() for _ in range(10)]
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