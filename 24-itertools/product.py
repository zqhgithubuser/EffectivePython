import itertools

single = itertools.product([1, 2], repeat=2)
print("Single:  ", list(single))

multiple = itertools.product([1, 2], ["a", "b"])
print("Multiple:", list(multiple))
