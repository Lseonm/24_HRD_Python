import keras
import tensorflow as tf

X = tf.constant([[0,0], [0,1], [1,0], [1,1]])
y = tf.constant([0,1,1,0])

model = keras.models.Sequntial(name= "XOR")
input = keras.Input(shape=(2,)) # 입력 (shape을 꼭 (2,)로 해줘야 함)

model.add(input)

layer1 = keras.layers.Dense(units=4, activation='sigmoid', name="Layer1")
model.add(layer1)

layer2 = keras.layers.Dense(units=2, activation='sigmoid', name ="Layer2")

output = keras.layers.Dense(units=1, activation='sigmoid', name="OUTPUT") # units = 1인게 중요함
# name = "OUTPUT" 으로 해주는게 좋음

model.add(output)
print(model.summary())


model.compile(loss='mse', optimizer="adam")
model.fit(X,y, epochs=2000, verbose=2)
print(model.predict(X))
model.save("XORGATE.keras")