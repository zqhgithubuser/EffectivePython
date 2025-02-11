import itertools

it = itertools.combinations([1, 2, 3, 4], 2)
print(list(it))  # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
