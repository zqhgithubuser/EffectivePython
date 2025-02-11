import time

now = 1710047865.0
local_tuple = time.localtime(now)
time_format = "%Y-%m-%d %H:%M:%S"
time_str = time.strftime(time_format, local_tuple)
print(time_str)  # 2024-03-10 13:17:45

time_tuple = time.strptime(time_str, time_format)
utc_now = time.mktime(time_tuple)
print(utc_now)  # 1710047865.0

parse_format = "%Y-%m-%d %H:%M:%S %Z"
depart_sfo = "2024-03-09 21:17:45 PST"
# time_tuple = time.strptime(depart_sfo, parse_format)
# time_str = time.strftime(time_format, time_tuple)
# print(time_str)
# ValueError: time data '2024-03-09 21:17:45 PST' does not match format '%Y-%m-%d %H:%M:%S %Z'

# arrival_nyc = "2024-03-10 03:31:18 EDT"
# time_tuple = time.strptime(arrival_nyc, parse_format)
# ValueError: time data '2024-03-10 03:31:18 EDT' does not match format '%Y-%m-%d %H:%M:%S %Z'
