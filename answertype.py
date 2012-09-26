# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 20:38:33 2012

@author: gavin
"""
#import os
import pickle

class Document(object):
    def __init__(self, text, fine, coarse, id):
        self.text = text;
        self.fine = fine
        self.coarse = coarse
        self.id = id
        
class Classifier(object):
    def __init__(self):
        #os.chdir('/home/gavin/dev/QA/static/pickles')
        #os.chdir('/home/ubuntu/app/static/pickles')
        
        # open train_coarse pickle
        # self.data_pickle = open('static/pickles/pickle_training_coarse.pkl', 'rb')
        self.data_pickle = open('/home/ubuntu/www/static/pickles/pickle_training_coarse.pkl', 'rb')
        self.train_coarse = pickle.load(self.data_pickle)
        self.data_pickle.close()
        # open text_clf pickle
        # self.training_pickle = open('static/pickles/pickle_clf_coarse.pkl', 'rb')
        self.training_pickle = open('/home/ubuntu/www/static/pickles/pickle_clf_coarse.pkl', 'rb')
        self.text_clf = pickle.load(self.training_pickle)
        self.training_pickle.close()

        self.categories = ['HUM', 'LOC', 'NUM', 'ENTY', 'DESC', 'ABBR'] 
        self.fine_categories = dict(
    HUM=['desc',  'gr',  'ind',  'title'], 
    LOC=['city',  'country',  'mount',  'other',  'state'], 
    NUM=['code',  'count',  'date',  'dist', 'money', 'ord', 'other', 'perc', 'period', 
         'speed', 'temp', 'volsize', 'weight'], 
    ABBR=['abb',  'exp'], 
    DESC=['def' , 'desc',  'manner',  'reason'], 
    ENTY=['animal', 'body',  'color',  'cremat',  'currency',  'dismed',  'event',  'food',  'instru',  
          'lang', 'letter',  'other',  'plant',  'product',  'religion',  'sport',  'substance',  'symbol', 
          'techmeth',  'termeq',  'veh',  'word']
    )


    def classifyAnswerType(self, question):
        predicted = self.text_clf.predict(question)
        for doc, category in zip(question, predicted):
            coarse_category = self.train_coarse.target_names[category]        
            #os.chdir('/home/ubuntu/app/static/pickles')
            #open fine data pickle
            print 'opening data pickle: ' + 'pickle_training_%s.pkl' % coarse_category
            #data_pickle = open('static/pickles/pickle_training_%s.pkl' % coarse_category, 'rb')
            data_pickle = open('/home/ubuntu/www/static/pickles/pickle_training_%s.pkl' % coarse_category, 'rb')
            train_data= pickle.load(data_pickle)
            data_pickle.close()
            # open text_clf pickle
            print 'opening training pickle: ' + 'pickle_clf_%s.pkl' % coarse_category
            #training_pickle = open('static/pickles/pickle_clf_%s.pkl' % coarse_category, 'rb')
            training_pickle = open('/home/ubuntu/www/static/pickles/pickle_clf_%s.pkl' % coarse_category, 'rb')
            text_clf_fine = pickle.load(training_pickle)
            training_pickle.close()
            # fine prediction
            fine_predicted = text_clf_fine.predict(question)
            answer_type_fine = train_data.target_names[fine_predicted[0]]
            print 'prediction for: %s is %s' % (doc, answer_type_fine)
            return answer_type_fine