# -*- coding: utf-8 -*-
'''

'''
import sys
sys.path.append('/home/gavin/dev/Factoid-Question-Answering')
from collections import defaultdict
from interfaces import ner_interface


def extract(tokens, pos_tagged_documents, ranked_docs):
    ner = ner_interface.NER_interface()
    answer_freq = defaultdict(int)

    for doc in ranked_docs:
        for entities in ner.get_date_entities(doc):
            for entity in entities:
                answer_freq[entity] += 1

    print len(answer_freq)
    for i in answer_freq.items():
        print i
    if len(answer_freq) == 0:
        answers = ["Sorry, I couldn't find any answers for that."]
    else:
        answers = sorted(
            answer_freq.items(), key=lambda x: x[1], reverse=True)[0]
    return 'factoid', answers[0], answers, None