# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 19:34:45 2012

@author: gavin
"""

import nltk
import re
import sys
import random

text = "Businesses have not started to hoard more cash Paul Dales senior economist at Capital Economics wrote."
text = "Businesses have not started to hoard more cash Paul Dales senior economist in England wrote."


AT = re.compile (r'.*\bat\b')
AT = re.compile(r'.*')



IN = re.compile (r'.*\bin\b')

def tokenize_text_and_tag_named_entities(text):
    tokens = []
    # split the source string into a list of sentences
    # for each sentence, split it into words and tag the word with its PoS
    # send the words to the named entity chunker
    # for each chunk containing a Named Entity, build an nltk Tree consisting of the word and its Named Entity tag
    # and append it to the list of tokens for the sentence
    # for each chunk that does not contain a NE, add the word to the list of tokens for the sentence
    for sentence in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence))):
            if hasattr(chunk,  'node'):
                if chunk.node != 'GPE':
                    tmp_tree = nltk.Tree(chunk.node,  [(' '.join(c[0] for c in chunk.leaves()))])
                else:
                    tmp_tree = nltk.Tree('LOCATION',  [(' '.join(c[0] for c in chunk.leaves()))])
                tokens.append(tmp_tree)
            else:
                tokens.append(chunk[0])
    return tokens
    
class doc():
  pass
doc.headline = ['this is expected by nltk.sem.extract_rels but not used in this script']

doc.text = tokenize_text_and_tag_named_entities(text)

def extract_people_at_organizations():
    print 'starting'
    for rel in nltk.sem.extract_rels('PERSON','ORGANIZATION',doc,corpus='ieer',pattern=AT):
      print rel
      print 'subject:' + rel['subjtext'] +  'filler:' + rel['filler'] + ' ' + 'object:' + rel['objtext']
      
def extract_people_at_locations():
    print 'starting'
    for rel in nltk.sem.extract_rels('PERSON','LOCATION',doc,corpus='ieer',pattern=AT):
      print rel
      print 'subject:' + rel['subjtext'] +  'filler:' + rel['filler'] + ' ' + 'object:' + rel['objtext']
      
      
      
      