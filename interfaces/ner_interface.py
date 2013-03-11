# -*- coding: utf-8 -*-
'''
I will also require coref for place names: eg. Atlanta == Atlanta, Georgia
'''
from itertools import chain
import re
import ner


class NER_interface:

    def __init__(self):
        self.tagger = ner.SocketNER(
            host='localhost', port=8008, output_format="slashTags")

    def get_tagged_text(self, text):
        return self.tagger.get_entities(text.encode('utf-8', 'replace'))

    def get_entities(self, text):
        chunks = self.tagger.get_entities(text.encode('utf-8', 'replace'))
        return [chunks[c] for c in chunks if c != 'O']

    def get_person_entities(self, text):
        chunks = self.tagger.get_entities(text.encode('utf-8', 'replace'))
        return [chunks[c] for c in chunks if c == 'PERSON']

    def get_location_entities(self, text):
        chunks = self.tagger.get_entities(text.encode('utf-8', 'replace'))
        return [chunks[c] for c in chunks if c == 'LOCATION']

    def get_time_entities(self, text):
        chunks = self.tagger.get_entities(text.encode('utf-8', 'replace'))
        return [chunks[c] for c in chunks if c == 'TIME']

    def get_organization_entities(self, text):
        chunks = self.tagger.get_entities(text.encode('utf-8', 'replace'))
        return [chunks[c] for c in chunks if c == 'ORGANIZATION']

    def get_money_entities(self, text):
        chunks = self.tagger.get_entities(text.encode('utf-8', 'replace'))
        return [chunks[c] for c in chunks if c == 'MONEY']

    def get_percent_entities(self, text):
        chunks = self.tagger.get_entities(text.encode('utf-8', 'replace'))
        return [chunks[c] for c in chunks if c == 'PERCENT']

    def get_date_entities(self, text):
        chunks = self.tagger.get_entities(text.encode('utf-8', 'replace'))
        return [chunks[c] for c in chunks if c == 'DATE']

if __name__ == '__main__':
    ner_interface = NER_interface()