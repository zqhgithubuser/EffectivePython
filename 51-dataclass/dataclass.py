from dataclasses import dataclass, astuple, asdict


class RGB:

    def __init__(self, red: int, green: int, blue: int, alpha: float = 1.0) -> None:
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha


@dataclass(order=True)
class DataclassRGB:
    red: int
    green: int
    blue: int
    alpha: float = 1.0


color1 = DataclassRGB(red=1, green=2, blue=3)
color2 = DataclassRGB(5, 6, 7)
print(color1)  # DataclassRGB(red=1, green=2, blue=3, alpha=1.0)
print(astuple(color1))  # (1, 2, 3, 1.0)
print(asdict(color1))  # {'red': 1, 'green': 2, 'blue': 3, 'alpha': 1.0}

print(color1 == color2)
print(color1 != color2)
print(color1 is color2)
print(color1 is not color2)
