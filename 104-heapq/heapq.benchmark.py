import random
import timeit
from heapq import heappop, heappush


def heap_overdue_benchmark(count):
    def prepare():
        to_add = list(range(count))
        random.shuffle(to_add)
        return [], to_add

    def run(queue, to_add):
        for i in to_add:
            heappush(queue, i)
        while queue:
            heappop(queue)

    return timeit.timeit(
        setup="queue, to_add = prepare()",
        stmt="run(queue, to_add)",
        globals=locals(),
        number=1,
    )


for i in range(1, 6):
    count = i * 1_000
    delay = heap_overdue_benchmark(count)
    print(f"Count {count: >5}, takes: {delay*1e3: >6.2f}ms")
