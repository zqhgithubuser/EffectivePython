import random
import time


def check_for_reset():
    return random.choice([True, False])


def announce(remaining):
    print(f"{remaining} ticks remaining")


class Timer():

    def __init__(self, period):
        self.period = period
        self.current = period

    def reset(self):
        print("Resetting")
        self.current = self.period

    def tick(self):
        before = self.current
        self.current -= 1
        return before

    def __bool__(self):
        return self.current > 0


def run():
    timer = Timer(4)
    while timer:
        if check_for_reset():
            timer.reset()
            time.sleep(1)
        announce(timer.tick())


run()
