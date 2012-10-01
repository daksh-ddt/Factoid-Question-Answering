import os
import pickle
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm.sparse import LinearSVC
from sklearn.pipeline import Pipeline

questions = ['Where is the Amazon river located?']

expanded_types = dict(
    HUM='Human', 
    LOC='Location', 
    NUM='Number', 
    ABBR='Abbreviation', 
    DESC='Description', 
    ENTY='Entity', 
    desc='Description', 
    gr='Organization or group of people', 
    ind='Individual person', 
    title='Title', 
    city='City',
    country='Country', 
    state='Geo-political state', 
    mount='Mountain range', 
    other='Other', 
    code='Code', 
    count='Count or quantity', 
    date='Date', 
    money='Money', 
    ord='Order or rank', 
    perc='Percentage', 
    period='Period or duration', 
    speed='Speed', 
    temp='Temperature', 
    volsize='Volume or size', 
    weight='Weight', 
    abb='Abbreviation', 
    exp='Expansion of an abbreviation', 
    manner='Manner or way', 
    reason='Reason or cause', 
    animal='Animal', 
    body='Body or organ', 
    color='color', 
    cremat='Creative or cultural material', 
    currency='Currency', 
    dismed='Disease or Medicine', 
    event='Event', 
    food='Food', 
    instru='Instrument', 
    lang='Language', 
    letter='Alphabet letter', 
    plant='Plant', 
    product='Product', 
    religion='Religion', 
    sport='Sport', 
    substance='Material or substance', 
    symbol='Symbol', 
    techmeth='Technological method', 
    termeq='Equivalent term',
   veh='Vehicle', 
  word='Word', 
                      )
expanded_types['def'] = 'Definition'


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

#def coarse_classify(question):
predicted = text_clf.predict(question)
print predicted
print expanded_types[train_coarse.target_names[predicted[0]]]

for doc, category in zip(questions, predicted):
    coarse_category = train_coarse.target_names[category]
    print '%r => %s' % (doc, expanded_types[coarse_category])
    
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
    print expanded_types[train_data.target_names[fine_predicted[0]]]
    
    



    
    
    
