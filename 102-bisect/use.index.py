data = list(range(10**5))


def find_closest(sequence, goal):
    for index, value in enumerate(sequence):
        if goal < value:
            return index
    raise ValueError(f"{goal} is out of bounds")


index = find_closest(data, 91234.56)
assert index == 91235
