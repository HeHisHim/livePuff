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
    _CANCELLED = "cancelled"

    def __init__(self):
        self.status = self._PENDING

    def set_result(self, result):
        # 设置Future结果, 并将Future置为finished
        self.status = self._FINISHED
        self._result = result

    def done(self):
        return self.status != self._PENDING

    def result(self):
        # 获取Future结果
        if self._FINISHED != self.status:
            raise Exception("Future is not ready")
        return self._result

    """
    第一次启动时, 将自身设置为阻塞状态, 然后返回self
    第二次启动判断当前的status属性是否为 finished或cancelled
    暴露set_result方法让回调函数给Future设置返回值, 并更改Future状态
    """
    def __iter__(self):
        if not self.done():
            self._blocking = True
        yield self
        assert self.done(), "Future not done" # 再次运行Future时, 要保证事件已经完成
        return self.result()