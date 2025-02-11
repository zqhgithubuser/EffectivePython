import math
import functools


def log_sum(log_total, value, *, base):
    log_value = math.log(value, base)
    return log_total + log_value


result = functools.reduce(
    lambda total, value: log_sum(total, value, base=10), [10, 20, 40], 0
)
print(math.exp(result))  # 49.555338121522816

# 固定原函数部分参数的基础上，创建新的函数
result = functools.reduce(functools.partial(log_sum, base=10), [10, 20, 40], 0)

print(math.pow(10, result))  # 8000.000000000004
