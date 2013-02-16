# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 20:58:08 2012

@author: gavin
"""
import bm25_ranker
from nltk import sent_tokenize
from nltk import pos_tag
from nltk import word_tokenize


def create_documents(data, filtered_keywords, tokens):
    documents = [result['Description'] for result in data]
    return filter_documents(documents, filtered_keywords, tokens)


def filter_documents(documents, filtered_keywords, tokens):
    sentences = []
    for d in documents:
        sentences.extend(sent_tokenize(d))
    sentences = [s for s in sentences if not s.endswith('?')]
    bm25_calc = bm25_ranker.BM25_calc(tokens, sentences)
    ranked_docs = bm25_calc.rank()
    tagged_docs = [pos_tag(word_tokenize(s)) for s in ranked_docs]
    return ranked_docs, tagged_docs