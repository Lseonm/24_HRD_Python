import numpy as np

list_a = [1,2,3,4,5]
print(type(list_a))
np_array1 = np.array(list_a, dtype=np.float32) # 옵션을 줄 수 있음
print(type(np_array1))

print(list_a)
print(np_array1) # 리스트에 , 가 없이 출력됨

# print(list_a.shape) # 리스트에는 shape이 없음
print(np_array1.shape) # 텐서(,)가 1이고 5개가 있다는 의미 -> Vector
# --> w1*1 + w2*2 + w3*3 + w4*4 + w5*5

print(np_array1.shape, np_array1.ndim, np_array1.dtype, np_array1.itemsize, np_array1.size)