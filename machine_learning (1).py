# -*- coding: utf-8 -*-
"""machine_learning.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HZH3-4oUsYiH6Eaiqc5FfJ-LNBBe50Vi
"""

import numpy as np
import sklearn
from sklearn import linear_model

height = [[4.0], [5.0], [6.0], [7.0], [8.0], [9.0], [10.0]]
weight = [8, 10, 12, 14, 16, 18, 20]

reg = linear_model.LinearRegression()
reg.fit(height, weight)

X_height = [[12.0]]
print(reg.predict(X_height))

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

# Step 1 - Data
x = [[4.0], [5.0], [6.0], [7.0], [8.0], [9.0], [10.0]]
y = [16, 25, 36, 49, 64, 81, 100]

# Step 2 - Fitting Linear Regression
lin_reg = LinearRegression()
lin_reg.fit(x, y)

# Step 3 - Linear Regression prediction
print(lin_reg.predict([[11]]))

# Step 4 - Polynomial Regression
polynomial_regression = make_pipeline(
    PolynomialFeatures(degree=2, include_bias=False),
    LinearRegression(),
)
polynomial_regression.fit(x, y)
X_height = [[20.0]]
target_predicted = polynomial_regression.predict(X_height)

# Step 5 - Print the prediction
print(target_predicted)
python machine_learning.py
