def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = value * 100 / total
        result.append(percent)
    return result

# 副本
def normalize_copy(numbers):
    numbers_copy = list(numbers)
    total = sum(numbers_copy)
    result = []
    for value in numbers_copy:
        percent = value * 100 / total
        result.append(percent)
    return result

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

it = read_visits("my_numbers.txt")
# percentages = normalize(it)
percentages = normalize_copy(it)
print(percentages)