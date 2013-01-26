# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 20:58:08 2012

@author: gavin
"""
from model import document


def create_documents(data, number_of_pages, filtered_keywords):
    descriptions = []
    for result in data['d']['results']:
        descriptions.append(result['Description'])

    documents = []
    counter = 0
    for description in descriptions:
        description.encode('ascii', 'ignore')
        documents.append(
            document.Document(
                text=description.decode('utf-8', 'ignore'), fine='', coarse='', id=str(counter)))
        counter += 1

    return filter_documents(documents, filtered_keywords)


def filter_documents(documents, filtered_keywords):
    filteredDocuments = []
    for document in documents:
        accept = False
        for term in filtered_keywords:
            if term in document.text:
                accept = True
        if accept:
            filteredDocuments.append(document)
            print document.text
    return filteredDocuments
