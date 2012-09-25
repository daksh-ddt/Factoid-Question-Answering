# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 20:12:33 2012

@author: gavin hackeling

"""

def filterDocuments(documents, query):
    filteredDocuments = []
    for document in documents:
        accept = False
        for term in query:
            # print "Checking %s for %s" % (document.text, term)
            if term in document.text:
                accept = True
        if accept == True:
            filteredDocuments.append(document)
    print "Accepted %s of %s documents" % (len(filteredDocuments), len(documents))
    return filteredDocuments
