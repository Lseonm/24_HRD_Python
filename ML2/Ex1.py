import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler # 최댓값과 최솟값 사이에서 비율 형태로 나눠서 값 존재


# 값이 큼 => MinMaxScalar 사용 -> tensor가 2여야 함.
X = [174, 152, 138, 128, 186]
y = [71, 55, 46, 38, 88]

# X_new = X[:, np.newaxis] # -> 차원을 늘림 -> Numpy 형태로 변환해야함

# Numpy 형태로 변환해야 함
X = np.array(X)
y = np.array(y)

X_new = X[:, np.newaxis] # -> 차원을 늘림 (tensor 2)
y_new = y[:, np.newaxis] # -> 차원을 늘림 (tensor 2)

print(X_new)
print(y_new)


scaler = MinMaxScaler() # MinMaxScaler 클래스 객체 생성
X = scaler.fit_transform(X_new)
y = scaler.fit_transform(y_new)

print(X)
print(y)

# 다시 차원을 내림
X = X.flatten()
y = y.flatten()

print(X)
print(y)

# 초기화 0.0, 1.0
W = 1.0 # 기울기
b = 0.8 # 절편

lr = 0.01 # 학습률

epochs = 1000 # 반복 수
n = len(X) # 입력 데이터 개수

for _ in range(epochs):
    y_hat = W * X + b # 예측값
    error = y_hat - y # 오류 찾기 (y는 정답)

    dW = (2/n) * sum(X * error)
    db = (2/n) * sum(error)
    W = W - lr * dW # 기울기 수정
    b = b - lr *db # 절편 수정

    print(f"W : {W}, b : {b}")

    from sklearn.linear_model import LinearRegression

    regression = LinearRegression()
    regression.fit(X_new,y)
    print(f"W : {regression.coef_}, b : {regression.intercept_}")