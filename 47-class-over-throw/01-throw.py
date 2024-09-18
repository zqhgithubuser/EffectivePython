import random
import time


class Reset(Exception):
    pass


def timer(period):
    current = period
    while current:
        try:
            yield current
        except Reset:
            print("Resetting")
            current = period
        else:
            current -= 1


def check_for_reset():
    return random.choice([True, False])


def announce(remaining):
    print(f"{remaining} ticks remaining")


def run():
    it = timer(4)
    next(it)
    while True:
        try:
            if check_for_reset():
                current = it.throw(Reset())
                time.sleep(1)
            else:
                current = next(it)
        except StopIteration:
            break
        else:
            announce(current)


run()
