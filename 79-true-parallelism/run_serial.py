import time

import my_module

NUMBERS = [
    (19633090, 22659730),
    (20306770, 38141720),
    (15516450, 22296200),
    (20390450, 20208020),
    (18237120, 19249280),
    (22931290, 10204910),
    (12812380, 22737820),
    (38238120, 42372810),
    (38127410, 47291390),
    (12923910, 21238110),
]


def main():
    start = time.perf_counter()
    results = list(map(my_module.gcd, NUMBERS))
    end = time.perf_counter()
    delta = end - start
    print(f"Took {delta: .3f} seconds")


if __name__ == "__main__":
    main()  # Took  17.907 seconds
