class Node:

    def evaluate(self):
        raise NotImplementedError

    def pretty(self):
        raise NotImplementedError


class IntegerNode(Node):

    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

    def pretty(self):
        return repr(self.value)


class AddNode(Node):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

    def pretty(self):
        left_str = self.left.pretty()
        right_str = self.right.pretty()
        return f"({left_str} + {right_str})"


class MultiplyNode(Node):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()

    def pretty(self):
        left_str = self.left.pretty()
        right_str = self.right.pretty()
        return f"({left_str} * {right_str})"


tree = MultiplyNode(
    AddNode(IntegerNode(3), IntegerNode(5)), AddNode(IntegerNode(4), IntegerNode(7))
)

print(tree.evaluate())  # 88
print(tree.pretty())  # ((3 + 5) * (4 + 7))
