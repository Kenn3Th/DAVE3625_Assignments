# Imports
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from sklearn import linear_model

# Helper functions
def convertToDate(dateString_):
    """
    Depends on pandas and datetime as pd and dt respectively.
    dateString_ -> string of date in yyyy-mm-dd format.
    Returns date in ordinal integer format.
    """
    _formattedDate = pd.to_datetime(dateString_)
    return dt.datetime.toordinal(_formattedDate)

def predictionFunction(ordinalDate_, model_):
    """
    Predicts price based on linear regression model.
    ordinalDate_ -> date in the ordinal integer format.
    model_ -> linear regression model based on sklearn.linear_model.LinearRegression()
    """
    return model_.predict([[ordinalDate_]])


# Data
nasData = pd.read_csv("NAS.csv")
nasData = nasData.dropna(axis=0)
nasData.sort_values(by="Date", ascending=True)

# Converting Date to numbers
dates = pd.to_datetime(nasData.Date)
dates = dates.map(dt.datetime.toordinal)
dates = dates.to_frame()

# Adjust prices
adjPrice = nasData["Adj Close"]
print(type(adjPrice))

# Linear model
linRegModell = linear_model.LinearRegression()
linRegModell.fit(dates, adjPrice)

# Plotting
plt.title("Adjusted prices over dates")
plt.xlabel("Dates")
plt.ylabel("Prices")
plt.scatter(dates, adjPrice, color="green")
plt.plot(dates, linRegModell.predict(dates), color="red")
plt.show()

# Prediction based on model.
dateIp_:str = ""
while():
    dateIp_ = input("Enter date on the form 'yyyy-mm-dd' -> ")
    if(dateIp_ == "q" or dateIp_ == "quit"):
        break
    predictedPrice = predictionFunction(convertToDate(dateIp_), linRegModell)
    print(f"Predicted price: {predictedPrice}")
