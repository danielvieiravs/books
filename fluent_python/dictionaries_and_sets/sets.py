"""a set is a collection of unique objects
"""
from unicodedata import name

food = ["spam", "spam", "eggs", "spam", "bacon", "eggs"]

print(set(food))

print(list(set(food)))

# set literals

# more faster and readable than calling the constructor because to evaluate it,
# Python has to look up the set name to fetch the constructor, then build a list,
# and finally pass it to the constructor
set_init_faster = {1, 2, 3}

set_int_slower = set([1, 2, 3])


# set comprehensions
print({chr(i) for i in range(32, 256) if "SIGN" in name(chr(i), " ")})


# set operations on dict views
d1 = dict(a=1, b=2, c=3, d=4)
d2 = dict(b=20, d=40, e=50)

print(d1.keys() & d2.keys())

s = {"a", "e", "i"}

print(d1.keys() & s)

print(d1.keys() | s)
