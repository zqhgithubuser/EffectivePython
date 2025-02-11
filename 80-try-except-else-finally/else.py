import json


def load_json_key(data, key):
    try:
        print("* Loading JSON data")
        result_dict = json.loads(data)
    except ValueError:
        print("* Handling ValueError")
        raise KeyError(key)
    else:
        print("* Looking up key")
        return result_dict[key]


assert load_json_key('{"foo": "bar"}', "foo") == "bar"

# load_json_key('{"foo": bad payload', "foo")  # KeyError: 'foo'

load_json_key('{"foo": "bar"}', "does not exist")
