# 索引
snacks = [("bacon", 350), ("donut", 240), ("muffin", 190)]

for i in range(len(snacks)):
  item = snacks[i]
  name = item[0]
  calories = item[1]
  print(f"#{i + 1}: {name} has {calories} calories")

# 解包
for rank, (name, calories) in enumerate(snacks, 1):
  print(f"#{rank}: {name} has {calories} calories")
