global_scope = {"my_condition": False}
local_scope = {}

exec(
    """
if my_condition:
    x = 'yes'
else:
    x = 'no'
""",
    global_scope,
    local_scope,
)

print(local_scope)  # {'x': 'no'}
