import json


class Serializable:

    def __init__(self, *args):
        self.args = args

    # 序列化
    def serialize(self):
        return json.dumps(
            {
                "class": self.__class__.__name__,
                "args": self.args
            },
            indent=2
        )

    def __repr__(self):
        name = self.__class__.__name__
        args_str = ", ".join([str(arg) for arg in self.args])
        return f"{name}({args_str})"


REGISTRY = {}


def register_class(target_class):
    REGISTRY[target_class.__name__] = target_class

# 反序列化
def deserialize(data):
    params = json.loads(data)
    name = params["class"]
    target_class = REGISTRY[name]
    return target_class(*params["args"])  # 创建对象


class RegisteredSerializable(Serializable):

    def __init_subclass__(cls):
        super().__init_subclass__()
        register_class(cls)

# 创建类时自动注册
class Point2D(RegisteredSerializable):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        

before = Point2D(5, 3)
print("Before:    ", before)
# object -> json
data = before.serialize()
print("Searialze: ", data)
# json -> object
after = deserialize(data)
print("After:     ", after)
