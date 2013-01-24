import os
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

os.chdir('/home/gavin/dev/Factoid-Question-Answering/corpora/data/fine')

categories = ['abb', 'exp']
train_ABBR = load_files(
    'ABBR/', categories=categories, shuffle=True, random_state=42)

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LinearSVC()),
])

_ = text_clf.fit(train_ABBR.data, train_ABBR.target)

filehandler = open('fine_abbr.p', 'wb')
pickle.dump(text_clf, filehandler)
filehandler.close()