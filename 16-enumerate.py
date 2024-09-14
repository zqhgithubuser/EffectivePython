flavor_list = ["vanilla", "chocolate", "pecan", "strawberry"]

print("----- range -----")
for i in range(len(flavor_list)):
  flavor = flavor_list[i]
  print(f"{i + 1}: {flavor}")

# it = enumerate(flavor_list)
# print(next(it))
# print(next(it))

print("----- enumerate -----")
for i, flavor in enumerate(flavor_list, 1):
  print(f"{i}: {flavor}")
