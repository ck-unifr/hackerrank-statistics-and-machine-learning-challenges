#https://www.hackerrank.com/challenges/computing-the-correlation/problem

import math

def linear_correlation(X, Y):
    n = len(X)
    numerator = (n * sum(X[i] * Y[i] for i in range(n)) - sum(X) * sum(Y))
    denominator = math.sqrt((n * sum(v ** 2 for v in X) - sum(X) ** 2) * (n * sum(v ** 2 for v in Y) - sum(Y) ** 2))
    p_coefficient = numerator / denominator

    return p_coefficient

n = input()
n = n.strip()
n = int(n)

M = []
P = []
C = []
for i in range(n):
    x = input()
    x = x.strip().split('\t')
    x = [float(a) for a in x]
    M.append(x[0])
    P.append(x[1])
    C.append(x[2])

print(round(linear_correlation(M, P), 2))
print(round(linear_correlation(P, C), 2))
print(round(linear_correlation(C, M), 2))



