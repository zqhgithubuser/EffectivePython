import types
from functools import wraps

TRACE_TYPES = (
    types.MethodType,
    types.FunctionType,
    types.BuiltinFunctionType,
    types.BuiltinMethodType,
    types.MethodDescriptorType,
    types.ClassMethodDescriptorType,
    types.WrapperDescriptorType,
)

IGNORE_METHODS = (
    "__repr__",
    "__str__",
)


def trace_func(func):
    if hasattr(func, "tracing"):
        return func

    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = repr(args)
        kwargs_repr = repr(kwargs)
        result = None
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            result = e
            raise
        finally:
            print(f"{func.__name__}({args_repr}, {kwargs_repr}) -> {result!r}")

    wrapper.tracing = True
    return wrapper


class TraceMeta(type):
    def __new__(cls, name, bases, class_dict):
        klass = super().__new__(cls, name, bases, class_dict)

        for key in dir(klass):
            if key in IGNORE_METHODS:
                continue

            value = getattr(klass, key)
            if not isinstance(value, TRACE_TYPES):
                continue

            wrapped = trace_func(value)
            setattr(klass, key, wrapped)
        return klass


class TraceDict(dict, metaclass=TraceMeta):
    pass


trace_dict = TraceDict([("hi", 1)])
trace_dict["there"] = 2
trace_dict["hi"]  # __getitem__(({'hi': 1, 'there': 2}, 'hi'), {}) -> 1
try:
    trace_dict["does not exist"]
except KeyError:
    pass
