#https://www.hackerrank.com/challenges/document-classification/problem


import sys
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier


transformer=HashingVectorizer(stop_words='english')


train_file_path = 'trainingdata.txt'

X_train = []
Y_train = []
f=open('trainingdata.txt')
# with open(...) as f:
#     for line in f:
for i in range(int(f.readline())):
    s = f.readline().rstrip()
    idx = s.find(' ')
    X_train.append(s[idx+1:])
    Y_train.append(int(s[:idx]))
f.close()


# X_train = transformer.fit_transform(X_train)
# clf = LinearSVC()
# clf = RandomForestClassifier(n_estimators=100, max_depth=4)

clf = Pipeline([('vect', CountVectorizer(max_df = 8.5)),
                ('tfidf', TfidfTransformer()),
                ('clf', LinearSVC()),
])

clf.fit(X_train, Y_train)

X_test=[]
if sys.version_info[0]>=3: raw_input=input
for i in range(int(raw_input())):
    s = raw_input().rstrip()
    X_test.append(s)
# X_test = transformer.transform(X_test)
test_label=clf.predict(X_test)

for e in test_label:
    print(e)
