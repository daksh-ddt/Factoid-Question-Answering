import os
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm.sparse import LinearSVC
from sklearn.pipeline import Pipeline

os.chdir('/home/gavin/Documents/dev/ie/corpora/data/')

categories = ['HUM', 'LOC', 'NUM', 'ENTY', 'DESC', 'ABBR']

# open train_coarse pickle
data_pickle = open('pickle_training_coarse.pkl', 'rb')
train_coarse = pickle.load(data_pickle)
data_pickle.close()

# open text_clf pickle
training_pickle = open('pickle_clf_coarse.pkl', 'rb')
text_clf = pickle.load(training_pickle)
training_pickle.close()

new = ['Where is the Amazon river located?', 
       'Where can I get a good sandwhich', 
       'In what state was Columbus born?', 
       'What is the best cheese?']
       
predicted = text_clf.predict(new)
for doc, category in zip(new, predicted):
    print '%r => %s' % (doc, train_coarse.target_names[category])
