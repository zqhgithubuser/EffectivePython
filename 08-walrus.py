fresh_fruit = {
    "apple": 10,
    "banana": 8,
    "lemon": 5,
}


def make_lemonade(count):
    ...


def make_cider(count):
    ...


def out_of_stock():
    ...


if count := fresh_fruit.get("lemon", 0):
    print("making lemonade...")
    make_lemonade(count)
else:
    out_of_stock()

if (count := fresh_fruit.get("apple", 0)) >= 4:
    print("making cider...")
    make_cider(count)
else:
    out_of_stock()
