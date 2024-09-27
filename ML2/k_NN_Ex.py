# 붓꽃 (iris)
from sklearn.datasets import load_iris # iris 데이터 셋을 가져옴

iris = load_iris()
print(iris) # dict 형임

data = iris['data']
target = iris['target']
print()
print(data) # 데이터 = 150개 (row)
print(data.shape)

print()
print(target)
print(target.shape) # size를 사용하면 갯수만 표현됨

print()


# 깔끔하게 정리
import pandas as pd
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
print(iris_df.head()) # 앞에 5개만 보여줌, tail() 뒤에 5개만 보여줌.

print()



# 훈련 데이터, 정답 데이터 비율 나눔
from sklearn.model_selection import train_test_split
(X_train, X_test, y_train, y_test) = train_test_split(data, target, train_size=0.8, test_size=0.2)



# 훈련 시킴
from sklearn.neighbors import KNeighborsClassifier
k = 7

kNN = KNeighborsClassifier(n_neighbors = k)
kNN.fit(X_train, y_train)

y_predict = kNN.predict(X_test)
print(y_predict)
print(y_test)

print()



# 정확도 측정해줌
from sklearn import metrics
scores = metrics.accuracy_score(y_test, y_predict)
print(f"정확도 : {scores}")

print()


# 새로운 데이터(꽃)
new_flower = [[3.0, 4.0, 5.0, 2.0]]
new_flower_predict = kNN.predict(new_flower)
print(new_flower_predict)