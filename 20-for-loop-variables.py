categories = ["Hydrogen", "Uranium", "Iron", "Other"]
for i, name in enumerate(categories):
    if name == "Iron":
        break
print(i)

for i, name in enumerate(categories):
    if name == "Lithium":
        break
print(i)

# NameError: name 'i' is not defined. Did you mean: 'id'?
# categories = []
# for i, name in enumerate(categories):
#     if name == "Lithium":
#         break
# print(i)
