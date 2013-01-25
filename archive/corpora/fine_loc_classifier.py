import os
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm.sparse import LinearSVC
from sklearn.pipeline import Pipeline

os.chdir('/home/gavin/Documents/dev/ie/corpora/data/fine/')

categories = ['city',  'country',  'mount',  'other',  'state']

# open train_HUM pickle
data_pickle = open('pickle_training_LOC.pkl', 'rb')
train_LOC = pickle.load(data_pickle)
data_pickle.close()

# open text_clf pickle
training_pickle = open('pickle_clf_LOC.pkl', 'rb')
text_clf = pickle.load(training_pickle)
training_pickle.close()

new = ['What is the oldest city in the world?',  
    'In what country is the city of Bern located in?', 
    'In what country is the tallest mountain in the world?', 
    'Where can I go to get a great bagel?', 
    'What was the first state to secede from the Union?']

predicted = text_clf.predict(new)
for doc, category in zip(new, predicted):
    print '%r => %s' % (doc, train_LOC.target_names[category])
