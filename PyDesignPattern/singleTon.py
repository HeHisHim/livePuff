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

class Borg:
    _shared_state = {} # 类属性在对象中是共享的
    def __init__(self):
        self.__dict__ = self._shared_state

class MyBorg(Borg):
    def __init__(self):
        Borg.__init__(self)
        self.state = "ok"

    def __str__(self):
        return self.state

x = MyBorg()
y = MyBorg()
print(x) # ok
print(y) # ok

x.state = "bad"
print(x) # bad
print(y) # bad

print(x == y, x is y) # False False 

# MyBorg对象在初始化中将 __dict__ 初始化为父类的类属性, 即两个MyBorg共享同一个 __dict__
# 但与SingleTon实现不同的是, MyBorg对象的内存地址是不一样的