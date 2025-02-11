import json

UNDEFINED = object()


def divide_json(path):
    print("* Opening file")
    handle = open(path, "r+")
    try:
        print("* Reading data")
        data = handle.read()  # May raise OSError
        print("* Loading JSON data")
        op = json.loads(data)  # May raise ValueError
        print("* Performing calculation")
        value = op["numerator"] / op["denominator"]  # May raise ZeroDivisionError
    except ZeroDivisionError:
        print("* Handling ZeroDivisionError")
        return UNDEFINED
    else:
        print("* Writing calculation")
        op["result"] = value
        result = json.dumps(op)
        handle.seek(0)  # May raise OSError
        handle.write(result)  # May raise OSError
        return value
    finally:
        print("* Calling close()")
        handle.close()


temp_path = "random_data.json"

with open(temp_path, "w") as f:
    f.write('{"numerator": 1, "denominator": 10}')

assert divide_json(temp_path) == 0.1

print("----------------------------------------------------------------------")
with open(temp_path, "w") as f:
    f.write('{"numerator": 1, "denominator": 0}')

assert divide_json(temp_path) == UNDEFINED

print("----------------------------------------------------------------------")
with open(temp_path, "w") as f:
    f.write('{"numerator": 1 bad data')

divide_json(temp_path)
