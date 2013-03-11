# -*- coding: utf-8 -*-
'''

'''
from collections import defaultdict


def extract(tokens, pos_tagged_documents, ranked_docs):
    '''

    '''
    first_tokens = [
        'north', 'south'
    ]
    continents = [
        'north america', 'south america', 'asia', 'europe', 'oceania',
        'australia', 'africa', 'antarctica'
    ]

    answer_freq = defaultdict(int)
    for doc in pos_tagged_documents:
        for index, tagged_token in enumerate(doc):
            token = tagged_token[0]
            tag = tagged_token[1]
            if tag == 'NNP':
                if token.lower() in continents:
                    answer_freq[token] += 1
                elif token.lower() in first_tokens:
                    multi_token_name = ' '.join([token, doc[index + 1][0]])
                    if multi_token_name.lower() in continents:
                        answer_freq[multi_token_name] += 1
    answers = sorted(
        answer_freq.items(), key=lambda x: x[1], reverse=True)
    return 'factoid', answers[0], answers, None