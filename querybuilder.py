# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 19:23:50 2012

@author: gavin
"""
#import os
#import unicodedata
import nltk.tokenize.punkt;

def buildKeywordsList(question, apphome):
    # encode unicode input as str
    question = question[0].encode('ascii', 'ignore')
    #keywordsList = nltk.word_tokenize(question[0])
    keywordsList = nltk.wordpunct_tokenize(question)
    # Filter keywords
    # prepend +- to force inclusion/exclusion in search
    #os.chdir('/home/ubuntu/app')
    # Load the stop word list
    stopListFile = open("%s/static/stopwords/english.txt" % apphome, "r")
    #stopListFile = open("/home/ubuntu/www/static/stopwords/english.txt", "r")
    stopList = [line.strip() for line in stopListFile.readlines()]
    stopListFile.close()
    # Filter non-alphanumeric characters from the query
    keywordsList = [filter(str.isalnum, token).lower() for token in keywordsList]
    
    # Filter empty tokens from the query
    keywordsList = [token for token in keywordsList if len(token) > 0]
    # Filter stop list words from the query
    keywordsList = [token for token in keywordsList if token not in stopList]
    return keywordsList
    
    

def buildQueryString(keywordsList):
    return " ".join(keywordsList)