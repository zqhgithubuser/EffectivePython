from cProfile import Profile
from pstats import Stats
from random import randint


def insertion_sort(data):
    result = []
    for value in data:
        insert_value(result, value)
    return result


def insert_value(array, value):
    for i, existing in enumerate(array):
        if existing > value:
            array.insert(i, value)
            return
    array.append(value)


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
#         1    0.000    0.000    8.835    8.835 insertion.sort.py:23(<lambda>)
#         1    0.012    0.012    8.835    8.835 insertion.sort.py:6(insertion_sort)
#     20736    8.759    0.000    8.823    0.000 insertion.sort.py:13(insert_value)
#     20723    0.064    0.000    0.064    0.000 {method 'insert' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        13    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
