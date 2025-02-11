def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    raise RuntimeError("Not reachable")


if __name__ == "__main__":
    result = gcd(
        (
            10,
            15,
        )
    )
    print(result)
