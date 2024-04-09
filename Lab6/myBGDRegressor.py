import numpy as np


def train_linear_regression(inputs, outputs, learning_rate, num_iterations):
    num_samples = len(inputs)
    num_features = len(inputs[0])

    # Convert inputs and outputs to NumPy arrays
    inputs = np.array(inputs)
    outputs = np.array(outputs)

    # Initialize weights with random values
    weights = np.random.rand(num_features + 1)

    for _ in range(num_iterations):
        # Add a column of ones to inputs for the intercept term
        inputs_with_bias = np.c_[np.ones(num_samples), inputs]
        # Calculate predictions using dot product between inputs and weights
        predictions = np.dot(inputs_with_bias, weights)
        # Calculate errors
        errors = predictions - outputs
        # Update weights using the mean gradient of the entire dataset
        gradients = np.dot(inputs_with_bias.T, errors) / num_samples
        weights -= learning_rate * gradients

    return weights


def predict(inputs, weights):
    # Add a column of 1s to inputs for the intercept term
    inputs_with_bias = [[1] + x for x in inputs]
    # Calculate predictions using dot product between inputs and weights
    predictions = [sum(w * x for w, x in zip(weights, input_with_bias)) for input_with_bias in inputs_with_bias]
    return predictions


