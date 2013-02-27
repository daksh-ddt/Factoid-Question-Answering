# -*- coding: utf-8 -*-
'''
Rank candidate texts by their similarity to the query.

@author: gavin hackeling
'''
from __future__ import division
from nltk import word_tokenize
from math import log
from collections import defaultdict


class BM25_calc:

    def __init__(self, query, c):
        self.k1 = 1.2
        self.b = 0.75
        #self.stop_words = ['the', 'is', 'are', 'am', 'was', 'have', 'had', 'has',
                        #'a', 'an', 'be', 'did', 'does', 'do', 'to', ]
        #self.query = [t.lower() for t in query if t.lower() not in self.stop_words]
        self.query = [t.lower() for t in query]
        self.original_collection = c
        c = [d.lower() for d in c]
        self.collection = [word_tokenize(d) for d in c]
        self.avg_len = sum([len(d) for d in self.collection]) / len(c)
        self.freq_counter = defaultdict(int)

    def get_num_docs_containing(self, token):
        num = 0
        for document in self.collection:
            if token in document:
                num += 1
        return num

    # TODO do this once
    def get_tf(self, token, document):
        counter = defaultdict(int)
        for word in document:
            #if word not in self.stop_words:
            counter[word] += 1
        return counter[token]

    def get_idf(self, token):
        N = len(self.collection)
        nq = self.get_num_docs_containing(token)
        top = N - nq + 0.5
        bottom = nq + 0.5
        idf = log(top / bottom)
        return max(.5, idf)

    def score(self, document):
        score = 0
        for token in self.query:
            tf = self.get_tf(token, document)
            idf = self.get_idf(token)
            top = tf * (self.k1 + 1)
            bottom = tf + self.k1 * (
                1 - self.b + self.b * (len(document) / self.avg_len))
            s = idf * (top / bottom)
            score += max(s, 0)
        return score

    def rank(self):
        scores = []
        for document_index, document in enumerate(self.collection):
            s = self.score(document)
            scores.append((s, document, document_index))

        scores.sort(key=lambda tup: tup[0], reverse=True)
        originals = []
        for i in scores:
            originals.append(self.original_collection[i[2]])

        return originals


if __name__ == '__main__':
    query = 'did the Ravens win the Super Bowl?'
    query = word_tokenize(query)
    collection = [
        'The Baltimore Ravens would later win Super Bowl XLVII in 2013 against the San Francisco 49ers.',
        "Ray Lewis was a member of both Ravens' Super Bowl wins.",
        '75 Jonathan Ogden elected in 2013 played for Ravens 1996–2007 won Super Bowl XXXV Retired numbers.',
        'The Ravens officially have no retired numbers.',
        "Michael Crabtree never had a chance to make a catch in the end zone on what turned out to be the San Francisco 49ers' last play of Super Bowl XLVII a 3431 loss to ",
        'Ravens quarterback Trent Dilfer and wide receiver ',
        ' The Ravens became the third wildcard team to win the Super Bowl.',
        'The Oakland Raiders did it in 1981 and ',
        'The Baltimore Ravens have appeared in two Super Bowls and won both of them.',
        'Here are the results victories in bold Super Bowl XXXV 12801  Baltimore 34 New ',
        'the and'
        ]
    #collection = [
        #'The Oakland Raiders did it in 1981 and ',
        #]
    bm25_calc = BM25_calc(query, collection)
    ranked = bm25_calc.rank()