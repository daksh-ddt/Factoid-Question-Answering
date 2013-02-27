# -*- coding: utf-8 -*-
"""
Modified on Mon Sep 24 19:23:50 2012

@author: gavin hackeling
"""
import urllib
import json
from collections import defaultdict
import re
import unicodedata

# TODO
# TODO incorporate document ranking into entity score
# TODO bundle docs into one to minimize API calls
# -- only ~1 mention of each entity will be returned from alchemy
# must bundle, get entities, and then count entities in bundled doc
def extract(tokens, pos_tagged_documents, ranked_docs):
    answer_freq = defaultdict(int)
    # TODO
    q = ' '.join(tokens).lower()
    def safe_unicode(obj, *args):
        try:
            return unicode(obj, *args)
        except UnicodeDecodeError:
            # obj is byte string
            ascii_text = str(obj).encode('string_escape')
            return unicode(ascii_text)

    def remove_accents(s):
        s = safe_unicode(s)
        return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')

    docs = '. '.join(ranked_docs)
    docs = remove_accents(docs)
    print docs, '\n'
    #print docs.encode('utf-8', 'replace')
    for doc in ranked_docs:
        doc = safe_unicode(doc)
        doc = remove_accents(doc)
        parameters = {
            "apikey": "693f8f0aa9e91878fa2644d2de3735323bf1a35d",
            "text": doc,
            "outputMode": "json"
            }
        base_url = \
        'http://access.alchemyapi.com/calls/text/TextGetRankedNamedEntities?'
        encoded_parameters = urllib.urlencode(parameters)
        url = base_url + encoded_parameters
        json_data = urllib.urlopen(url)
        data = json.load(json_data)

        print 'data\n', data

        for entity in data['entities']:
            if entity['type'].lower() == 'person':
                if 'disambiguated' in entity:
                    entity_name = entity['disambiguated']['name']
                    if '(' in entity_name:
                        entity_name = re.sub(r' \(.+\)', r'', entity_name)
                    if entity_name.lower() not in q:
                        print '%s not in %s' % (entity_name, q)
                        answer_freq[entity_name] += 1
                    else:
                        print 'WARNING: %s in %s' % (entity_name, q)
                else:
                    entity_name = entity['text']
                    if entity_name not in q:
                        print '%s not in %s' % (entity_name, q)
                        answer_freq[entity_name] += 1
                    else:
                        print 'WARNING: %s in %s' % (entity_name, q)

    for i in answer_freq.items():
        print i, answer_freq[i]
    answer = sorted(
        answer_freq.items(), key=lambda x: x[1], reverse=True)[0]
    return answer[0]