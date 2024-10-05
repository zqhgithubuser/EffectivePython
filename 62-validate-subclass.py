class Polygon(type):
    sides = None

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.sides < 3:
            raise ValueError("Polygons need 3+ sides")

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 100


class Filled:
    color = None

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.color not in ("red", "gren", "blue"):
            raise ValueError("Fills need a valid color")


class Hexagon(Polygon):
    sides = 6


# print("Before class")

# class Point(Polygon):
#     sides = 1  # ValueError: Polygons need 3+ sides

# print("After class")


class RedTriangle(Filled, Polygon):
    color = "red"
    sides = 3


# print("Before class")

# class BlueLine(Filled, Polygon):
#     color = "blue"
#     sides = 2  # ValueError: Polygons need 3+ sides

# print("After class")

print("Before class")


class BeigeSquare(Filled, Polygon):
    color = "beige"  # ValueError: Fills need a valid color
    sides = 4


print("After class")
