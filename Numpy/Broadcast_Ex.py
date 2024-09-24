import numpy as np

a = np.array([[10,20,30],
             [40,50,60]])

b = np.array([2,3,4])

print(a+b)
print(a*b)

print()

c = np.full((2,3), 100)
print(c)

ex = 10 * np.eye(4)
print(ex)