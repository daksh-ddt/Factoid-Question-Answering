import os
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm.sparse import LinearSVC
from sklearn.pipeline import Pipeline

os.chdir('/home/gavin/Documents/dev/ie/corpora/data/fine/')

categories = ['desc',  'gr',  'ind',  'title']

train_HUM = load_files('HUM/',  categories=categories,  shuffle=True,  random_state=42)

# save train_HUM pickle
filehandler = open('pickle_training_HUM.pkl', 'wb') 
pickle.dump(train_HUM, filehandler)
filehandler.close()

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LinearSVC()),
])

_ = text_clf.fit(train_HUM.data, train_HUM.target)

# save text_clf pickle
filehandler = open('pickle_clf_HUM.pkl', 'wb') 
pickle.dump(text_clf, filehandler)
filehandler.close()

# prediction 
new = ['Who was the first man on the moon?',  
    'What company produces the xbox 360?', 
    'Who is Selena Gomez?', 
    'What is the title of Obama?', 
    'What is the name of Jackie Chan\'s grandmother?']

predicted = text_clf.predict(new)
for doc, category in zip(new, predicted):
    print '%r => %s' % (doc, train_HUM.target_names[category])


