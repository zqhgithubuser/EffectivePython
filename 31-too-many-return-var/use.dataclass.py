from dataclasses import dataclass


@dataclass
class Stats:
    minimum: float
    maximum: float
    average: float
    median: float
    count: int


lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]


def get_stats_obj(numbers):
    return Stats(
        minimum=min(numbers),
        maximum=max(numbers),
        average=sum(numbers) / len(numbers),
        median=sorted(numbers)[len(numbers) // 2],
        count=len(numbers),
    )


result = get_stats_obj(lengths)
print(result)  # Stats(minimum=60, maximum=73, average=67.5, median=70, count=10)
