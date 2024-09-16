import json

# def decode(data, default={}):
#     try:
#         return json.loads(data)
#     except ValueError:
#         return default


def decode(data, default=None):
    """Load JSON data from a string.
    """
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default


foo = decode("bad data")
foo["stuff"] = 5
bar = decode("also bad")
bar["meep"] = 1
print("Foo:", foo)
print("Bar:", bar)
