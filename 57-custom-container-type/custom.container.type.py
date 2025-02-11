from collections.abc import Sequence


class BinaryNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class IndexableNode(BinaryNode):

    def _traverse(self):
        if self.left is not None:
            yield from self.left._traverse()
        yield self
        if self.right is not None:
            yield from self.right._traverse()

    def __getitem__(self, index):
        for i, item in enumerate(self._traverse()):
            if index == i:
                return item.value
        raise IndexError(f"Index {index} is out of range")


class SequenceNode(IndexableNode):

    def __len__(self):
        count = 0
        for _ in self._traverse():
            count += 1
        return count


tree = IndexableNode(
    10,
    left=IndexableNode(
        5,
        left=IndexableNode(2),
        right=IndexableNode(6, right=IndexableNode(7)),
    ),
    right=IndexableNode(15, left=IndexableNode(11)),
)

print("LRR is", tree.left.right.right.value)  # LRR is 7
print("Index 0 is", tree[0])  # Index 0 is 2
print("Index 1 is", tree[1])  # Index 1 is 5
print("11 in the tree?", 11 in tree)  # 11 in the tree? True
print("17 in the tree?", 17 in tree)  # 17 in the tree? False
print("Tree is", list(tree))  # Tree is [2, 5, 6, 7, 10, 11, 15]
# print("Tree length is", len(tree)) # TypeError: object of type 'IndexableNode' has no len()

tree = SequenceNode(
    10,
    left=SequenceNode(
        5,
        left=SequenceNode(2),
        right=SequenceNode(6, right=SequenceNode(7)),
    ),
    right=SequenceNode(15, left=SequenceNode(11)),
)

print("Tree length is", len(tree))  # Tree length is 7


class BetterNode(SequenceNode, Sequence):
    pass


tree = BetterNode(
    10,
    left=BetterNode(
        5,
        left=BetterNode(2),
        right=BetterNode(6, right=BetterNode(7)),
    ),
    right=BetterNode(15, left=BetterNode(11)),
)

# 抽象基类实现了额外的方法
print("Index of 7 is", tree.index(7))  # Index of 7 is 3
print("Count of 10 is", tree.count(10))  # Count of 10 is 1
