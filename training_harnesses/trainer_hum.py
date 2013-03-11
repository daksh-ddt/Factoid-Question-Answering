# -*- coding: utf-8 -*-
'''
Train and pickle a classifier for the fine HUM categories
'''
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

categories = ['desc', 'gr', 'ind', 'title']

train_HUM = load_files(
    '../corpora/data/fine/HUM/',
    categories=categories, shuffle=True, random_state=42)

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LinearSVC()),
])

_ = text_clf.fit(train_HUM.data, train_HUM.target)

filehandler = open('../training_models/fine_hum.p', 'wb')
pickle.dump(text_clf, filehandler)
filehandler.close()

print 'pickled fine_hum.p'
print train_HUM.target_names
