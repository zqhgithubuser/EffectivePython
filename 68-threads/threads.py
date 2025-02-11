import select
import socket
import time
from threading import Thread


def slow_systemcall():
    select.select([socket.socket()], [], [], 0.1)


start = time.perf_counter()

# for _ in range(5):
#     slow_systemcall()

threads = []
for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)


def compute_helicopter_location(index):
    pass


for i in range(5):
    compute_helicopter_location(i)

for thread in threads:
    thread.join()

end = time.perf_counter()
delta = end - start
print(f"Took {delta: .3f} seconds")  # Took  0.106 seconds
