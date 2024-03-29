
class MyLinearMultivariateRegression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = []

    def fit(self, trainInputs, trainOutputs):
        X1_squared = [x[0] ** 2 for x in trainInputs]
        X2_squared = [x[1] ** 2 for x in trainInputs]
        X1y = [trainInputs[i][0] * trainOutputs[i] for i in range(len(trainInputs))]
        X2y = [trainInputs[i][1] * trainOutputs[i] for i in range(len(trainInputs))]
        X1X2 = [trainInputs[i][0] * trainInputs[i][1] for i in range(len(trainInputs))]
        X1 = [x[0] for x in trainInputs]
        X2 = [x[1] for x in trainInputs]
        y = trainOutputs
        n = len(trainInputs)

        sum_X1 = sum(X1)
        sum_X2 = sum(X2)
        sum_y = sum(y)
        sum_X1_squared = sum(X1_squared)
        sum_X2_squared = sum(X2_squared)
        sum_X1y = sum(X1y)
        sum_X2y = sum(X2y)
        sum_X1X2 = sum(X1X2)

        sum_x1_squared = sum_X1_squared - sum_X1 ** 2 / n
        sum_x2_squared = sum_X2_squared - sum_X2 ** 2 / n
        sum_x1y = sum_X1y - sum_X1 * sum_y / n
        sum_x2y = sum_X2y - sum_X2 * sum_y / n
        sum_x1x2 = sum_X1X2 - sum_X1 * sum_X2 / n

        w1 = (sum_x2_squared * sum_x1y - sum_x1x2 * sum_x2y) / (sum_x1_squared * sum_x2_squared - sum_x1x2 ** 2)
        w2 = (sum_x1_squared * sum_x2y - sum_x1x2 * sum_x1y) / (sum_x1_squared * sum_x2_squared - sum_x1x2 ** 2)
        w0 = sum_y / n - w1 * sum_X1 / n - w2 * sum_X2 / n

        self.intercept_ = w0
        self.coef_ = [w1, w2]

    # predict the outputs for some new inputs (by using the learnt model)
    def predict(self, x):
        return [self.intercept_ + self.coef_[0] * val[0] + self.coef_[1] * val[1] for val in x]


def mean_absolute_error(computedValidationOutputs, validationOutputs):
    # compute the differences between the predictions and real outputs
    # "manual" computation
    error = 0.0
    for t1, t2 in zip(computedValidationOutputs, validationOutputs):
        error += (t1 - t2) ** 2
    error = error / len(validationOutputs)
    return error
