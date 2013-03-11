# -*- coding: utf-8 -*-
'''
Train and pickle a classifier for the fine ABBR categories
'''
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

categories = ['abb', 'exp']
train_ABBR = load_files(
    '../corpora/data/fine/ABBR/',
    categories=categories, shuffle=True, random_state=42)

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LinearSVC()),
])

_ = text_clf.fit(train_ABBR.data, train_ABBR.target)

filehandler = open('../training_models/fine_abbr.p', 'wb')
pickle.dump(text_clf, filehandler)
filehandler.close()

print 'pickled fine_abbr.p'
print train_ABBR.target_names
