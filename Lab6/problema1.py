from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from myBGDRegressor import *
from dataProcessing import *

def problema1TOOLProdusIntern():
    # processData(fileName, "world-happiness-processed.csv")
    inputs, outputs = loadDataOneFeature("world-happiness-processed.csv", "Economy..GDP.per.Capita.", "Happiness.Score")

    # Split the Data Into Training and Test Subsets
    np.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    testSample = [i for i in indexes if not i in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]

    testInputs = [inputs[i] for i in testSample]
    testOutputs = [outputs[i] for i in testSample]

    # model initialisation
    regressor = linear_model.SGDRegressor(alpha=0.01, max_iter=100, shuffle=False)
    # training the model by using the training inputs and known training outputs
    regressor.fit(np.array(trainInputs).reshape(-1, 1), trainOutputs)
    # save the model parameters
    w0, w1 = regressor.intercept_[0], regressor.coef_[0]
    print('the learnt model: f(x) = ', w0, ' + ', w1, ' * x')

    # use the trained model to predict new inputs
    computedTestOutputs = regressor.predict(np.array(testInputs).reshape(-1, 1))
    error = mean_squared_error(testOutputs, computedTestOutputs)
    print('prediction error (tool):  ', error)


def problema1TOOLProdusInternFreedom():
    # processData("world-happiness-report-2017.csv", "world-happiness-processed.csv")
    data = pd.read_csv("world-happiness-processed.csv")
    # Definirea variabilelor independente și a variabilei dependente
    X = data[['Economy..GDP.per.Capita.', 'Freedom']]
    y = data['Happiness.Score']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Add a column of ones for the intercept term
    X_train = np.c_[np.ones(X_train.shape[0]), X_train]
    X_test = np.c_[np.ones(X_test.shape[0]), X_test]

    # Initialize weights with random values
    np.random.seed(42)
    weights = np.random.rand(X_train.shape[1])

    # Perform batch gradient descent
    for _ in range(100):
        # Compute predictions
        predictions = np.dot(X_train, weights)
        # Compute errors
        errors = predictions - y_train
        # Compute gradients
        gradients = np.dot(X_train.T, errors) / X_train.shape[0]
        # Update weights
        weights -= 0.01 * gradients

    # Make predictions
    y_pred = np.dot(X_test, weights)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    # Print model parameters
    intercept, *coefficients = weights
    print('The learnt model: f(x,w) = ', intercept, ' + ', coefficients[0], ' * x1', ' + ', coefficients[1], ' * x2')
    # Print evaluation metrics
    print("Mean Squared Error:", mse)


def problema1FARATOOLProdusIntern():
    inputs, outputs = loadDataOneFeature("world-happiness-processed.csv", "Economy..GDP.per.Capita.", "Happiness.Score")

    # Split the Data Into Training and Test Subsets
    np.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    testSample = [i for i in indexes if not i in trainSample]

    trainInputs = [[inputs[i]] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]

    testInputs = [[inputs[i]] for i in testSample]
    testOutputs = [outputs[i] for i in testSample]

    # Train the model
    weights = train_linear_regression(trainInputs, trainOutputs, 0.01, 100)

    # Perform predictions
    predictions = predict(testInputs, weights)
    print("The learnt model: f(x) = ", weights[0], " + ", weights[1], " * x")
    error = 0.0
    for t1, t2 in zip(testOutputs, predictions):
        error += (t1 - t2) ** 2
    error = error / len(predictions)
    print('prediction error (manual): ', error)


def problema1FARATOOLProdusInternFreedom():
    # processData(fileName, "world-happiness-processed.csv")
    input1, input2, output = loadDataTwoFeatures("world-happiness-processed.csv", "Economy..GDP.per.Capita.", "Freedom", "Happiness.Score")

    # Combine input1 and input2 into a single list of feature vectors
    features = list(zip(input1, input2))
    # Convert list of tuples into list of lists
    features = [list(feature) for feature in features]
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

    # Train the model
    weights = train_linear_regression(trainInputs, trainOutputs, 0.01, 100)

    # Perform predictions
    predictions = predict(validationInputs, weights)
    print("The learnt model: f(x) = ", weights[0], " + ", weights[1], " * x", " + ", weights[2], " * x^2")
    error = 0.0
    for t1, t2 in zip(validationOutputs, predictions):
        error += (t1 - t2) ** 2
    error = error / len(predictions)
    print('prediction error (manual): ', error)


def problema1():
    problema1TOOLProdusIntern()
    print()
    problema1TOOLProdusInternFreedom()
    print()
    problema1FARATOOLProdusIntern()
    print()
    problema1FARATOOLProdusInternFreedom()
