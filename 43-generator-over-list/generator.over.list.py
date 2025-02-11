def index_words(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == " ":
            yield index + 1


address = "Four score and seven years ago..."
result = index_words(address)
print(list(result)[:10])  # [0, 5, 11, 15, 21, 27]
