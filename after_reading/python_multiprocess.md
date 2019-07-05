### [Python中的并行处理](https://python.freelycode.com/contribution/detail/1364)

### 一次可以运行的最大进程数受计算机中处理器数量的限制, 可以使用multiprocessing模块中的cpu_count()查看
```python
import multiprocessing as mp
mp.cpu_count()
```

## **`multiprocessing Pool类`**
### 同步执行
* Pool.map()
* Pool.starmap()
* Pool.apply()
### 异步执行
* Pool.map_async()
* Pool.starmap_async()
* Pool.apply_async()

## **`apply()和map()的异同`**
#### apply()和map()都是把将要进行并行化处理的函数作为主要参数. 不同的是apply()接受args参数, 通过args将各个参数传递到被并行处理的函数中, 而map()仅将一个迭代器作为参数

## **`计算每行中给定数值范围内的元素个数`**
* [Example (prepare data)](./python_multiprocess.py)
* [Example (不使用并行处理的参考代码)](./python_multiprocess.py)
* [Example (Pool.apply()进行并行化)](./python_multiprocess.py)
* [Example (Pool.map()进行并行化)](./python_multiprocess.py)
* [Example (Pool.starmap()进行并行化)](./python_multiprocess.py)

