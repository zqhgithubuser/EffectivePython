import time
from datetime import datetime, timezone

now = datetime(2024, 3, 10, 5, 17, 45)
now_utc = now.replace(tzinfo=timezone.utc)
print(now_utc)  # 2024-03-10 05:17:45+00:00
# utc -> local time
now_local = now_utc.astimezone()
print(now_local)  # 2024-03-10 13:17:45+08:00

time_str = "2024-03-09 21:17:45"
time_format = "%Y-%m-%d %H:%M:%S"
now = datetime.strptime(time_str, time_format)
time_tuple = now.timetuple()
utc_now = time.mktime(time_tuple)
print(utc_now)  # 1709990265.0
