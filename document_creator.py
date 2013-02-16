# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 20:58:08 2012

@author: gavin
"""


def create_documents(data, filtered_keywords):
    documents = []
    for result in data['d']['results']:
        print type(result['Description'])
        documents.append(result['Description'].encode('ascii', 'ignore'))

    return filter_documents(documents, filtered_keywords)


def filter_documents(documents, filtered_keywords):
    filteredDocuments = []
    for document in documents:
        accept = False
        for term in filtered_keywords:
            if term in document:
                accept = True
        if accept:
            filteredDocuments.append(document)
    return filteredDocuments
