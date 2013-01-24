import os
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

os.chdir('/home/gavin/dev/Factoid-Question-Answering/corpora/data/fine')

categories = ['animal', 'body', 'color', 'cremat', 'currency', 'dismed',
            'event', 'food', 'instru', 'lang', 'letter', 'other', 'plant',
            'product', 'religion', 'sport', 'substance', 'symbol', 'techmeth',
            'termeq', 'veh', 'word']

train_ENTY = load_files(
    'ENTY/', categories=categories, shuffle=True, random_state=42)

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LinearSVC()),
])

_ = text_clf.fit(train_ENTY.data, train_ENTY.target)

filehandler = open('fine_enty.p', 'wb')
pickle.dump(text_clf, filehandler)
filehandler.close()