from bisect import bisect_left

data = list(range(10**5))
index = bisect_left(data, 91234)
assert index == 91234

index = bisect_left(data, 91234.56)
assert index == 91235
