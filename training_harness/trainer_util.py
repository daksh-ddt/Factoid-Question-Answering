# -*- coding: utf-8 -*-
'''
Train and pickle a classifier for the fine NUM categories
'''
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

categories = ['more', 'wrong']

train_NUM = load_files(
    '../corpora/data/fine/UTIL/',
    categories=categories, shuffle=True, random_state=42)

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LinearSVC()),
])

_ = text_clf.fit(train_NUM.data, train_NUM.target)

filehandler = open('../training_model/fine_util.p', 'wb')
pickle.dump(text_clf, filehandler)
filehandler.close()

print 'pickled fine_util.p'
print train_NUM.target_names
