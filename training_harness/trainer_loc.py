# -*- coding: utf-8 -*-
'''
Train and pickle a classifier for the fine LOC categories
'''
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

categories = ['city', 'country', 'mount', 'other', 'state']

train_LOC = load_files(
    '../corpora/data/fine/LOC/', categories=categories, shuffle=True, random_state=42)

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LinearSVC()),
])

_ = text_clf.fit(train_LOC.data, train_LOC.target)

filehandler = open('../training_model/fine_loc.p', 'wb')
pickle.dump(text_clf, filehandler)
filehandler.close()

print 'pickled fine_loc.p'
print train_LOC.target_names
