# https://zhuanlan.zhihu.com/p/64991670

"""
Future
Future本质上是一个用生成器实现的回调管理器
之所以使用协程, 是为了在遇到io阻塞的时候将运行的权利交出去, 当阻塞事件完成的时候, 通过一个回调来唤醒程序继续往下走
并且返回io事件的值. Future就是对这个过程的包装
"""

class Future:
    _FINISHED = "finished"
    _PENDING = "pending"
    _CANCELLED = "CANCELLED"