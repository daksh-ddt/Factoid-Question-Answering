# -*- coding: utf-8 -*-
'''
Train and pickle a classifier for the fine DESC categories
'''
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

categories = ['def', 'desc', 'manner', 'reason']
train_desc = load_files(
    '../corpora/data/fine/DESC/',
    categories=categories, shuffle=True, random_state=42)

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LinearSVC()),
])

_ = text_clf.fit(train_desc.data, train_desc.target)

filehandler = open('../training_model/fine_desc.p', 'wb')
pickle.dump(text_clf, filehandler)
filehandler.close()

print 'pickled fine_desc.p'
print train_desc.target_names
