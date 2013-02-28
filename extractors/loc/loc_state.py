# -*- coding: utf-8 -*-
'''

'''
from __future__ import division
import os
from collections import defaultdict


def extract(tokens, pos_tagged_documents, ranked_docs):
    '''

    '''
    countries_file = os.path.join(os.path.dirname(__file__),
        '../resources/gazetteer_states.txt')
    with open(countries_file) as f:
        countries_gazetteer = f.read().splitlines()

    answer_freq = defaultdict(int)
    for doc in pos_tagged_documents:
        for token, tag in doc:
            if tag == 'NNP':
                token = token.lower()
                if token in countries_gazetteer:
                    answer_freq[token] += 1
    best_answer = sorted(
        answer_freq.items(), key=lambda x: x[1], reverse=True)[0][0]
    return best_answer