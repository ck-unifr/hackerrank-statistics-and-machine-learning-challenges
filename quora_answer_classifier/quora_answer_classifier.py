#https://www.hackerrank.com/challenges/quora-answer-classifier/problem

import sys
#from sklearn.svm import LinearSVC #SVM cannot be used somehow.
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
if sys.version_info[0]>=3: raw_input=input
transformer=DictVectorizer()

X_train = []
Y_train = []

n,m = [int(e) for e in raw_input().split()]

for i in range(n):
    a = raw_input().split()
    a.pop(0)
    Y_train.append(int(a[0]))
    a.pop(0)
    X_train.append({int(e[0]):float(e[1]) for e in [x.split(':') for x in a]})

X_train = transformer.fit_transform(X_train).toarray()
svm = RandomForestClassifier()
svm.fit(X_train, Y_train)

X_test = []
Y_test = []
Test_name = []

for i in range(int(raw_input())):
    a = raw_input().split()
    Test_name.append(a[0])
    a.pop(0)
    X_test.append({int(e[0]):float(e[1]) for e in [x.split(':') for x in a]})

X_test = transformer.transform(X_test).toarray()
Y_test = svm.predict(X_test)
for x,y in zip(Test_name, Y_test):
    print(x+' %+d'%(y,))