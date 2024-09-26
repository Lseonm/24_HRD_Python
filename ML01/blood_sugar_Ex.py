import numpy as np
from sklearn import datasets # 라이브러리에서 제공하는 공공 데이터

(diabetes_X, diabetes_y) = datasets.load_diabetes(return_X_y=True) # X : 훈련 데이터, y : 정답
print(diabetes_X)
print()
print(diabetes_X.shape)
print()
print(diabetes_y)
print()
print(diabetes_y.shape)

print()
# bmi 의 모든 데이터 가져옴
bmi = diabetes_X[:, 2] # 2번째 인덱스의 모든 데이터
print(bmi)
print(bmi.shape)

print()
diabetes_X_new = diabetes_X[:,np.newaxis, 2] # 축을 지정해서 축 형태로 모든 데이터를 가져옴
print(diabetes_X_new)
print(diabetes_X_new.shape)

from sklearn.model_selection import train_test_split # 분류 시켜주는 툴
(X_train, X_test, y_train, y_test) = train_test_split(diabetes_X_new, diabetes_y,
                                                      train_size=0.8, test_size=0.2, random_state=0) # 8:2, 7:3 비율, random_state는 시드

print()
# print(X_train[10])

from sklearn import linear_model

regression = linear_model.LinearRegression()
regression.fit(X_train, y_train)

y_predict = regression.predict(X_test)
print(y_predict)
print(y_test)

import matplotlib.pyplot as plt
plt.scatter(y_test, y_predict)
plt.show()