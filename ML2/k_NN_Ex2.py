
dachs_length = [77, 78, 85, 83, 73, 77, 73, 80]
dachs_height = [25, 28, 29, 30, 21, 22, 17, 35]

samoyed_length = [75, 77, 86, 86, 79, 83, 83, 88]
samoyed_heigth = [56, 57, 50, 53, 60, 53, 49, 61]


# 그래프 그리기
import matplotlib.pyplot as plt
plt.scatter(dachs_length, dachs_height, c='r', marker='.')
plt.scatter(samoyed_length, samoyed_heigth, c='b', marker='*')
# plt.show()


import numpy as np
# 닥스훈트
d_data = np.column_stack((dachs_length, dachs_height)) # 두 변수를 가로로 합쳐서 세로로 늘림.
print(d_data)
d_label = np.zeros(len(d_data)) # 정답 (닥스훈트는 0 으로 표시)
print(d_label)

print()

# 사모예드
s_data = np.column_stack((samoyed_length, samoyed_heigth))
print(s_data)
s_label = np.ones(len(s_data)) # 정답 (사모예드는 1 로 표시)
print(s_label)


# 두 데이터 합치기
dogs = np.concatenate((d_data, s_data)) # 개 데이터
labels = np.concatenate((d_label, s_label)) # 정답

print()

print(f"개 : {dogs}")
print(f"정답 : {labels}")

# 훈련 시키기
from sklearn.neighbors import KNeighborsClassifier
k = 3

kNN = KNeighborsClassifier(n_neighbors=k)
kNN.fit(dogs, labels)


print()

# 새로운 개 (데이터) 발견
new_dog = [[78, 35]]

new_dog_predict = kNN.predict(new_dog)
print(f" 예측 : {new_dog_predict}") # --> 0 (닥스훈트)로 예상


# 400 마리의 품종을 2일 내에 적용하는 방법