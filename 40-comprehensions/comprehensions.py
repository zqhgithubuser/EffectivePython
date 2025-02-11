a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map, filter
alt = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, a)))
print(alt)  # [4, 16, 36, 64, 100]

# 列表推导式
even_squares = [x * x for x in a if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]
