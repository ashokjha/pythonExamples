# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 21:26:35 2021

@author: Ashok Kumar Jha
"""

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
a1 = np.array([1, 2, 3, 4], dtype='int64')
print(a1.dtype, a1.shape)
a2 = np.array([5, 6, 7, 8], dtype='int64')
print(a1*a2)
print(a1+a2)


x = [i for i in range(10)]
y = [i for i in range(10)]
X = np.array(x)
Y = np.array(y)
print(X, Y, sep=',')
X = np.array(x).reshape(-1, 1)
Y = np.array(y).reshape((-1, 1))
print(X, Y, sep='\n')
lnrRegressor = LinearRegression()
lnrRegressor.fit(X, Y)
Y_pred = lnrRegressor.predict(X)
alpha = str(round(lnrRegressor.intercept_[0], 5))
beta = str(round(lnrRegressor.coef_[0][0], 5))
fig, ax = plt.subplots()
ax.set_title(f"Alpha - {alpha}, Beta - {beta}")
ax.scatter(X, Y)
ax.plot(X, Y_pred, c='y')
