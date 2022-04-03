VAL = 100
VAL_LIST = [100]


def alter_global():
    """
    当全局变量指向的对象不可变时，比如是整型、字符串等等，如果你尝试在函数内部改变它的值，却不加关键字 global，就会抛出异常
    这是因为程序认为函数内部的 VAL += 100 改变了外部变量 VAL 的地址
    """
    VAL += 100  # UnboundLocalError: local variable 'VAL' referenced before assignment

    """
    不过，如果全局变量指向的对象是可变的，比如是列表、字典等等，你就可以在函数内部修改它了
    这里的VAL_LIST.append(200)并没有改变VAL_LIST, VAL_LIST仍然指向原来的列表

    >> 全局列表 VAL_LIST 之所以可以在函数中VAL_LIST.append是因为VAL_LIST指向的列表不变
        但是如果列表中的元素超过了列表预留的空间就会重新开启一个更大的列表VAL_LIST指向这个新的列表
        这个时候VAL_LIST不也变了吗? 为什么还能在函数中使用?
    >> 因为VAL_LIST的append()并不是一个赋值操作，不会去定义新的变量
       即时对列表进行扩容, 该列表的首地址仍然不变, 因为python的list类型本质是链表
    """
    VAL_LIST.append(200)


if "__main__" == __name__:
    alter_global()
    print(VAL)
    print(VAL_LIST)
