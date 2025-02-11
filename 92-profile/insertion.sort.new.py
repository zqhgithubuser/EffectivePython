from bisect import bisect_left
from cProfile import Profile
from pstats import Stats
from random import randint


def insertion_sort(data):
    result = []
    for value in data:
        insert_value(result, value)
    return result


def insert_value(array, value):
    i = bisect_left(array, value)
    array.insert(i, value)


max_size = 12**4
data = [randint(0, max_size) for _ in range(max_size)]
test = lambda: insertion_sort(data)

profiler = Profile()
profiler.runcall(test)

stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats("cumulative")
stats.print_stats()

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.079    0.079 insertion.sort.new.py:21(<lambda>)
#         1    0.007    0.007    0.079    0.079 insertion.sort.new.py:7(insertion_sort)
#     20736    0.011    0.000    0.073    0.000 insertion.sort.new.py:14(insert_value)
#     20736    0.051    0.000    0.051    0.000 {method 'insert' of 'list' objects}
#     20736    0.010    0.000    0.010    0.000 {built-in method _bisect.bisect_left}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
