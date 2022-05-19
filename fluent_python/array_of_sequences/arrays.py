"""a python array is as lean as a C array
"""

from array import array
from random import random


floats = array("d", (random() for i in range(10**7)))

print(floats[-1])

fp = open("floats.bin", "wb")

# saving is 7 times faster than writing one float per line in a text file
floats.tofile(fp)

fp.close()

floats2 = array("d")

fp = open("floats.bin", "rb")

# 60 times faster than reading the numbers from a text file
floats2.fromfile(fp, 10**7)

fp.close()

print(floats2[-1])

print(floats2 == floats)
