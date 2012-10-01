import os
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm.sparse import LinearSVC
from sklearn.pipeline import Pipeline

os.chdir('/home/gavin/Documents/dev/ie/corpora/data/fine/')

categories = ['abb',  'exp']

train_ABBR = load_files('ABBR/',  categories=categories,  shuffle=True,  random_state=42)

# save train_ABBR pickle
filehandler = open('pickle_training_ABBR.pkl', 'wb') 
pickle.dump(train_ABBR, filehandler)
filehandler.close()

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LinearSVC()),
])

_ = text_clf.fit(train_ABBR.data, train_ABBR.target)

# save text_clf pickle
filehandler = open('pickle_clf_ABBR.pkl', 'wb') 
pickle.dump(text_clf, filehandler)
filehandler.close()

# prediction
new = ['What does IBM stand for?', 
       'What is the abbreviation for toothpick?']

predicted = text_clf.predict(new)
for doc, category in zip(new, predicted):
    print '%r => %s' % (doc, train_ABBR.target_names[category])


