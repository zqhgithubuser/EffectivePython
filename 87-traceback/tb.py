import json
import traceback


class Request:
    def __init__(self, body):
        self.body = body
        self.response = None


def do_work(data):
    assert False, data
    ...


def handle(request):
    try:
        do_work(request.body)
    except BaseException as e:
        print(repr(e))
        request.response = 400


def handle2(request):
    try:
        do_work(request.body)
    except BaseException as e:
        traceback.print_tb(e.__traceback__)
        print(repr(e))
        request.response = 400


def handle3(request):
    try:
        do_work(request.body)
    except BaseException as e:
        stack = traceback.extract_tb(e.__traceback__)
        for frame in stack:
            print(frame.name)
        print(repr(e))
        request.response = 400


# request = Request("My message")
# request = Request("My message 2")
request = Request("My message 3")
# handle(request)
# handle2(request)
# handle3(request)


def log_if_error(file_path, target, *args, **kwargs):
    try:
        target(*args, **kwargs)
    except BaseException as e:
        stack = traceback.extract_tb(e.__traceback__)
        stack_without_wrapper = stack[1:]
        trace_dict = dict(
            stack=[item.name for item in stack_without_wrapper],
            error_type=type(e).__name__,
            error_message=str(e),
        )
        json_data = json.dumps(trace_dict)

        with open(file_path, "a") as f:
            f.write(json_data)
            f.write("\n")


log_if_error("my_log.json", do_work, "First error")
log_if_error("my_log.json", do_work, "Second error")

with open("my_log.json") as f:
    for line in f:
        print(line, end="")

