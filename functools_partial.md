### [functools.partial的应用](https://docs.python.org/zh-cn/3.7/library/functools.html?highlight=functools#functools.partial)

## **`官方源码`**
`def partial(func, *args, **keywords):`<br/>
&ensp;&ensp;&ensp;&ensp;`def newfunc(*fargs, **fkeywords):`<br/>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`newkeywords = keywords.copy()`<br/>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`newkeywords.update(fkeywords)`<br/>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`return func(*args, *fargs, **newkeywords)`<br/>
&ensp;&ensp;&ensp;&ensp;`newfunc.func = func`<br/>
&ensp;&ensp;&ensp;&ensp;`newfunc.args = args`<br/>
&ensp;&ensp;&ensp;&ensp;`newfunc.keywords = keywords`<br/>
&ensp;&ensp;&ensp;&ensp;`return newfunc`<br/>

`from functools import partial`<br/>
`basetwo = partial(int, base=2)`<br/>
`basetwo('10010')` -- 18<br/>

### 在某些场景中, 当函数被调用时, 有些参数是已经提前知道或固定的. 这时候可以调用`functools.partial`将该函数和已知参数封装成一个新的函数, 方便后续调用

`def add(x, y, z):`<br/>
&ensp;&ensp;&ensp;&ensp;`return x + y + z`

### 比如当x是固定的100时
`x_add = functools.partial(add, 100)`<br/>
`x_add(1, 2)` -- 103<br/>

### 比如当x, y参数是固定的10, 20时
`x_y_add = functools.partial(add, 10, 20)`<br/>
`x_y_add(30)` -- 60<br/>