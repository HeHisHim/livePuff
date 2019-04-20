"""
单例模式
1. 一个类必须只有一个实例, 该实例可以通过一个众所周知的访问点访问
2. 该类必须在通过继承扩展后不会破坏原有模式
"""
class SingleTon:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

# x = SingleTon()
# y = SingleTon()
# print(x == y, x is y) # True True 