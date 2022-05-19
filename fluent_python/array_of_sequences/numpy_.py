"""if doing advanced numeric processing arrays we should use NumPy libraries
"""
import numpy as np


a = np.arange(12)

print(a)

print(type(a))

print(type(a.shape))

a.shape = 3, 4

print(a)

print(a[2])

print(a[:, 1])

print(a.transpose())
