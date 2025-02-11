import random
import timeit


def list_overdue_benchmark(count):
    def prepare():
        to_add = list(range(count))
        random.shuffle(to_add)
        return [], to_add

    def run(queue, to_add):
        for i in to_add:
            queue.append(i)
            queue.sort(reverse=True)
        while queue:
            queue.pop()

    return timeit.timeit(
        setup="queue, to_add = prepare()",
        stmt="run(queue, to_add)",
        globals=locals(),
        number=1,
    )


for i in range(1, 6):
    count = i * 1_000
    delay = list_overdue_benchmark(count)
    print(f"Count {count: >5}, takes: {delay*1e3: >6.2f}ms")


def list_return_benchmark(count):
    def prepare():
        queue = list(range(count))
        random.shuffle(queue)

        to_return = list(range(count))
        random.shuffle(to_return)

        return queue, to_return

    def run(queue, to_return):
        for i in to_return:
            queue.remove(i)

    return timeit.timeit(
        setup="queue, to_return = prepare()",
        stmt="run(queue, to_return)",
        globals=locals(),
        number=1,
    )


print("----------------------------------------------------------------------")
for i in range(1, 6):
    count = i * 1_000
    delay = list_return_benchmark(count)
    print(f"Count {count: >5}, takes: {delay*1e3: >6.2f}ms")
