# https://zhuanlan.zhihu.com/p/64991670
import collections

_event_loop = None
def get_event_loop():
    global _event_loop
    if not _event_loop:
        _event_loop = Eventloop()
    return _event_loop

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

    def __init__(self, loop = None):
        if loop is None:
            self._loop = get_event_loop()
        else:
            self._loop = loop
        self._callbacks = []
        self._blocking = False
        self._result = None
        self.status = self._PENDING

    def _schedule_callbacks(self):
        # 将回调函数添加到事件队列里, 由Eventloop(run_once)运行
        for callbasks in self._callbacks:
            self._loop.add_ready(callbasks)

        self._callbacks = []

    def set_result(self, result):
        # 设置Future结果, 并将Future置为finished
        self.status = self._FINISHED
        self._result = result
        self._schedule_callbacks() # Future完成后, 添加回调到Eventloop并等待执行

    def add_done_callback(self, callback, *args):
        """
        添加回调函数
        """
        # 如果status非pending, 则将callback直接加入Eventloop的事件队列中
        # 否则, 将callback封装成Handle, 添加到 _callbacks列表里, 等待set_result被调用时处理
        if self.done():
            self._loop.call_soon(callback, *args)
        else:
            handle = Handle(callback, self._loop, *args)
            self._callbacks.append(handle)

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

# 任何一个协程框架都首先必须是一个异步框架, asyncio也不例外. asyncio的调度者是eventloop -- 事件循环
class Eventloop:
    def __init__(self):
        self._ready = collections.deque() # 事件队列
        self._stopping = False

    def stop(self):
        self._stopping = True

    def call_soon(self, callback, *args):
        handle = Handle(callback, self, *args)
        self._ready.append(handle)

    def add_ready(self, handle):
        # 添加事件到队列中
        if isinstance(handle, Handle):
            self._ready.append(handle)
        else:
            raise Exception("Only Handler is allowed to join in ready")

    def run_once(self):
        # 执行 _ready中的事件
        ntodo = len(self._ready)
        for _ in range(ntodo):
            handle = self._ready.popleft()
            # _run()相当于执行callback
            handle._run()

    def run_forever(self):
        while True:
            self.run_once()
            if self._stopping:
                break

class Handle:
    """
    对callback调用的一个简单封装, 主要是包装出 _run函数给Eventloop调用
    """
    def __init__(self, callback, loop, *args):
        self._callback = callback
        self._args = args

    def _run(self):
        self._callback(*self._args)


# Task继承自Future, 用来驱动协程的进行
class Task(Future):
    def __init__(self, coro, loop = None):
        Future.__init__(self, loop)
        self._coro = coro
        self._loop.call_soon(self._step) # 启动协程

    def _step(self, exc = None):
        try:
            if exc is None:
                # 首次send(None)相当于驱动Future __iter__ 里面的yield self
                result = self._coro.send(None)
            else:
                result = self._coro.throw(exc) # 抛出异常
        except StopIteration as identifier: # 该异常表明协程已经执行完毕, 调用set_result
            self.set_result(identifier.value)
        else:
            if isinstance(result, Future):
                if result._blocking:
                    self._blocking = False
                    result.add_done_callback(self._wakeup, result)
                else:
                    self._loop.call_soon(self._step, RuntimeError("use yield Error"))
            elif result is None:
                self._loop.call_soon(self._step)
            else:
                self._loop.call_soon(self._step, RuntimeError("Illegal return value"))

    def _wakeup(self, future):
        try:
            future.result()
        except Exception as identifier:
            self._step(identifier)
        else:
            self._step()