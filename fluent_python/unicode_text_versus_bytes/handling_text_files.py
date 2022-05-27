"""
The unicode sandwich good practice for text processing

read -> bytes to str -> decode bytes on input

100% str -> process text only

write -> str to bytes -> encode text on output

python 3 as utf_8 as default
"""

# code that has to run on multiple machines or non multiple occasions should never
# depend on encoding defaults. Always pass an explicit encoding = argument when
# opening text files, because the default may change from one machine to the next,
# or from one day to the next
print(open("cafe.txt", "w", encoding="cp1252").write("café"))

try:
    print(open("cafe.txt").read())

except UnicodeDecodeError as error:
    print(error)
