# -*- coding: utf-8 -*-
"""
Modified on Mon Sep 24 19:23:50 2012

@author: gavin hackeling
"""
import sys
sys.path.append('/home/gavin/dev/Factoid-Question-Answering')
import urllib
import json
from collections import defaultdict
import re
import unicodedata
#from nlp import text_encoding
from interfaces import ner_interface


def extract(tokens, pos_tagged_documents, ranked_docs):
    ner = ner_interface.NER_interface()
    answer_freq = defaultdict(int)

    for doc in ranked_docs:
        for entities in ner.get_organization_entities(doc):
            for entity in entities:
                answer_freq[entity] += 1

    for i in answer_freq.items():
        print i
    if len(answer_freq) == 0:
        answers = ["Sorry, I could not find any answers for that."]
    else:
        answers = sorted(
            answer_freq.items(), key=lambda x: x[1], reverse=True)[0]
    return 'factoid', answers[0], answers, None