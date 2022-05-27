from string import octdigits


octets = b"Montr\xe9al"

print(octets.decode("cp1252"))

print(octets.decode("iso8859_7"))

print(octets.decode("koi8_r"))

try:
    print(octets.decode("utf_8"))

except UnicodeDecodeError as error:
    print(error)

print(octets.decode("utf_8", errors="replace"))
