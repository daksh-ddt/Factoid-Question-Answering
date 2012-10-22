import os
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm.sparse import LinearSVC
from sklearn.pipeline import Pipeline

os.chdir('/home/gavin/Documents/dev/ie/corpora/data/fine/')

categories = ['def' , 'desc',  'manner',  'reason']

# open train_DESC pickle
data_pickle = open('pickle_training_DESC.pkl', 'rb')
train_DESC= pickle.load(data_pickle)
data_pickle.close()

# open text_clf pickle
training_pickle = open('pickle_clf_DESC.pkl', 'rb')
text_clf = pickle.load(training_pickle)
training_pickle.close()

new = []
predicted = text_clf.predict(new)
for doc, category in zip(new, predicted):
    print '%r => %s' % (doc, train_DESC.target_names[category])
