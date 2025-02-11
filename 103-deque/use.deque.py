import collections
from collections import deque


class Email:
    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message


def get_emails():
    yield Email("foo@example.com", "bar@example.com", "hello1")
    yield Email("baz@example.com", "banana@example.com", "hello2")
    yield None
    yield Email("meep@example.com", "butter@example.com", "hello3")
    yield Email("stuff@example.com", "avocado@example.com", "hello4")
    yield None
    yield Email("thingy@example.com", "orange@example.com", "hello5")
    yield Email("roger@example.com", "bob@example.com", "hello6")
    yield None
    yield Email("peanut@example.com", "alice@example.com", "hello7")
    yield None


EMAIL_IT = get_emails()


class NoEmailError(Exception):
    pass


def try_receive_email():
    try:
        email = next(EMAIL_IT)
    except StopIteration:
        email = None

    if not email:
        raise NoEmailError

    print(f"Produced email: {email.message}")
    return email


def produce_emails(queue):
    while True:
        try:
            email = try_receive_email()
        except NoEmailError:
            return
        else:
            queue.append(email)  # Producer


def consume_one_email(queue):
    if not queue:
        return
    email = queue.popleft()  # Consumer
    print(f"Consumed email: {email.message}")


def loop(queue, keep_running):
    while keep_running():
        produce_emails(queue)
        consume_one_email(queue)


def make_test_end():
    count = list(range(10))

    def func():
        if count:
            count.pop()
            return True
        return False

    return func


my_end_func = make_test_end()
loop(collections.deque(), my_end_func)
