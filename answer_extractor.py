# -*- coding: utf-8 -*-
'''
Load the appropriate extraction module for the question type
and extract candidate answers for verification.

'''
from extractors import hum_ind


class Answer_extractor:

    def __init__(self):
        hum_map = {
            'desc': 'hum_desc',
            'gr': 'hum_gr',
            'ind': hum_ind,
            'title': 'hum_title'
        }

        num_map = {
            'code': 'num_code',
            'count': 'num_count',
            'date': 'num_date',
            'dist': 'num_dist',
            'money': 'num_money',
            'ord': 'num_ord',
            'other': 'num_other',
            'perc': 'num_perc',
            'period': 'num_period',
            'speed': 'num_speed',
            'temp': 'num_temp',
            'volsize': 'num_volsize',
            'weight': 'num_weight'
        }

        self.extraction_map = {
            'hum': hum_map,
            'num': num_map,

        }

    def extract_answers(
        self, tokens, pos_tagged_documents, coarse, fine, keywordsList):
        extractor = self.extraction_map[coarse][fine]
        candidate_answers = extractor.extract(tokens, pos_tagged_documents)
        return candidate_answers