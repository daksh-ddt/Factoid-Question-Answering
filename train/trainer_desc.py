import os
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

os.chdir('/home/gavin/dev/Factoid-Question-Answering/corpora/data/fine')

categories = ['def', 'desc', 'manner', 'reason']
train_desc = load_files(
    'DESC/', categories=categories, shuffle=True, random_state=42)

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LinearSVC()),
])

_ = text_clf.fit(train_desc.data, train_desc.target)

filehandler = open('fine_desc.p', 'wb')
pickle.dump(text_clf, filehandler)
filehandler.close()