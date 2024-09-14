my_tree = (10, (7, None, 9), (13, 11, None))


def contains(tree, value):
    if not isinstance(tree, tuple):
        return tree == value

    pivot, left, right = tree

    if value < pivot:
        return contains(left, value)
    elif value > pivot:
        return contains(right, value)
    else:
        return pivot == value


print(contains(my_tree, 9))
print(contains(my_tree, 14))


# match语句：解构
def contains_match(tree, value):
    match tree:
        case pivot, left, _ if value < pivot:
            return contains_match(left, value)
        case pivot, _, right if value > pivot:
            return contains_match(right, value)
        case (pivot, _, _) | pivot:
            return value == pivot


print(contains_match(my_tree, 9))
print(contains_match(my_tree, 14))