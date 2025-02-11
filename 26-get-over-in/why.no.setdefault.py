data = {}
key = "foo"
value = []

data.setdefault(key, value)

print("Before:", data)  # Before: {'foo': []}
value.append("hello")
print("After: ", data)  # After:  {'foo': ['hello']}
