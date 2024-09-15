import itertools

it = itertools.cycle([1, 2])
result = [next(it) for _ in range(10)]
print(result)
