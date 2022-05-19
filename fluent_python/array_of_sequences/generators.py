import array

symbols = "£$@^%"

tuple = (ord(symbol) for symbol in symbols)

print(tuple)


print(array.array("I", (ord(symbol) for symbol in symbols)))
