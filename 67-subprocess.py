import subprocess
import time

start = time.perf_counter()

sleep_procs = []
for _ in range(10):
    proc = subprocess.Popen(["sleep", "1"])
    sleep_procs.append(proc)

for proc in sleep_procs:
    proc.communicate()

end = time.perf_counter()
delta = end - start
print(f"Finished in {delta:.3} seconds")
