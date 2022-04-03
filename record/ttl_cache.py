import functools
import time


def ttl_cache(ttl):
    def decorating_function(func):
        cache = {}

        @functools.wraps(func)
        def wraps(*args, **kwargs):
            target = object()
            if kwargs:
                key = args + (repr(sorted(kwargs.items())),)
            else:
                key = args
            print("key: {}".format(key))
            result = cache.get(key, target)
            if result is not target:
                expire_at, value = result
                if expire_at > time.time():
                    print("hit cache: {}".format(expire_at))
                    return value
            value = func(*args, **kwargs)
            print("miss cache")
            cache[key] = (time.time() + ttl, value)
            return value

        return wraps

    return decorating_function


"""
rqdata的ttl_cache装饰器
"""
# def ttl_cache(ttl):
#     if not isinstance(ttl, int) or not ttl > 0:
#         raise TypeError("Expected ttl to be a positive integer")

#     def decorating_function(user_function):
#         wrapper = _ttl_cache_wrapper(user_function, ttl)
#         # return functools.update_wrapper(wrapper, user_function)
#         return wrapper
#     return decorating_function

# def _ttl_cache_wrapper(user_function, ttl):
#     sentinel = object()
#     cache = {}
#     cache_get = cache.get  # bound method to lookup a key or return None
#     def wrapper(*args, **kwargs):
#         if kwargs:
#             key = args + (repr(sorted(kwargs.items())),)
#         else:
#             key = args

#         # in cpython, dict.get is thread-safe
#         result = cache_get(key, sentinel)
#         if result is not sentinel:
#             expire_at, value = result
#             if expire_at > time.time():
#                 print("hit cache: {}".format(expire_at))
#                 return value
#         value = user_function(*args, **kwargs)
#         print("miss cache")
#         cache[key] = (time.time() + ttl, value)
#         return value

#     return wrapper


@ttl_cache(30)
def test_ttl(*args, **kwargs):
    print("test_ttl: {} - {}".format(args, kwargs))


if "__main__" == __name__:
    test_ttl(123, bbc=123)
    test_ttl(123, bbc=123)
