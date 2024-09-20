class Integer:

    def __init__(self, value):
        self.value = value


class Add:

    def __init__(self, left, right):
        self.left = left
        self.right = right


class Multiply:

    def __init__(self, left, right):
        self.left = left
        self.right = right


def evaluate(node):
    if isinstance(node, Integer):
        return node.value
    elif isinstance(node, Add):
        return evaluate(node.left) + evaluate(node.right)
    elif isinstance(node, Multiply):
        return evaluate(node.left) * evaluate(node.right)
    else:
        raise NotImplementedError


tree = Add(Integer(2), Integer(9))
print(evaluate(tree))

tree = Multiply(
    Add(Integer(3), Integer(5)),
    Add(Integer(4), Integer(7)),
)
print(evaluate(tree))
