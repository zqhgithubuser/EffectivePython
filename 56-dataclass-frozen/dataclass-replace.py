import dataclasses


@dataclasses.dataclass(frozen=True)
class ImmutablePoint:
    name: str
    x: float
    y: float


def translate_dataclass(point, delta_x, delta_y):
    return dataclasses.replace(point, x=point.x + delta_x, y=point.y + delta_y)


origin = ImmutablePoint("origin", 0, 0)
print(origin)  # ImmutablePoint(name='origin', x=0, y=0)
new = translate_dataclass(origin, 3, 4)
print(new)  # ImmutablePoint(name='origin', x=3, y=4)
