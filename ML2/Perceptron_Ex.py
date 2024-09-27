from sklearn.linear_model import Perceptron

# AND GATE
X = [[0, 0],
     [0, 1],
     [1, 0],
     [1, 1]]

y = [0, 1, 1, 0]

percept = Perceptron(tol=0.0001)
percept.fit(X,y)

y_predict = percept.predict(X)
print(y_predict)

y_prediction = percept.predict([[1,0]])
print(f"결과값 : {y_prediction}")