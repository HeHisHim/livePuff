from inject import ExecutionContext, ModifyExceptionFromType


def test():
    with ExecutionContext():
        print(1 / 0)


if "__main__" == __name__:
    test()
