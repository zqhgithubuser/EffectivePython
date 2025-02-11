import itertools

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_five = itertools.islice(values, 5)
print("First five: ", list(first_five))  # [1, 2, 3, 4, 5]

middle_odds = itertools.islice(values, 2, 8, 2)
print(f"Middle odds: {list(middle_odds)}")  # [3, 5, 7]
