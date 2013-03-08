# -*- coding: utf-8 -*-
"""
TODO:
    need to add unstructured fallback

Modified on Wed Mar 6 21:18:50 2013

@author: gavin hackeling

'who was John Lennon?'
'who is the Queen Mother?'
'who is Ishmael in Moby Dick?'

"""
import urllib
import json
import re
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import pos_tag
import coref_resolver


def extract(tokens, pos_tagged_documents, ranked_docs):

    def split_sentence_into_100_char_parts(sentence):
        '''
        Split a sentence along whitespace into <100 character chunks.
        '''
        parts = []
        index = find_index_below_100(sentence, ' ')
        parts.append(sentence[0:index])
        print 'adding "%s" with len %s' % (sentence[0:index], len(sentence[0:index]))
        sentence = sentence[index+1:]
        print 'remaining sentence is: %s' % sentence
        return parts

    def find_index_below_100(string, character):
        '''
        Return the index of the space closest to index 100.
        '''
        return [i for i in find(string, character) if i < 100][-1]

    def find(string, character):
        '''
        Get the indices of the character in the string.
        '''
        return [i for i, c in enumerate(string) if c == character]

    base_url = 'https://www.googleapis.com/freebase/v1/text/en/'
    coref = coref_resolver.Coref_resolver()

    # Get possible entities
    people = coref.get_people_entities(' '.join(tokens))
    # Format the entity for Freebase
    people = [p[0].replace(' ', '_').lower() for p in people]
    print 'People:', people

    # Will there ever be multiple people in the query?
    #for person in people:
        #url = base_url + person
        #json_data = urllib.urlopen(url)
        #data = json.load(json_data)
        #print data['result']

    if len(people) != 0:
        url = base_url + people[0]
        json_data = urllib.urlopen(url)
        data = json.load(json_data)
        result = data['result']
        result = re.sub(r'\(.+\)', '', result)
        # need to process short result and long result

        skip_tags = ['']
        print '\nresult processing'

        result_sentences = sent_tokenize(result)
        for i in result_sentences:
            print '*', i

        sentence = result_sentences[0]
        if len(sentence) < 100:
            print 'first sentence is adequate'
            short_answer = sentence
        else:
            parts = split_sentence_into_100_char_parts(sentence)
            # Need to find the first space before character #100




        short_answer = None
        long_answer = []
        return 'description', short_answer, None, long_answer
    else:
        # need to fallback to web
        return 'description', 'Need to implement fallback', None, 'long_answer'