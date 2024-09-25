import numpy as np

b = np.array([[1,1], [2,2], [3,3]], dtype=np.int32)
print(b)


print(np.insert(b, 1, 4, axis=0))

print(np.insert(b, 1, 4, axis=1))


# 행렬 내의 값 가져오기
np_value = np.array([[1,2,3], [4,5,6], [7,8,9], [0,1,2]])
print(np_value)

print(np_value[0][0])
print(np_value[3,0])

print(np_value.flatten())