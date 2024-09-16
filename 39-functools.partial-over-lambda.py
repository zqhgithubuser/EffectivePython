import math
import functools


def logn_sum(logn_total, value, *, base):
    logn_value = math.log(value, base)
    return logn_total + logn_value


# result = functools.reduce(
#     lambda total, value: logn_sum(total, value, base=10),
#     [10, 20, 40],
#     0
# )

# 固定原函数部分参数的基础上，创建新的函数
result = functools.reduce(
    functools.partial(logn_sum, base=10),
    [10, 20, 40],
    0
)

print(math.pow(10, result))
