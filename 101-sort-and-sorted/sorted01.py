original = ["Swallowtail", "Monarch", "Red Admiral"]
alphabetical = sorted(original)
print(f"Original {original}")  # ['Swallowtail', 'Monarch', 'Red Admiral']
print(f"Sorted   {alphabetical}")


legs = {"insects": 6, "spiders": 8, "lizards": 4}
sorted_legs = sorted(legs, key=lambda x: legs[x], reverse=True)
print(sorted_legs)  # ['spiders', 'insects', 'lizards']
