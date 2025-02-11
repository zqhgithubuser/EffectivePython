import itertools

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_reduce = itertools.accumulate(values)
print("Sum:   ", list(sum_reduce))  # [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]


def sum_modulo_20(first, second):
    output = first + second
    return output % 20


modulo_reduce = itertools.accumulate(values, sum_modulo_20)
print("Modulo:", list(modulo_reduce))  # [1, 3, 6, 10, 15, 1, 8, 16, 5, 15]
