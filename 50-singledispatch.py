import functools


@functools.singledispatch
def my_evaluate(node):
    raise NotImplementedError


@functools.singledispatch
def my_pretty(node):
    raise NotImplementedError


########################################
class Integer:

    def __init__(self, value):
        self.value = value

# 向类添加方法，而无需修改类
@my_evaluate.register(Integer)
def _(node):
    return node.value


@my_pretty.register(Integer)
def _(node):
    return repr(node.value)


########################################
class Add:

    def __init__(self, left, right):
        self.left = left
        self.right = right


@my_evaluate.register(Add)
def _(node):
    left = my_evaluate(node.left)
    right = my_evaluate(node.right)
    return left + right


@my_pretty.register(Add)
def _(node):
    left_str = my_pretty(node.left)
    right_str = my_pretty(node.right)
    return f'({left_str} + {right_str})'


########################################
class Multiply:

    def __init__(self, left, right):
        self.left = left
        self.right = right


@my_evaluate.register(Multiply)
def _(node):
    left = my_evaluate(node.left)
    right = my_evaluate(node.right)
    return left * right


@my_pretty.register(Multiply)
def _(node):
    left_str = my_pretty(node.left)
    right_str = my_pretty(node.right)
    return f'({left_str} * {right_str})'


tree = Multiply(
    Add(Integer(3), Integer(5)),
    Add(Integer(4), Integer(7)),
)

print(my_pretty(tree))
result = my_evaluate(tree)
print(result)
