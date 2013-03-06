# -*- coding: utf-8 -*-
'''
Train and pickle a classifier for the coarse categories
'''
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

#categories = ['HUM', 'LOC', 'NUM', 'ENTY', 'DESC', 'ABBR', 'UTIL']
categories = ['HUM', 'LOC', 'NUM', 'ENTY', 'DESC', 'ABBR', ]

train_COARSE = load_files(
    '../corpora/data/coarse/',
    categories=categories, shuffle=True, random_state=42)

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LinearSVC()),
])

_ = text_clf.fit(train_COARSE.data, train_COARSE.target)

filehandler = open('../training_model/coarse.p', 'wb')
pickle.dump(text_clf, filehandler)
filehandler.close()

print 'pickled coarse.p'
print train_COARSE.target_names
