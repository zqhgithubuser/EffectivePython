value = [len(x) for x in open("my_file.txt")]
print(value)  # [292, 288, 192, 232]

it = (len(x) for x in open("my_file.txt"))
print(it)
# print(next(it))  # 292
# print(next(it))  # 288

roots = ((x, x**0.5) for x in it)
print(next(roots))  # (292, 17.08800749063506)
