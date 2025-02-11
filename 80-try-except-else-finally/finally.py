def try_finally_example(filename):
    print("* Opening file")
    handle = open(filename, encoding="utf-8")
    try:
        print("* Reading data")
        return handle.read()
    finally:
        print("* Calling close()")
        handle.close()


filename = "random_data.txt"

with open(filename, "wb") as f:
    f.write(b"\xf1\xf2\xf3\xf4\xf5")  # Invalid utf-8

data = try_finally_example(filename)
