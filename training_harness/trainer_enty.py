# -*- coding: utf-8 -*-
'''
Train and pickle a classifier for the fine ENTY categories
'''
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

categories = ['animal', 'body', 'color', 'cremat', 'currency', 'dismed',
            'event', 'food', 'instru', 'lang', 'letter', 'other', 'plant',
            'product', 'religion', 'sport', 'substance', 'symbol', 'techmeth',
            'termeq', 'veh', 'word']

train_ENTY = load_files(
    '../corpora/data/fine/ENTY/', categories=categories, shuffle=True, random_state=42)

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LinearSVC()),
])

_ = text_clf.fit(train_ENTY.data, train_ENTY.target)

filehandler = open('../training_model/fine_enty.p', 'wb')
pickle.dump(text_clf, filehandler)
filehandler.close()

print 'pickled fine_enty.p'
print train_ENTY.target_names
