import os
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm.sparse import LinearSVC
from sklearn.pipeline import Pipeline

os.chdir('/home/gavin/Documents/dev/ie/corpora/data/fine/')

categories = ['desc',  'gr',  'ind',  'title']

# open train_HUM pickle
data_pickle = open('pickle_training_HUM.pkl', 'rb')
train_HUM = pickle.load(data_pickle)
data_pickle.close()

# open text_clf pickle
training_pickle = open('pickle_clf_HUM.pkl', 'rb')
text_clf = pickle.load(training_pickle)
training_pickle.close()

new = ['Who was the first man on the moon?',  
    'What company produces the xbox 360?', 
    'Who is Selena Gomez?', 
    'What is the title of Obama?', 
    'What is the name of Jackie Chan\'s grandmother?']

predicted = text_clf.predict(new)
for doc, category in zip(new, predicted):
    print '%r => %s' % (doc, train_HUM.target_names[category])
