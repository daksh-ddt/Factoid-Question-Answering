# -*- coding: utf-8 -*-
'''
Load the appropriate extraction module for the question type
and extract candidate answers for verification.

'''
from extractors import hum_ind
from extractors import hum_ind_alchemy
from extractors import num_count
from extractors import loc_country
from extractors import loc_cont


class Answer_extractor:

    def __init__(self):
        hum_map_alchemy = {
            'desc': 'hum_desc',
            'gr': 'hum_gr',
            'ind': hum_ind_alchemy,
            'title': 'hum_title'
        }

        hum_map = {
            'desc': 'hum_desc',
            'gr': 'hum_gr',
            'ind': hum_ind,
            'title': 'hum_title'
        }

        loc_map = {
            'attr': '',
            'bodwat': '',
            'city': '',
            'cont': loc_cont,
            'country': loc_country,
            'mount': '',
            'other': '',
            'rest': '',
            'retail': '',
            'state': ''
        }

        num_map = {
            'code': 'num_code',
            'count': num_count,
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
            'loc': loc_map,
        }

        self.extraction_map_alchemy = {
            'hum': hum_map_alchemy,
            'num': num_map,
            'loc': loc_map,
        }

    def extract_answers(self, tokens,
                        pos_tagged_documents, ranked_docs,
                        coarse, fine, keywordsList, use_alchemy):
        if not use_alchemy:
            extractor = self.extraction_map[coarse][fine]
            ranked_answers = extractor.extract(
                tokens, pos_tagged_documents)
        else:
            print('using alchemy api')
            extractor = self.extraction_map_alchemy[coarse][fine]
            ranked_answers = extractor.extract(
                tokens, pos_tagged_documents, ranked_docs)
        return ranked_answers