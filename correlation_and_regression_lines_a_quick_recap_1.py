#https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem

# Here are the test scores of 10 students in physics and history:
# Physics Scores  15  12  8   8   7   7   7   6   5   3
# History Scores  10  25  17  11  13  17  20  13  9   15

#15 12 8 8 7 7 7 6 5 3
#10 25 17 11 13 17 20 13 9 15

#Compute Karl Pearson’s coefficient of correlation between these scores.
#Compute the answer correct to three decimal places.

import math

# X = input()
# X = X.strip().split(' ')
# X = [float(x) for x in X]
#
# Y = input()
# Y = Y.strip().split(' ')
# Y = [float(y) for y in Y]

X = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
Y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

n = len(X)

numerator = (n * sum(X[i] * Y[i] for i in range(n)) - sum(X) * sum(Y))
denominator = math.sqrt((n * sum(v**2 for v in X) - sum(X) ** 2) * (n * sum(v ** 2 for v in Y) - sum(Y) ** 2))
p_coefficient = numerator / denominator

print(round(p_coefficient, 3))

#import numpy as np
#print(np.corrcoef(np.array(X), np.array(Y)))