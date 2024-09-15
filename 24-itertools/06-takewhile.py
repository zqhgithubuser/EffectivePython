import itertools

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 函数返回False时停止
it = itertools.takewhile(lambda x: x < 7, values)
print(list(it))

# 函数返回True时跳过
it = itertools.dropwhile(lambda x: x < 7, values)
print(list(it))
