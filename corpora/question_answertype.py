import os
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm.sparse import LinearSVC
from sklearn.pipeline import Pipeline

questions = ['Where is the Amazon river located?', 
       'Where can I get a good sandwhich', 
       'In what state was Columbus born?', 
       'What is the best cheese?', 
       'Who was the first king of Spain?', 
       'How many pounds are in 14 stone?', 
       'Why is poetry so beautiful?', 
       'How much does an aardvark weigh?', 
       'How much does a poodle weigh?']

#def load_coarse_classifier():
os.chdir('/home/gavin/Documents/dev/ie/corpora/data/')
categories = ['HUM', 'LOC', 'NUM', 'ENTY', 'DESC', 'ABBR']
fine_categories = dict(HUM=['desc',  'gr',  'ind',  'title'], 
                       LOC=['city',  'country',  'mount',  'other',  'state'], 
                       NUM=['code',  'count',  'date',  'dist',  'money', 'ord',  'other',  'perc',  'period', 
              'speed',  'temp',  'volsize',  'weight'], 
                        ABBR=['abb',  'exp'], 
                        DESC=['def' , 'desc',  'manner',  'reason'], 
                        ENTY=['animal', 'body',  'color',  'cremat',  'currency',  'dismed',  'event',  'food',  'instru',  
    'lang', 'letter',  'other',  'plant',  'product',  'religion',  'sport',  'substance',  'symbol', 
    'techmeth',  'termeq',  'veh',  'word']
    )
# open train_coarse pickle
data_pickle = open('pickle_training_coarse.pkl', 'rb')
train_coarse = pickle.load(data_pickle)
data_pickle.close()
# open text_clf pickle
training_pickle = open('pickle_clf_coarse.pkl', 'rb')
text_clf = pickle.load(training_pickle)
training_pickle.close()

#def coarse_classify(questions):
predicted = text_clf.predict(questions)
for doc, category in zip(questions, predicted):
    coarse_category = train_coarse.target_names[category]
    print '%r => %s' % (doc, coarse_category)
    
    categories = fine_categories[coarse_category]
    print categories
    
    os.chdir('/home/gavin/Documents/dev/ie/corpora/data/fine/')
    # open fine data pickle
    print 'opening data pickle: ' + 'pickle_training_%s.pkl' % coarse_category
    data_pickle = open('pickle_training_%s.pkl' % coarse_category,  'rb')
    train_data= pickle.load(data_pickle)
    data_pickle.close()
    
    # open text_clf pickle
    print 'opening training pickle: ' + 'pickle_clf_%s.pkl' % coarse_category
    training_pickle = open('pickle_clf_%s.pkl' % coarse_category, 'rb')
    text_clf_fine = pickle.load(training_pickle)
    training_pickle.close()
    
    # fine prediction
    print 'prediction for: ' + doc
    fine_predicted = text_clf_fine.predict(doc)
    print train_data.target_names[fine_predicted[0]]
    
    



    
    
    
