# **`ch02`**
### python是强类型语言
```
In [16]: '5' + 5
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-16-f9dbf5f0b234> in <module>()
----> 1 '5' + 5
TypeError: must be str, not int
```
在某些语言中, 例如 Visual Basic, 字符串"5"可能被默许转换(或投射)为整数, 因此会产生 10. 但在其它语言中, 例如 JavaScript, 整数 5 会被投射成字符串, 结果是联结字符串"55". 在这个方面, Python 被认为是强类型化语言, 意味着每个对象都有明确的类型(或类), 默许转换只会发生在特定的情况下, 如int和float的计算

### list()总是创建一个新的 Python 列表
```
a = [1, 2, 3]
c = list(a)
a is not c # True
```

# **`ch03`**
### list的 + 和 extend
```
# 两者都是为已定义的列表追加多个元素, 但是通过加法将列表串联的计算量较大
# 因为"+"要创建一个新的列表即开辟一个新的内存空间, 还要复制对象
# 用extend则可以节省内存空间, 也比"+"的操作更快
```

### 使用zip把行的列表转换为列的列表
```
pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'), ('Schilling', 'Curt')]
first, second = zip(*pitchers)
print(first)  # ('Nolan', 'Roger', 'Schilling')
print(second)  # ('Ryan', 'Clemens', 'Curt')
```

### 柯里化: 部分参数应用
* 柯里化指的是通过"部分参数应用"从现有函数派生出新函数的计数
```
# 如执行两数相加的简单函数
def add_numbers(x, y):
    return x + y

# 通过该函数可以派生出新的只有一个参数的函数, add_five. 它对另一个参数加5
add_five = lambda y: add_numbers(5, y)

# add_numbers的第二个参数称为"柯里化的"(curried), 其实就是定义了一个可以调用现有函数的新函数罢了. 内置的functools.partial函数可将此过程简化
import functools
add_five = functools.partial(add_numbers, 5)
```

# **`ch04`**
### 对Numpy数据子集的修改会直接反映到源数组上, 这意味着数据不会被复制, 视图上的任何修改都会直接反映到源数组上
```
numpy_arr = np.arange(10)
python_arr = list(range(10))
numpy_part = numpy_arr[5:8].copy()
python_part = python_arr[5:8]
numpy_part[0] = 12
python_part[0] = 12
print(numpy_arr)  # array([ 0,  1,  2,  3,  4, 12,  6,  7,  8,  9])
print(python_arr)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
* 这是因为Numpy的设计目的是处理大数据, 将数据复制多份就需要考虑性能和内存的问题, 这与设计初衷相背
* 若需要数据副本, 明确地进行复制操作即可. 如numpy_part = numpy_arr[5:8].copy()

### ndarray的切片
```
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[:2])  # array([[1, 2, 3], [4, 5, 6]]), 选取前两行
print(arr2d[:2, 1:])  # array([[2, 3], [5, 6]]), 选取前两行, 再选取后两列
print(arr2d[1, :2])  # array([4, 5]), 选取第二行, 再取前两列
print(arr2d[:2, 2])  # array([3, 6]), 选取第三列的前两行
print(arr2d[:, :1])  # array([[1], [4], [7]]), 选取所有行的前一列
```

### numpy.transpose
```
arr = np.arange(6).reshape((2,3))
print(arr)  # array([[0, 1, 2], [3, 4, 5]])
arr = arr.transpose((1, 0))
print(arr)  # array([[0, 3], [1, 4], [2, 5]])
```
* transpose((x, y, z, ...))可以理解为arr数组的轴, arr第一个[]为0, 第二个[]为1, 多维则第三个[]为2
* transpose((1,0))代表将[x][y]置换成[y][x], 即原arr[0][0] = 0, 置换后arr[0][0]还是为0. 而arr[0][1] = 1置换后arr[1][0] = 1. arr[1][0] = 3置换后arr[0][1] = 3. arr[0][2] = 2置换后arr[2][0] = 2
```
arr = np.arange(12).reshape((2,2,3))
print(arr)  # array([[[ 0,  1,  2], [ 3,  4,  5]], [[ 6,  7,  8], [ 9, 10, 11]]])
arr = arr.transpose((2, 0, 1))
print(arr)  # array([[[ 0,  3], [ 6,  9]], [[ 1,  4], [ 7, 10]], [[ 2,  5], [ 8, 11]]])
```
* transpose((2, 0, 1))代表将[x][y][z]置换成[z][x][y], 如arr[1][0][1] = 7置换为arr[1][1][0] = 7. arr[1][1][0]=9置换为arr[0][1][1] = 9

### numpy.where
* numpy.where是三元表达式x if condition else y的向量版本
```
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
# 假设需要根据cond为True选择xarr, 否则选择yarr. 用列表推导式写法
res = [(x if z else y) for x, y, z in zip(xarr, yarr, cond)]  # [1.1, 2.2, 1.3, 1.4, 2.5]
# 列表推导式写法无法处理多维数组的数据, 使用numpy.where能更好的解决这个问题
res = np.where(cond, xarr, yarr)  # array([1.1, 2.2, 1.3, 1.4, 2.5])
# where通常用于根据另一个数组而产生一个新的数组, 如将多维数组大于0的值替换为2
arr = np.random.randn(2, 3, 4)
np.where(arr>0, 2, arr)
```

### numpy.dot
* dot()返回的是两个数组的点积(dot product), 在python3.5也可用@运算符进行点积计算
```
# 如果处理的是一维数组, 则得到的是两数组的內积(两数组长度必须一致)
arr = np.arange(5)
brr = np.arange(5)
res = np.dot(arr, brr)  # arr.dot(brr)
print(res)  # 30, a0b0 + a1b1 + ... + a4b4

