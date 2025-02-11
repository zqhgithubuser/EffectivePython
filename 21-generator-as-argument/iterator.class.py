def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = value * 100 / total
        result.append(percent)
    return result


class ReadVisits:

    def __init__(self, data_path):
        self.data_path = data_path

    # 返回迭代器对象
    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


visits = ReadVisits("my_numbers.txt")
percentages = normalize(visits)
print(percentages)
