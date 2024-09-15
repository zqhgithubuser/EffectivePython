import itertools

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filter_result = filter(lambda x: x % 2 == 0, values)
print("Filter:      ", list(filter_result))

filter_false_result = itertools.filterfalse(lambda x: x % 2 == 0, values)
print(f"Filter false: {list(filter_false_result)}")
