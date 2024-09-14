int_value = 5
str_value = '5'

print(int_value)
print(str_value)

print(repr(int_value))
print(repr(str_value))

print("%r, %r" % (int_value, str_value))

print(f'{int_value!r}, {str_value!r}')