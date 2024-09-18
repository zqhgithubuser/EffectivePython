stock = {
    "nails": 125,
    "screws": 35,
    "wingnuts": 8,
    "washers": 24,
}

order = ["screws", "wingnuts", "clips"]


def get_batches(count, size):
    return count // size


# result = {
#     name: get_batches(stock.get(name, 0), 8)
#     for name in order
#     if get_batches(stock.get(name, 0), 8)
# }

# 海象运算符
result = {
    name: batch for name in order
    if (batch := get_batches(stock.get(name, 0), 8))
}

print(result)
