class Node:

    def evaluate(self):
        raise NotImplementedError


class IntegerNode(Node):

    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value


class AddNode(Node):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()


class MultiplyNode(Node):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()


tree = MultiplyNode(
    AddNode(IntegerNode(3), IntegerNode(5)),
    AddNode(IntegerNode(4), IntegerNode(7))
)

print(tree.evaluate())