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
import coref_resolver


def extract(tokens, pos_tagged_documents, ranked_docs):
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
        return result
    else:
        # need to fallback to web
        return 'nothing'