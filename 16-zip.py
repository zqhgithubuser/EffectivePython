names = ["Cecilia", "Lise", "Marie"]
counts = [len(n) for n in names]

longest_name = None
max_count = 0

print("----- range -----")
for i in range(len(names)):
  count = counts[i]
  if count > max_count:
    max_count = count
    longest_name = names[i]
print(longest_name)
print(max_count)

print("----- zip -----")
for name, count in zip(names, counts):
  if count > max_count:
    max_count = count
    longest_name = name

print(longest_name)
print(max_count)
