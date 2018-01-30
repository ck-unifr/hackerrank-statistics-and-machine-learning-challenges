#https://www.hackerrank.com/challenges/correlation-and-regression-lines-7/problem

# Here are the test scores of 10 students in physics and history:
# Physics Scores  15  12  8   8   7   7   7   6   5   3
# History Scores  10  25  17  11  13  17  20  13  9   15

#15 12 8 8 7 7 7 6 5 3
#10 25 17 11 13 17 20 13 9 15

# Compute the slope of the line of regression obtained while treating Physics as the independent variable.
# Compute the answer correct to three decimal places.

import math

X = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
Y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

mean_x = float(sum(X))/len(X)
mean_y = float(sum(Y))/len(Y)

A = 0
B = 0
C = 0
for i in range(len(X)):
    A += (X[i]-mean_x)*(Y[i]-mean_y)
    B += (X[i]-mean_x)**2
    C += (Y[i]-mean_y)**2

r = float(A) / math.sqrt(B * C)

std_x = math.sqrt((float(B)/(len(X))))
std_y = math.sqrt((float(C)/(len(Y))))

slope = float(r*std_y)/std_x
print(round(slope, 3))