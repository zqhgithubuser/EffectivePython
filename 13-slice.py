a = ["a", "b", "c", "d", "e", "f", "g", "h"]

print(a[:])      # ["a", "b", "c", "d", "e", "f", "g", "h"]
print(a[:5])     # ["a", "b", "c", "d", "e"]
print(a[:-1])    # ["a", "b", "c", "d", "e", "f", "g"]
print(a[4:])     #                     ["e", "f", "g", "h"]
print(a[-3:])    #                          ["f", "g", "h"]
print(a[2:5])    #           ["c", "d", "e"]
print(a[2:-1])   #           ["c", "d", "e", "f", "g"]
print(a[-3:-1])  #                          ["f", "g"]

b = a[3:]
print("Before:   ", b)
b[1] = 99
print("After:    ", b)
print("No change:", a)