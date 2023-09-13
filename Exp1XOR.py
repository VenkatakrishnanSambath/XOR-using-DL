from keras.models import Sequential
from keras.layers import Dense
import numpy as np

inp = np.array([[0,0],[0,1],[1,0],[1,1]])
out = np.array([[0],[1],[1],[0]])

model = Sequential()
model.add(Dense(2,input_dim=2,activation= 'sigmoid'))
model.add(Dense(1,activation='sigmoid'))
model.compile(optimizer='adam',loss='mean_squared_error')
model.fit(inp,out,epochs=5000,verbose=0)

print("Evaluation of the model is: ",model.evaluate(inp,out))
a = int(input("Enter 1st input: "))
b = int(input("Enter 2nd input: "))
prediction = model.predict([[a,b]],batch_size=2)
round_pred = np.round(prediction)
print("The XOR gate output is: ",np.int_(round_pred))