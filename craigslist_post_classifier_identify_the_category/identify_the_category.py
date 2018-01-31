#https://www.hackerrank.com/challenges/craigslist-post-classifier-the-category/problem

import json
import sys
if sys.version_info[0]>=3: raw_input=input
from sklearn.svm import LinearSVC
from sklearn.feature_extraction import DictVectorizer


transformer = DictVectorizer()

X_train = []
Y_train = []
f = open('training.json')
for i in range(int(f.readline())):
	h = json.loads(f.readline())
	Y_train.append(h['category'])
	del h['category']
	X_train.append(h)
f.close()

X_train = transformer.fit_transform(X_train)
svm = LinearSVC()
svm.fit(X_train,Y_train)

X_test=[]
for i in range(int(raw_input())):
	h = json.loads(raw_input())
	X_test.append(h)
X_test = transformer.transform(X_test)
Y_test = svm.predict(X_test)
for y_test in Y_test:
    print(y_test)