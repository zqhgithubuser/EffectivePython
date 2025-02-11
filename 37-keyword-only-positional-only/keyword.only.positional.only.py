def safe_division(
    numerator,
    denominator,
    /,
    ndigits=10,
    *,
    ignore_overflow=False,
    ignore_zero_division=False,
):
    try:
        fraction = numerator / denominator
        return round(fraction, ndigits)
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


result = safe_division(1.0, 0, ignore_zero_division=True)
print(result)  # inf

result = safe_division(22, 7)
print(result)  # 3.1428571429

result = safe_division(22, 7, 5)
print(result)  # 3.14286

result = safe_division(22, 7, ndigits=2)
print(result)  # 3.14
