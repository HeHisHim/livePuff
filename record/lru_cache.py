from collections import OrderedDict
import functools


def lru_cache(size):
    def decorating_function(func):
        cache = OrderedDict()

        @functools.wraps(func)
        def wraps(*args, **kwargs):
            print(cache)
            target = object()
            if kwargs:
                key = args + (repr(sorted(kwargs.items())),)
            else:
                key = args
            res = cache.get(key, target)
            if res is not target:
                val = cache.pop(key)
                cache[key] = val
                print("hit cache")
                return val
            val = func(*args, **kwargs)
            if len(cache) == size:
                print("cache size full")
                cache.popitem(last=False)
            cache[key] = val
            return val

        return wraps

    return decorating_function


@lru_cache(3)
def test_lru(*args, **kwargs):
    print("test_lru: {} - {}".format(args, kwargs))


@lru_cache(4)
def test_lru2(*args, **kwargs):
    print(args, kwargs)


if "__main__" == __name__:
    test_lru(123, bbc=123)
    test_lru(223, bbc=123)
    test_lru(323, bbc=123)
    test_lru(423, bbc=123)
    test_lru(323, bbc=123)
    test_lru2(123, ccd=321)
