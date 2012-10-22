import os
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm.sparse import LinearSVC
from sklearn.pipeline import Pipeline

os.chdir('/home/gavin/dev/spyder-workspace/shallowQA/corpora/data')

categories = ['HUM', 'LOC', 'NUM', 'ENTY', 'DESC', 'ABBR', 'BOOL']

train = load_files('coarse/',  categories=categories,  shuffle=True,  random_state=42)
# save train pickle
filehandler = open('pickle_training_coarse.pkl', 'wb') 
pickle.dump(train,  filehandler)
filehandler.close()

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LinearSVC()),
])

_ = text_clf.fit(train.data, train.target)

# save text_clf pickle
filehandler = open('pickle_clf_coarse.pkl', 'wb') 
pickle.dump(text_clf, filehandler)
filehandler.close()

new = ['Where is the Amazon river located?', 
       'Who was the first president', 
       'In what state was Columbus born?', 
       'What is the fastest animal?',
       'Do you like pie?']

predicted = text_clf.predict(new)
for doc, category in zip(new, predicted):
    print '%r => %s' % (doc, train.target_names[category])

