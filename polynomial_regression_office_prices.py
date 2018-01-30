# https://www.hackerrank.com/challenges/predicting-office-space-price/problem


mn = input()
mn = mn.strip().split(' ')

m = int(mn[0])
n = int(mn[1])

X = []
Y = []
for i in range(n):
    x = input()
    x = x.strip().split(' ')
    x = [float(a) for a in x]
    X.append(x[0:m])
    Y.append(x[m:])

q = input()
q = int(q.strip())

X_test = []
for i in range(q):
    x_test = input()
    x_test = x_test.strip().split(' ')
    x_test = [float(a) for a in x_test]
    X_test.append(x_test)


from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

poly = PolynomialFeatures(degree=3)
poly.fit(np.array(X))

regression = LinearRegression()
regression.fit(poly.transform(np.array(X)), Y)

Y_test = regression.predict(poly.transform(np.array(X_test)))
for y_test in Y_test:
    print(round(y_test[0], 2))
