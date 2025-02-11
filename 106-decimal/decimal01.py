from decimal import Decimal, ROUND_UP

rate = Decimal("1.45")
seconds = Decimal(3 * 60 + 42)
cost = rate * seconds / Decimal(60)
print(cost)  # 5.365


rate = Decimal("0.05")
seconds = Decimal("5")
small_cost = rate * seconds / Decimal(60)
print(small_cost)  # 0.004166666666666666666666666667

rounded = small_cost.quantize(Decimal("0.01"), rounding=ROUND_UP)
print(f"Rounded {small_cost} to {rounded}")  # 0.01
