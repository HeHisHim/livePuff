# 使用property来对类属性进行限制, 实现类似java的get / set方法

class Spirit:
    def __init__(self):
        self._speed = 1
    
    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        # 对self._speed的赋值做限定
        if isinstance(speed, int) and 0 < speed and speed < 11:
            self._speed = speed
            return
        raise ValueError("speed value error")


mySpirit = Spirit()
print(mySpirit.get_speed()) # -- 1
mySpirit.set_speed(8) # set方法调用
print(mySpirit.get_speed()) # -- 8

print("\n")

# 在调用set方法上, python提供了一种更优雅的方式, 可以直接调用 mySpirit.speed 来进行set.
class Spirit_Use_Property:
    def __init__(self):
        self._speed = 1

    @property
    def speed(self):
        print("I am speed getter")
        return self._speed

    @speed.setter # 使用setter 相当于实现set方法
    def speed(self, speed):
        print("I am speed setter")
        if isinstance(speed, int) and 0 < speed and speed < 11:
            self._speed = speed
            return
        raise ValueError("speed value error")

x = Spirit_Use_Property()
print(x.speed)  # 该处调用打印了I am speed getter
x.speed = 9     # 该处调用打印了I am speed setter
print(x.speed)



