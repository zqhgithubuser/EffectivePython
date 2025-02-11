import json


# 对象转化为字典
class ToDictMixin:

    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, "__dict__"):
            return self._traverse_dict(value.__dict__)
        else:
            return value


class BinaryTree(ToDictMixin):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTreeWithParent(BinaryTree):

    def __init__(
        self,
        value,
        left=None,
        right=None,
        parent=None,
    ):
        super().__init__(value, left, right)
        self.parent = parent

    # 重写函数，处理新的情况
    def _traverse(self, key, value):
        if isinstance(value, BinaryTreeWithParent) and key == "parent":
            return value.value
        else:
            return super()._traverse(key, value)


class JsonMixin:

    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)
        return cls(**kwargs)

    def to_json(self):
        return json.dumps(self.to_dict(), indent=2)


class DatacenterRack(ToDictMixin, JsonMixin):

    def __init__(self, switch=None, machines=None):
        self.switch = Switch(**switch)
        self.machines = [Machine(**kwargs) for kwargs in machines]


class Switch(ToDictMixin, JsonMixin):

    def __init__(self, ports=None, speed=None):
        self.ports = ports
        self.speed = speed


class Machine(ToDictMixin, JsonMixin):

    def __init__(self, cores=None, ram=None, disk=None):
        self.cores = cores
        self.ram = ram
        self.disk = disk


tree = BinaryTree(
    10,
    left=BinaryTree(7, right=BinaryTree(9)),
    right=BinaryTree(13, left=BinaryTree(11)),
)

print(tree.__dict__)
output = tree.to_dict()
print(output)

# print(json.dumps(output, indent=2))
# {
#   "value": 10,
#   "left": {
#     "value": 7,
#     "left": null,
#     "right": {
#       "value": 9,
#       "left": null,
#       "right": null
#     }
#   },
#   "right": {
#     "value": 13,
#     "left": {
#       "value": 11,
#       "left": null,
#       "right": null
#     },
#     "right": null
#   }
# }

root = BinaryTreeWithParent(10)
root.left = BinaryTreeWithParent(7, parent=root)
root.left.right = BinaryTreeWithParent(9, parent=root.left)
output = root.to_dict()
# print(json.dumps(output, indent=2))

serialized = """\
{
    "switch": {"ports": 5, "speed": 1e9},
    "machines": [
        {"cores": 8, "ram": 32e9, "disk": 5e12},
        {"cores": 4, "ram": 16e9, "disk": 1e12},
        {"cores": 2, "ram": 4e9, "disk": 500e9}
    ]
}
"""

deserialized = DatacenterRack.from_json(serialized)
# print(deserialized)
roundtrip = deserialized.to_json()
# print(roundtrip)

# {
#   "switch": {
#     "ports": 5,
#     "speed": 1000000000.0
#   },
#   "machines": [
#     {
#       "cores": 8,
#       "ram": 32000000000.0,
#       "disk": 5000000000000.0
#     },
#     {
#       "cores": 4,
#       "ram": 16000000000.0,
#       "disk": 1000000000000.0
#     },
#     {
#       "cores": 2,
#       "ram": 4000000000.0,
#       "disk": 500000000000.0
#     }
#   ]
# }

