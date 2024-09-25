import numpy as np
import matplotlib.pyplot as plt

(Fig, Ax) = plt.subplots(nrows=2, ncols=2)

x = np.random.randn(100)
y = np.random.randn(100)

Ax[0, 0].scatter(x,y) # 첫 번째 그래프에 그리기 (안쓰면 맨 뒤에 그려짐)


x = np.arange(10) # x축을 0 ~ 9
y = np.random.uniform(0, 10, 10)
Ax[0,1].bar(x, y) # 막대 그래프

y = np.eye(100)
Ax[1,1].imshow(y)

plt.show()