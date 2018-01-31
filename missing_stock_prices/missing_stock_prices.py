#https://www.hackerrank.com/challenges/missing-stock-prices/problem

import numpy as np
from scipy import interpolate

n = int(input())
prices = []
for i in range(n):
    time, price = input().split("\t")
    prices.append(price)

X = []
Y = []
X_missing = []
for i in range(n):
    if not "Missing" in prices[i]:
        X.append(i)
        Y.append(float(prices[i]))
    else:
        X_missing.append(i)

Y = np.array(Y)
f = interpolate.UnivariateSpline(X, Y, s=1)

for i in X_missing:
    print(f(i))