fruits = ["grape", "raspberry", "apple", "banana"]

# creates a new object
print(sorted(fruits))

print(sorted(fruits, reverse=True))

print(sorted(fruits, key=len))

print(sorted(fruits, key=len, reverse=True))

# doens't creates a new object and as convention returns None
print(fruits.sort())
