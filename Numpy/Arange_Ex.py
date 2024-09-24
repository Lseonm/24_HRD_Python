import numpy as np

# 0부터 10까지 배열 생성 (1차원)
np_arr = np.arange(0, 10)
print(np_arr)
np_arr1 = np_arr.reshape(5,2)

print(np_arr1)

# 0~10.까지 수를 1000개로 뽑아옴
np_arr2 = np.linspace(0, 10, 1000)
print(np_arr2)
