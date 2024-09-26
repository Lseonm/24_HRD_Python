from sklearn import linear_model
import matplotlib.pyplot as plt

X = [174, 152, 138, 128, 186]
y = [71, 55, 46, 38, 88]

plt.scatter(X,y, color='red')
# plt.show()

# 객체 생성
regression = linear_model.LinearRegression() # 생성자 호출 (클래스 생성)

# Tensor 가 2인 형태로 바꿔 줘야 함. (Tensor = 2, ndim = 2)
X = [[174], [152], [138], [128], [186]]
y = [71, 55, 46, 38, 88] # 테스트 데이터는 그대로 둬도됨

regression.fit(X, y) # fit : 맞추다

print(f"기울기 : {regression.coef_}") # 기울기 구하기

print(f"바이어스 : {regression.intercept_}")

y_hat = regression.predict(X) # y 예측하기

print(y_hat)


my_weight = regression.predict([[177]])
print(f"my weight : {my_weight}") # 키를 통한 몸무게 예측

plt.plot(X,y_hat, color='blue', linewidth=4)
plt.show()





