import array

cafe = bytes("café", encoding="utf-8")

print(cafe)

print(cafe[0])

print(cafe[:1])

cafe_arr = bytearray(cafe)

print(cafe_arr)

print(cafe_arr[-1:])


# initializing bytes from the raw data of an array
numbers = array.array("h", [-2, -1, 0, 1, 2])

octets = bytes(numbers)

print(octets)
