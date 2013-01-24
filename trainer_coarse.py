import os
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

os.chdir('/home/gavin/dev/Factoid-Question-Answering/corpora/data')

categories = ['HUM', 'LOC', 'NUM', 'ENTY', 'DESC', 'ABBR']

train = load_files(
    'coarse/', categories=categories, shuffle=True, random_state=42)

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LinearSVC()),
])

_ = text_clf.fit(train.data, train.target)

# save text_clf pickle
filehandler = open('coarse.p', 'wb')
pickle.dump(text_clf, filehandler)
filehandler.close()