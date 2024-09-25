import numpy as np

np_value1 = np.array([1,2,3,4,5,6,7,8])

# 4X2 가됨.
np_value2 = np_value1.reshape(4,2) #뒤에 -1을 넣으도 자동으로 바꿔줌.

print(np_value2)
