import random


def flip_coin():
    if random.randint(0, 1) == 0:
        return "Heads"
    else:
        return "Tails"


def flip_is_heads():
    return flip_coin() == "Heads"


def flip_is_tails():
    return flip_coin() == "Tails"


# 循环
all_heads = True
for i in range(20):
    if not flip_is_heads():
        all_heads = False
        break
print(all_heads)

# all: 一旦遇到False则返回False
all_heads = all(flip_is_heads() for i in range(20))
print(all_heads)

# any: 一旦遇到True则返回True
all_heads = not any(flip_is_tails() for i in range(20))
print(all_heads)