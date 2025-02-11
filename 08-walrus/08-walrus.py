fresh_fruit = {
    "apple": 10,
    "banana": 8,
    "lemon": 5,
}


def make_lemonade(count):
    print(f"Making {count} lemons into lemonade")


def make_cider(count):
    print(f"Making cider with {count} apples")


def out_of_stock():
    print("Out of stock!")


if count := fresh_fruit.get("lemon", 0):
    make_lemonade(count)
else:
    out_of_stock()

if (count := fresh_fruit.get("apple", 0)) >= 4:
    make_cider(count)
else:
    out_of_stock()
