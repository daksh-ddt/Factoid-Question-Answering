import os
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm.sparse import LinearSVC
from sklearn.pipeline import Pipeline

os.chdir('/home/gavin/Documents/dev/ie/corpora/data/fine/')

categories = ['city',  'country',  'mount',  'other',  'state']

train_LOC = load_files('LOC/',  categories=categories,  shuffle=True,  random_state=42)

# save train_HUM pickle
filehandler = open('pickle_training_LOC.pkl', 'wb') 
pickle.dump(train_LOC, filehandler)
filehandler.close()

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LinearSVC()),
])

_ = text_clf.fit(train_LOC.data, train_LOC.target)

# save text_clf pickle
filehandler = open('pickle_clf_LOC.pkl', 'wb') 
pickle.dump(text_clf, filehandler)
filehandler.close()

# prediction 
new = ['What is the oldest city in the world?',  
    'In what country is the city of Bern located in?', 
    'In what country is the tallest mountain in the world?', 
    'Where can I go to get a great bagel?', 
    'What was the first state to secede from the Union?']

predicted = text_clf.predict(new)
for doc, category in zip(new, predicted):
    print '%r => %s' % (doc, train_LOC.target_names[category])


