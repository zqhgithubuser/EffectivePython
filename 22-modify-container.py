my_dict = {"red": 1, "blue": 2, "green": 3}

# 副本
keys_copy = list(my_dict.keys())
for key in keys_copy:
    if key == "blue":
        my_dict["green"] = 4

print(my_dict)

my_list = [1, 2, 3]
list_copy = list(my_list)
for number in list_copy:
    if number == 2:
        my_list.insert(0, 4)

print(my_list)

# 性能优化
my_dict = {"red": 1, "blue": 2, "green": 3}
modifications = {}

for key in my_dict:
    if key == "blue":
        modifications["green"] = 4

my_dict.update(modifications)
print(my_dict)