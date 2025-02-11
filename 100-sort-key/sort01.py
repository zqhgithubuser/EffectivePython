class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"Tool({self.name!r}, {self.weight})"


tools = [
    Tool("level", 3.5),
    Tool("hammer", 1.25),
    Tool("screwdriver", 0.5),
    Tool("chisel", 0.25),
]

# tools.sort()

print("Unsorted:", repr(tools))
tools.sort(key=lambda x: x.name)
print("\nSorted:  ", tools)

tools.sort(key=lambda x: x.weight)
print("By weight:", tools)


power_tools = [
    Tool("drill", 4),
    Tool("circular saw", 5),
    Tool("jackhammer", 40),
    Tool("sander", 4),
]

power_tools.sort(key=lambda x: (x.weight, x.name))
print(power_tools)

power_tools.sort(
    key=lambda x: (x.weight, x.name),
    reverse=True,  # Makes all criteria descending
)
print(power_tools)

# 按 name 升序，按 weight 降序
power_tools.sort(
    key=lambda x: x.name,
)
power_tools.sort(key=lambda x: x.weight, reverse=True)
print(power_tools)
