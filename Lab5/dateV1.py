import numpy as np
from sklearn import linear_model
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from dataProcessing import processData, loadData
from myRegression import *


def runV1CuTool():
    processData("data/v1_world-happiness-report-2017.csv", "data/v1ProcessedData.csv")
    data = pd.read_csv("data/v1ProcessedData.csv")
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
    # Evaluarea modelului
    mse = mean_squared_error(y_test, y_pred)  # Mean Squared Error (cu cât mai mic, cu atât mai bine)
    r2 = r2_score(y_test, y_pred)  # R-squared (cu cât mai aproape de 1, cu atât mai bine)
    print("Mean Squared Error:", mse)
    print("R-squared:", r2)


def runV1FaraTool():
    processData("data/v1_world-happiness-report-2017.csv", "data/v1ProcessedData.csv")
    input1, input2, output = loadData("data/v1ProcessedData.csv", "Economy..GDP.per.Capita.", "Freedom",
                                      "Happiness.Score")

    # Combine input1 and input2 into a single list of feature vectors
    features = list(zip(input1, input2))
    # Combine features and outputs into a list of tuples (feature_vector, output)
    data = list(zip(features, output))

    # Split the Data Into Training and Test Subsets
    # In this step we will split our dataset into training and testing subsets (in proportion 80/20%).
    np.random.seed(5)
    indexes = [i for i in range(len(data))]
    trainSample = np.random.choice(indexes, int(0.8 * len(data)), replace=False)
    validationSample = [i for i in indexes if not i in trainSample]
    trainData = [data[i] for i in trainSample]
    validationData = [data[i] for i in validationSample]

    # Separate training inputs, outputs and validation inputs, outputs
    trainInputs = [x[0] for x in trainData]
    trainOutputs = [x[1] for x in trainData]
    validationInputs = [x[0] for x in validationData]
    validationOutputs = [x[1] for x in validationData]

    # Calculate the model parameters
    model = MyLinearMultivariateRegression()
    model.fit(trainInputs, trainOutputs)
    w0, w1, w2 = model.intercept_, model.coef_[0], model.coef_[1]
    print('The learnt model: f(x,w) = ', w0, ' + ', w1, ' * x1', ' + ', w2, ' * x2')

    # Make predictions
    computedValidationOutputs = model.predict(validationInputs)

    # Evaluarea modelului
    mae = mean_absolute_error(computedValidationOutputs, validationOutputs)
    print("Mean Squared Error:", mae)


def runV1():
    runV1CuTool()
    print()
    runV1FaraTool()


# X este matricea de variabile independente, iar y este vectorul de valori reale ale variabilei dependente
# (OLS - Ordinary Least Squares).
# def calculare_coeficienti1(X, y):
#     # Adăugați o coloană de 1-uri la matricea X pentru termenul de interceptare
#     X_with_intercept = np.column_stack((np.ones(len(X)), X))
#
#     # Calculați coeficienții folosind formula OLS
#     coefficients = np.linalg.inv(X_with_intercept.T @ X_with_intercept) @ X_with_intercept.T @ y
#
#     return coefficients[0], coefficients[1], coefficients[2]
