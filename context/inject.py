import codecs
import six


class ExecutionContext:
    def __init__(self, filename="strategy.py"):
        self.filename = filename
        with codecs.open(filename=filename, encoding="utf-8") as f:
            self.source_code = f.read()

    def doit(self):
        code = compile(self.source_code, self.filename, "exec")
        six.exec_(code)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Restore the algo instance stored in __enter__.
        """
        print("exc_type: {}".format(exc_type))
        print("exc_val: {}".format(exc_val))
        print("exc_tb: {}".format(exc_tb))


class ModifyExceptionFromType:
    def __init__(self, force=False):
        self.force = force

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            # exc_from_type = getattr(exc_val, EXC_EXT_NAME, const.EXC_TYPE.NOTSET)
            # if self.force or exc_from_type == const.EXC_TYPE.NOTSET:
            #     setattr(exc_val, EXC_EXT_NAME, self.exc_from_type)
            print("ModifyExceptionFromType")


if "__main__" == __name__:
    with ExecutionContext() as context:
        with ModifyExceptionFromType():
            context.doit()
