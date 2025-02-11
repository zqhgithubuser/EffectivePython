import functools
import sys


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except BaseException as e:
            result = e
            raise
        finally:
            print(f"Called {func.__name__}(*{args!r}, **{kwargs!r}) got {result!r}")

    return wrapper


@log
def my_func(x):
    if x > 0:
        sys.exit(1)
    x / 0


my_func(123)
