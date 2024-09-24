import numpy as np

np_array = np.array([[1,2,3], [4,5,6]])
print(np_array.shape)
print(np_array)
# [[1 2 3]
#  [4 5 6]]

print()

print(np_array.shape, np_array.ndim, np_array.itemsize, np_array.size)

print()

np_array2 = np.array([10,20,30])
result = np_array2 * 3
print(result)

result2 = np_array2 + 10
print(result2)