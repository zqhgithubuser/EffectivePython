class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


def distance(left, right):
    return ((left.x - right.x) ** 2 + (left.y - right.y) ** 2) ** 0.5


def bad_distance(left, right):
    left.x = -3
    return distance(left, right)


origin1 = Point("source", 0, 0)
point1 = Point("destination", 3, 4)
print(distance(origin1, point1))  # 5.0

print(bad_distance(origin1, point1))  # 7.211102550927978
print(origin1.x)  # -3
