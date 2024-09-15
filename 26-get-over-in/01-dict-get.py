votes = {
    "baguette": ["Bob", "Alice"],
    "ciabatta": ["Coco", "Deb"],
}

key = "brioche"
who = "Elmer"

# in
# if key in votes:
#     name = votes[key]
# else:
#     votes[key] = name = []

# name.append(who)

# get
if (names := votes.get(key)) is None:
    votes[key] = names = []
    
names.append(who)

print(votes)