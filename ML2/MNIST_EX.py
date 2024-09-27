import matplotlib.pyplot as plt
from sklearn import datasets

digits = datasets.load_digits()
# print(digits)
# print()
#
# print(digits['data'])
# print(digits['target'])
# print(digits['feature_names'])
#
# digit = digits['data']
# label = digits['target']
# plt.imshow(digit)
# print(digits.images[0])
# print(label[0])
#
# # plt.imshow(digits.images[0], cmap=plt.cm.gray_r, interpolation='nearest')
# # plt.show()
#
# n_images = len(digits.images)
# print(n_images)
# print(digits.images.shape)
# # data = digits.images.flatten()
# # print(data)
# # data = digits.images.reshape(1797, 8 * 8)
# data = digits.images.reshape(1797, -1) # 둘 중에 하나 사용 (-1 쓰면 자동으로 맞춰줌)
# print(data)
# print(data.shape)
# print(digits.data)

from sklearn.model_selection import train_test_split

(X_train, X_test, y_train, y_test) = train_test_split(digits.data, digits.target, test_size=0.3, random_state=42)
print(X_train)
print(X_train.shape)

from sklearn.neighbors import KNeighborsClassifier
k = 5
kNN = KNeighborsClassifier(n_neighbors=k)
kNN.fit(X_train, y_train)
prediction = kNN.predict(X_test)
print(prediction)
print(y_test)


# 정확도 확인 방법 (accuacy가 정확도)
from sklearn.metrics import classification_report
print("EVALUATION ON TESTING DATA")
print(classification_report(y_test, prediction))

y_predict = kNN.predict([X_test[10]])
plt.imshow(X_test[10].reshape(8,8), cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
print(y_predict)
print(y_test[10])

# from sklearn import metrics
# scores = metrics.accuracy_score(y_test, prediction)
# print(f"정확도 : {scores}")