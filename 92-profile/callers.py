from cProfile import Profile
from pstats import Stats


def my_utility(a, b):
    c = 1
    for i in range(100):
        c += a * b


def first_func():
    for _ in range(1000):
        my_utility(4, 5)


def second_func():
    for _ in range(10):
        my_utility(1, 3)


def my_program():
    for _ in range(20):
        first_func()
        second_func()


profiler = Profile()
profiler.runcall(my_program)

stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats("cumulative")
stats.print_callers()

# Function                                          was called by...
#                                                       ncalls  tottime  cumtime
# callers.py:20(my_program)                         <-
# callers.py:10(first_func)                         <-      20    0.008    0.170  callers.py:20(my_program)
# callers.py:4(my_utility)                          <-   20000    0.161    0.161  callers.py:10(first_func)
#                                                          200    0.001    0.001  callers.py:15(second_func)
# callers.py:15(second_func)                        <-      20    0.000    0.001  callers.py:20(my_program)
# {method 'disable' of '_lsprof.Profiler' objects}  <-


stats.print_callees()

# Function                                          called...
#                                                       ncalls  tottime  cumtime
# callers.py:21(my_program)                         ->      20    0.006    0.146  callers.py:11(first_func)
#                                                           20    0.000    0.001  callers.py:16(second_func)
# callers.py:11(first_func)                         ->   20000    0.139    0.139  callers.py:5(my_utility)
# callers.py:5(my_utility)                          ->
# callers.py:16(second_func)                        ->     200    0.001    0.001  callers.py:5(my_utility)
# {method 'disable' of '_lsprof.Profiler' objects}  ->
