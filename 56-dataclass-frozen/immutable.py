from dataclasses import dataclass


@dataclass(frozen=True)
class DataclassImmutablePoint:
    name: str
    x: float
    y: float


origin = DataclassImmutablePoint("origin", 0, 0)
origin.x = -3  # dataclasses.FrozenInstanceError: cannot assign to field 'x'
