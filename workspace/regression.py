#!/usr/bin/env python

import numpy as np
from sklearn.linear_model import LinearRegression

def simple_linear_regression(X, Y):
    model = LinearRegression().fit(X, Y)
    return model.predict(X)

if __name__ == '__main__':
    X = np.array([1, 2, 3, 4, 5]).reshape((-1, 1))
    Y = np.array([2, 3, 4, 6, 7])
    prediction = simple_linear_regression(X, Y)
    print('Prediction:', prediction)