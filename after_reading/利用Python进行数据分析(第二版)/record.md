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
