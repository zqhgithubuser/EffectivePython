# def careful_divide(a, b):
#     try:
#         return True, a / b
#     except ZeroDivisionError:
#         return False, None

# x, y = 0, 5
# success, result = careful_divide(x, y)
# if not success:
#     print("Invalid inputs")
# else:
#      print(f"Result is {result:.1f}")

#######################################################

def careful_divide(a: float, b: float) -> float:
    """Divides a by b.

    Raises:
        ValueError: When the inputs cannot be divided.
    """
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Invalid inputs")

x, y = 0, 5
try:
    result = careful_divide(x, y)
except ValueError:
    print("Invalid inputs")
else:
    print(f"Result is {result:.1f}")
