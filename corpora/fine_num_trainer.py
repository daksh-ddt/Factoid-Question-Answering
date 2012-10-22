import os
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm.sparse import LinearSVC
from sklearn.pipeline import Pipeline

os.chdir('/home/gavin/Documents/dev/ie/corpora/data/fine/')

categories = ['code',  'count',  'date',  'dist',  'money', 'ord',  'other',  'perc',  'period', 
              'speed',  'temp',  'volsize',  'weight']

train_NUM = load_files('NUM/',  categories=categories,  shuffle=True,  random_state=42)

# save train_NUM pickle
filehandler = open('pickle_training_NUM.pkl', 'wb') 
pickle.dump(train_NUM, filehandler)
filehandler.close()

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LinearSVC()),
])

_ = text_clf.fit(train_NUM.data, train_NUM.target)

# save text_clf pickle
filehandler = open('pickle_clf_NUM.pkl', 'wb') 
pickle.dump(text_clf, filehandler)
filehandler.close()

# prediction 
new = ['What is the phone number for Papa Johns?', 
       'How many licks does it take to get to the center of a tootsie pop?', 
       'In what year was Les Paul born?', 
       'How wide is a subway car?', 
       'How much does a bagel cost?', 
       'How does Canada rank in military spending?', 
       'What is the population of Spain?',
       'What percentage of people are awesome?', 
       'How long was Prohibition?', 
       'How fast can a human run?', 
       'How fast can a human run from a cheetah?', 
       'To what temperature should you cook a potato?', 
       'How hot is the sun?', 
       'How big is the sun?', 
       'How much does a manatee weigh?'
       ]

predicted = text_clf.predict(new)
for doc, category in zip(new, predicted):
    print '%r => %s' % (doc, train_NUM.target_names[category])