# 如果是计算二维数组的点积
arr = np.arange(5, 9).reshape((2, 2))
brr = np.arange(1, 5).reshape((2, 2))
res = arr.dot(brr)  # array([[23, 34], [31, 46]]), [[a00b00 + a01b10, a00b01 + a01b11], [a10b00 + a11b10, a10b01 + a11b11]]

# 如果是计算多维数组的点积, arr的行长必须与brr的列长一致
arr = np.arange(5, 11).reshape((2, 3))
brr = np.arange(1, 7).reshape((3, 2))
res = arr.dot(brr)  # array([[ 58,  76], [ 85, 112]])
```

# **`ch05`**
### pandas.rank
* 排名(rank)会从 1 开始一直到数组中有效数据的数量. 默认情况下, rank是通过"为各组分配一个平均排名"的方式破坏平级关系的
```
obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(obj.rank())
'''
0    6.5
1    1.0
2    6.5
3    4.5
4    3.0
5    2.0
6    4.5
dtype: float64
'''
# 出现0.5小数位是因为-5排名1.0. 0排名2.0, 2排名3.0, 出现两个数据4, 可排4.0或5.0, 所以按照平均排名, 4排名4.5. 所以7排名6.5

print(obj.rank(method="first"))
'''
0    6.0
1    1.0
2    7.0
3    4.0
4    3.0
5    2.0
6    5.0
dtype: float64
'''
# 如果使用method="first"参数, 则会按照出现顺序进行排名. 不再计算平均值
# method可选average: 平均排名, min: 分组最小排名, max: 分组最大排名, first: 原始数据顺序排名, dense: 类似min参数, 但是是原rank数据+1
```

# **`ch07`**
### Series的map方法
```
data = {
    "food": ["bacon", "pulled pork", "bacon", "Pastrami", "corned beef", "Bacon", "pastrami", "honey ham", "nova lox"], 
    "ounces": [4, 3, 12, 6, 7.5, 8, 3, 5, 6]
}
data = pd.DataFrame(data)
'''
          food  ounces
0        bacon     4.0
1  pulled pork     3.0
2        bacon    12.0
3     Pastrami     6.0
4  corned beef     7.5
5        Bacon     8.0
6     pastrami     3.0
7    honey ham     5.0
8     nova lox     6.0
'''
# 需要添加一列肉类的来源, 此时可使用Series的map方法映射
meat_to_animal = { "bacon": "pig", "pulled pork": "pig", "pastrami": "cow", "corned beef": "cow", "honey ham": "pig", "nova lox": "salmon"}
data["animal"] = data["food"].str.lower().map(meat_to_animal)

'''
          food  ounces  animal
0        bacon     4.0     pig
1  pulled pork     3.0     pig
2        bacon    12.0     pig
3     Pastrami     6.0     cow
4  corned beef     7.5     cow
5        Bacon     8.0     pig
6     pastrami     3.0     cow
7    honey ham     5.0     pig
8     nova lox     6.0  salmon
'''
```
