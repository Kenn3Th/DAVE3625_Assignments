# Imports
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from sklearn import linear_model
from random import randint

sizeOfData = 20
x_array = [n for n in range(sizeOfData)]
y_array = [randint(1, 20) for n in range(sizeOfData)]

print("X")
print(x_array)
print("Y")
print(y_array)

newArray = [randint(1, 20) for n in range(sizeOfData)]
print("New array")
print(newArray)

model = linear_model.LinearRegression()
model.fit([ x_array ], [ y_array ])
print("Predict:")
print(model.predict([x_array]))

plt.scatter(x_array, [y_array])
plt.plot([ x_array], model.predict([ x_array ]))
plt.show()