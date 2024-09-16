def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period


weight_a = 2.5
weight_b = 3
time_a = 1
time_b = 4
weight_diff = weight_b - weight_a
time_diff = time_b - time_a
flow_per_second = flow_rate(weight_diff, time_diff)
print(f"{flow_per_second:.3} kg per second")

flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)
print(f"{flow_per_hour:.3} kg per hour")
