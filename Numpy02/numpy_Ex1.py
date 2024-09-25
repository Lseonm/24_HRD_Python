import numpy as np

np_value1 = np.array([5,3,2,0,1,9])
np_value1.sort()
print(np_value1)
print(np_value1[::-1])

print()

a = np.array([1,2,3])
b = np.array([[4,5,6],[7,8,9]])

print(np.append(a,b))

print(np.append([a],b, axis=0))