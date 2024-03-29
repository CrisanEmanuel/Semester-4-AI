from sklearn import linear_model
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from sklearn.model_selection import train_test_split
from dataProcessing import processData


def runV3():
    processData("data/v3_world-happiness-report-2017.csv", "data/v3ProcessedData.csv")
    data = pd.read_csv("data/v3ProcessedData.csv")
    # Definirea variabilelor independente și a variabilei dependente
    X = data[['Economy..GDP.per.Capita.', 'Freedom']]
    y = data['Happiness.Score']

    # Split the data into training and testing sets (80% training, 20% testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Antrenarea modelului de regresie liniară
    model = linear_model.LinearRegression()
    model.fit(X_train, y_train)
    # save the model parameters
    w0, w1, w2 = model.intercept_, model.coef_[0], model.coef_[1]
    print('The learnt model: f(x,w) = ', w0, ' + ', w1, ' * x1', ' + ', w2, ' * x2')
    # Facerea predicțiilor
    y_pred = model.predict(X_test)
    # Evaluarea modelului:
    mse = mean_squared_error(y_test, y_pred)  # Mean Squared Error (cu cât mai mic, cu atât mai bine)
    r2 = r2_score(y_test, y_pred)  # R-squared (cu cât mai aproape de 1, cu atât mai bine)
    print("Mean Squared Error:", mse)
    print("R-squared:", r2)
