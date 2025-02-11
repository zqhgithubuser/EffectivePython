def sort_priority2(numbers, group):
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return 0, x
        else:
            return 1, x

    numbers.sort(key=helper)
    return found


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}

found = sort_priority2(numbers, group)
print("Found:", found)  # Found: True
print(numbers)
