# 单例模式
class SingleTon:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

# x = SingleTon()
# y = SingleTon()
# print(x == y, x is y) # True True 