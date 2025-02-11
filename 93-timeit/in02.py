import random
import timeit

count = 100_000

delay = timeit.timeit(
    setup="""
numbers = set(range(10_000))
probe = 7_777
    """,
    stmt="""
probe in numbers
    """,
    globals=globals(),
    number=count,
)

print(f"{delay/count*1e9: .2f} nanoseconds")  # 36.39 nanoseconds
