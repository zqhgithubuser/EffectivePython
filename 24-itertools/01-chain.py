import itertools

it = itertools.chain([1, 2, 3], [4, 5, 6])
print(list(it))

it1 = [i * 3 for i in ("a", "b", "c")]
it2 = [i * 2 for i in ("a", "b", "c")]
nested_it = [it1, it2]
output_it = itertools.chain.from_iterable(nested_it)
print(list(output_it))
