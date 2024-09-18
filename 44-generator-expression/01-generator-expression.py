value = [len(x) for x in open("my_file.txt")]
print(value)

it = (len(x) for x in open("my_file.txt"))
print(it)
print(next(it))