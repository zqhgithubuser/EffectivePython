import timeit


def loop_sum(items):
    total = 0
    for i in items:
        total += i
    return total


count = 1000


delay = timeit.timeit(
    setup="numbers = list(range(10_000))",
    stmt="loop_sum(numbers)",
    globals=globals(),
    number=count,
)

# 求和操作的平均时间
print(f"{delay/count/10_000*1e9: .2f} nanoseconds")  # 46.94 nanoseconds
