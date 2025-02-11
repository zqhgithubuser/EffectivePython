import itertools

it1, it2, it3 = itertools.tee(["first", "second"], 3)
print(list(it1))  # ['first', 'second']
print(list(it2))  # ['first', 'second']
print(list(it3))  # ['first', 'second']
