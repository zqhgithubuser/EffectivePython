import itertools

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_five = itertools.islice(values, 5)
print("First five: ", list(first_five))

middle_odds = itertools.islice(values, 2, 8, 2)
print(f"Middle odds: {list(middle_odds)}")