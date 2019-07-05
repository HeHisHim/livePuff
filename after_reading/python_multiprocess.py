import numpy as np
from time import time
import multiprocessing as mp

np.random.RandomState(100)
arr = np.random.randint(0, 10, size = [200000, 5])
datas = arr.tolist()

def solution(arr, minimum = 4, maximun = 8):
    count = 0
    for n in arr:
        if minimum <= n <= maximun:
            count += 1
    return count

pool = mp.Pool(mp.cpu_count())
results = []

# ---------------不使用并行处理的参考代码---------------
for arr in datas:
    results.append(solution(arr, 4, 8))
print(results[:5])
# ---------------不使用并行处理的参考代码---------------


# ---------------Pool.apply()进行并行化---------------
results = [pool.apply(solution, args = (arr, 4, 8)) for arr in datas]
pool.close()
print(results[:5])
# ---------------Pool.apply()进行并行化---------------


# ---------------Pool.map()进行并行化---------------
results = pool.map(solution, [arr for arr in datas])
pool.close()
print(results[:5])
# ---------------Pool.map()进行并行化---------------


# ---------------Pool.starmap()进行并行化---------------
# 与Pool.map()一样, Pool.starmap()也仅接受一个迭代器参数
# 但在starmap()中, 迭代器中的每一个元件也是一个迭代器
# 实际上, Pool.starmap()就像是一个接受参数的Pool.map()版本
results = pool.starmap(solution, [(arr, 4, 8) for arr in datas])
pool.close()
print(results[:5])
# ---------------Pool.starmap()进行并行化---------------


# ---------------Pool.apply_async()进行并行化---------------
# 此时results是pool.ApplyResult对象的列表, 用get()方法来获取所需的最终结果
results = [pool.apply_async(solution, args = (arr, 4, 8)) for arr in datas]
pool.close()
pool.join()
# print(results[:5]) # pool.ApplyResult对象
for res in results[:5]:
    print(res.get())
# ---------------Pool.apply_async()进行并行化---------------


# ---------------Pool.map_async()进行并行化---------------
results = pool.map_async(solution, [arr for arr in datas]).get()
pool.close()
pool.join()
print(results[:5])
# ---------------Pool.map_async()进行并行化---------------


# ---------------Pool.starmap_async()进行并行化---------------
results = pool.starmap_async(solution, [(arr, 4, 8) for arr in datas]).get()
pool.close()
pool.join()
print(results[:5])
# ---------------Pool.starmap_async()进行并行化---------------