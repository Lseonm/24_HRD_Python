import numpy as np

np_value1 = np.random.randn(10) *10 +175
print(np_value1)

print(np_value1.round(2))
print(np_value1.astype(int))

print()

np.random.seed(2024)
np_value2 = np.random.normal(165, 10, (10,10))
print(np_value2)

print()

a = np.array([[1,2], [1, -3]])
b = np.array([6, 1])

s = np.linalg.solve(a,b)
print(s)
print(np.linalg.inv(a))