import numpy as np
import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [1,2,3,4,5]
# plt.xlabel('X축')
# plt.ylabel('Y축')
# plt.plot(x,y)
# plt.show()

# x = [-5, -4, -3, -2, -1 , 0, 1,2,3,4,5]
# y = [i**2 for i in x]

# x = np.array(x)
# y = x **2 # 브로드캐스팅
#
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.axis([0,10, 0,30]) # x = 0~10, y=0~30 까지 보여줌
# plt.plot(x,y)
# plt.show()

# X = np.arange(-20,20)
# y1 = 2 * X
# y2 = (1/3) * (X ** 2) + 5
# y3 = -(X**2) - 5
#
# # plt.plot(X,y1,X,y2,X,y3)
# plt.plot(X,y1, 'g--')
# plt.plot(X,y2, 'b^')
# plt.plot(X,y3, 'r*')
# plt.axis([-30,30,-30,30])
# plt.show()

X = np.linspace(0, 2*np.pi, 1_000)
y1 = np.sin(X)
y2 = np.cos(X)
y3 = np.tan(X)

plt.title('Sin-Cos-Tan')
plt.plot(X,y1,'b',label = 'Sin')
plt.plot(X,y2,'r',label = 'Cos')
plt.plot(X,y3,'c',label = 'Tan')
plt.legend()
plt.axis([0,2*np.pi, -2, 2])
# plt.savefig("Sin-Cos-Tan.png")
plt.show()