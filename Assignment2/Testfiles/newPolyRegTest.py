# Imports
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

# Helper functions


def convertToDate(dateString_):
    """
    Depends on pandas and datetime as pd and dt respectively.
    dateString_ -> string of date in yyyy-mm-dd format.
    Returns date in ordinal integer format.
    """
    _formattedDate = pd.to_datetime(dateString_)
    return dt.datetime.toordinal(_formattedDate)


def predictLinearModel(ordinalDate_, model_):
    """
    Predicts price based on linear regression model.
    ordinalDate_ -> date in the ordinal integer format.
    model_ -> linear regression model based on sklearn.linear_model.LinearRegression()
    """
    return model_.predict([[ordinalDate_]])

def predictPolModel(ordinalDate_, model_):
    """
    Predicts price based on linear regression model.
    ordinalDate_ -> date in the ordinal integer format.
    model_ -> linear regression model based on sklearn.linear_model.LinearRegression()
    """
    return model_.predict(polyRegModel.fit_transform([[ordinalDate_]]))

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
# print(f"adjPrice type: { type(adjPrice) }")

# Modelling.
# ----- LINEAR -------
linRegModell = linear_model.LinearRegression()
linRegModell.fit(dates, adjPrice)

# ----- POLY -------
polyRegModel = PolynomialFeatures(degree=9)
datesPoly = polyRegModel.fit_transform(dates)
polyRegModel.fit(datesPoly, adjPrice)
linRegModell2 = linear_model.LinearRegression()
linRegModell2.fit(datesPoly, adjPrice)

# # Debugging
# # ----- Printing prediction ----------
# dateIp = convertToDate("2021-01-01")
# print(linRegModell.predict([[dateIp]]))
# print(polyRegModel.fit_transform([[dateIp]]))
# print(linRegModell2.predict(polyRegModel.fit_transform([[dateIp]])))

# Plotting linear regression.
plt.title("Adjusted prices over dates - Linear")
plt.xlabel("Dates")
plt.ylabel("Prices")
plt.scatter(dates, adjPrice, color="green")
plt.plot(dates, linRegModell.predict(dates), color="red")
plt.show()

# Plotting polynomial regression.
plt.title("Adjusted prices over dates - Polynomial")
plt.xlabel("Dates")
plt.ylabel("Prices")
plt.scatter(dates, adjPrice, color="green")
plt.plot(dates, linRegModell2.predict(polyRegModel.fit_transform(dates)), color="red")
plt.show()

# Prediction based on model.
dateIp_ = ""
while(True):
    dateIp_ = input("Enter date on the form 'yyyy-mm-dd' -> ")
    if(dateIp_ == "q" or dateIp_ == "quit"):
        print("Terminating...")
        break
    linPredPrice = predictLinearModel(convertToDate(dateIp_), linRegModell)
    polPredPrice = predictPolModel(convertToDate(dateIp_), linRegModell2)
    print(f"Predicted price (Linear regression): {linPredPrice}")
    print(f"Predicted price (Polynomial regression): {polPredPrice}")
