import collections
import timeit


def deque_append_benchmark(count):
    def prepare():
        return collections.deque()

    def run(queue):
        for i in range(count):
            queue.append(i)

    return timeit.timeit(
        setup="queue = prepare()",
        stmt="run(queue)",
        globals=locals(),
        number=1,
    )


for i in range(1, 6):
    count = i * 100_000
    delay = deque_append_benchmark(count)
    print(f"Count {count: >5}, takes: {delay*1e3: >6.2f}ms")


def deque_popleft_benchmark(count):
    def prepare():
        return collections.deque(range(count))

    def run(queue):
        while queue:
            return queue.popleft()

    return timeit.timeit(
        setup="queue = prepare()",
        stmt="run(queue)",
        globals=locals(),
        number=1,
    )


print("----------------------------------------------------------------------")
for i in range(1, 6):
    count = i * 100_000
    delay = deque_popleft_benchmark(count)
    print(f"Count {count: >5}, takes: {delay*1e3: >6.2f}ms")
