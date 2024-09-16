from dataclasses import dataclass


@dataclass
class Stats:
    minimum: float
    maximum: float
    average: float
    median: float
    count: int


lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]


def get_median(numbers):
    count = len(numbers)
    sorted_numbers = sorted(numbers)
    middle = count // 2
    if count % 2 == 0:
        lower = sorted_numbers[middle - 1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]
    return median


def get_stats_obj(numbers):
    return Stats(
        minimum=min(numbers),
        maximum=max(numbers),
        average=sum(numbers) / len(numbers),
        median=sorted(numbers)[len(numbers) // 2],
        count=len(numbers)
    )

result = get_stats_obj(lengths)
print(result)