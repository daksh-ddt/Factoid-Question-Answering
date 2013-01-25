import os
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm.sparse import LinearSVC
from sklearn.pipeline import Pipeline

os.chdir('/home/gavin/Documents/dev/ie/corpora/data/fine/')

categories = ['animal', 'body',  'color',  'cremat',  'currency',  'dismed',  'event',  'food',  'instru',  
    'lang', 'letter',  'other',  'plant',  'product',  'religion',  'sport',  'substance',  'symbol', 
    'techmeth',  'termeq',  'veh',  'word']
    
train_ENTY = load_files('ENTY/',  categories=categories,  shuffle=True,  random_state=42)

# save train_DESC pickle
filehandler = open('pickle_training_ENTY.pkl', 'wb') 
pickle.dump(train_ENTY, filehandler)
filehandler.close()

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LinearSVC()),
])

_ = text_clf.fit(train_ENTY.data, train_ENTY.target)

# save text_clf pickle
filehandler = open('pickle_clf_ENTY.pkl', 'wb') 
pickle.dump(text_clf, filehandler)
filehandler.close()

# prediction
new = ['What mammal lays eggs?', 
       'What organ is responsible for the immune system?', 
       'What are the school colors of UNC?',
       'What is the name of Michael Bay\'s 2011 masterpiece film?', 
       'What currency does finland use?', 
       'What disease was deadliest in the 18th century?', 
       'What happened in Japan in 1982?', 
       'What kind of food is served at McDonald\s?', 
       'What kinds of instruments does Fender make?', 
       'What language do Canadians speak?', 
       'What letters are absent in the arabic alphabet?', 
       'What is the fastest plane in the world?', 
       'What kinds of trees grow well in indirect sunlight?',
       'What does H&M sell?', 
       'What is the dominant religion in China?', 
       'What sport did Michael Jordan play?', 
       'What is a mattress made of?', 
       'What does the logo for IBM look like?', 
       'How do you fix a flat tire?', 
       'What do you call a shape with 11 sides?', 
       'What does Batman drive?', 
       'What is the word for a person who only eats potatoes?', 
       ]

predicted = text_clf.predict(new)
for doc, category in zip(new, predicted):
    print '%r => %s' % (doc, train_ENTY.target_names[category])


