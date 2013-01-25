# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 20:58:08 2012

@author: gavin
"""
import urllib2
import nltk.tokenize.punkt
import deHtmlParser
from model import document

# set user-agent for requests
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]


def createDocuments(data, number_of_pages):
    counter = 0;
    tmpCounter = 0;
    documents = []
    for result in data['d']['results']:
        if tmpCounter < number_of_pages:
            try:
                infile = opener.open(result['Url'])
                page = infile.read()
                resultText = deHtmlParser.dehtml(page)
                for sent in nltk.tokenize.sent_tokenize(resultText):
                    documents.append(document.Document(text=sent, fine='', coarse='', id=str(counter)))
                    counter += 1
            except Exception:
                print 'Error retrieving document'
            tmpCounter+=1
    return documents


def getDescriptions(data, number_of_pages):
    descriptions = []
    for result in data['d']['results']:
        descriptions.append(result['Description'])
    return descriptions

def createDocumentsFromDescriptions(descriptions):
    documents = []
    counter = 0
    for description in descriptions:
        # for sent in nltk.tokenize.sent_tokenize(description)
        documents.append(document.Document(text=description, fine='', coarse='', id=str(counter)))
        counter += 1
    return documents
