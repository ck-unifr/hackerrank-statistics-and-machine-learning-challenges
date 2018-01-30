#https://www.hackerrank.com/challenges/stat-warmup/problem

# Input Format

# The first line contains the number of integers.
# The second line contains space separated integers for which you need to find the
# mean, median, mode, standard deviation and confidence interval boundaries.
# Note
# Use the constant 1.96 while computing the confidence interval.




from scipy import stats
import math

N = input()
N = N.strip()
N = int(N)

X = input()
X = X.strip().split(' ')
X = [float(x) for x in X]

# mean
mean = sum(X)/len(X)

# median
X = sorted(X)
if len(X) % 2 != 0:
    median = X[int(len(X) / 2)]
else:
    median = (X[int(len(X) / 2)] + X[int(len(X) / 2)-1])/2


# mode
mode = stats.mode(X)

# standard deviation (SD)
sd = math.sqrt(sum([math.pow(x - mean, 2) for x in X]) / len(X))


# confidence interval for the mean
cf1 = mean - 1.96*(sd/(len(X)**0.5))
cf2 = mean + 1.96*(sd/(len(X)**0.5))


print(round(mean, 1))
print(round(median, 1))
print(mode[0][0])
print(round(sd, 1))
print(round(cf1, 1), round(cf2, 1))