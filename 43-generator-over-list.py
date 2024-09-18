def index_words(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == " ":
            yield index + 1
    return result


address = "Four score and seven years ago..."
result = index_words(address)
print(list(result)[:10])
