import traceback


class MissingError(Exception):
    pass


class ServerMissingKeyError(Exception):
    pass


server_dict = {
    "my key 1": "my key 1",
    "my key 2": "my value 2",
    "my key 3": "my value 3",
}

my_dict = {}


def contact_server(my_key):
    print(f"Looking up {my_key!r} in server")
    try:
        return server_dict[my_key]
    except KeyError:
        raise ServerMissingKeyError(my_key)


def lookup(my_key):
    try:
        return my_dict[my_key]
    except KeyError:
        try:
            result = contact_server(my_key)
        except ServerMissingKeyError:
            raise MissingError(my_key)
        else:
            my_dict[my_key] = result
            return result


def lookup_explicit(my_key):
    try:
        return my_dict[my_key]
    except KeyError as e:
        try:
            result = contact_server(my_key)
        except ServerMissingKeyError:
            raise MissingError(my_key) from e
        else:
            my_dict[my_key] = result
            return result


print("Call 1")
print("Result:", lookup("my key 2"))
print("Call 2")
print("Result:", lookup("my key 2"))

# print(lookup("my key 4"))

print("----------------------------------------------------------------------")
try:
    lookup_explicit("my key 5")
except Exception as e:
    print("Exception:", repr(e))
    print("Context:  ", repr(e.__context__))  # ServerMissingKeyError('my key 5')
    print("Cause:    ", repr(e.__cause__))  # KeyError('my key 5')
    print("Suppress: ", repr(e.__suppress_context__))  # True

print("----------------------------------------------------------------------")
try:
    lookup("my key 6")
except Exception as e:
    stack = traceback.extract_tb(e.__traceback__)
    for frame in stack:
        print(frame.line)


def get_cause(exc):
    if exc.__cause__ is not None:
        return exc.__cause__
    elif not exc.__suppress_context__:
        return exc.__context__
    else:
        return None


print("----------------------------------------------------------------------")
try:
    lookup("my key 7")
except Exception as e:
    while e is not None:
        stack = traceback.extract_tb(e.__traceback__)
        for i, frame in enumerate(stack, 1):
            print(i, frame.line)
        e = get_cause(e)
        if e:
            print("Caused by")
