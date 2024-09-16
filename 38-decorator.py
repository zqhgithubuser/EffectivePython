from functools import wraps


def trace(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = repr(args)
        kwargs_repr = repr(kwargs)
        length = kwargs.get("depth", 0)
        indent = "\t" * length
        print(f"{indent}调用: "
              f"{func.__name__}"
              f"({args_repr}, {kwargs_repr})")
        result = func(*args, **kwargs)
        print(f"{indent}返回: "
              f"{func.__name__}"
              f"({args_repr}, {kwargs_repr}) "
              f"-> {result!r}")
        return result

    return wrapper


@trace
def fibonacci(n, depth=0):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return fibonacci(n - 2, depth=depth + 1) + fibonacci(n - 1,
                                                         depth=depth + 1)


fibonacci(4)
