# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 13:25:17 2012

@author: gavin hackeling
"""

from nltk import metrics
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from math import log, exp
from random import shuffle, randint, uniform
from copy import deepcopy

p = "No delegate finished the report"
h = "Some delegate finished the report on time"
pTokens = nltk.tokenize.word_tokenize(p)
p_postags = nltk.pos_tag(pTokens)
hTokens = nltk.tokenize.word_tokenize(h)
h_postags = nltk.pos_tag(hTokens)

costs = {}

# TODO: need to pass in pos tag after simplifying pos tag
# get the cost of aligning a token to another token
def getWordAlignmentCost(hToken, pToken):
    lemmatizer = WordNetLemmatizer();
    hLemma = lemmatizer.lemmatize(hToken, 'v')
    pLemma = lemmatizer.lemmatize(pToken, 'v')
    levenshtein_edit_distance = metrics.edit_distance(hLemma, pLemma)
    sim = 1 - (levenshtein_edit_distance / max(len(hLemma), len(pLemma)))
    if sim == 0:
        sim = 0.0000000000001
    cost = -log(sim)
    return cost
    
# get the minimum cost of aligning the hypothesis token to the premise
def getMinHTokenAlignmentCost(hToken):
    max_cost = 10
    costs = []
    for pToken in pTokens:
        costs.append(getWordAlignmentCost(hToken, pToken))
        print 'Cost of aligning %s to %s: %s' % (hToken, pToken, getWordAlignmentCost(hToken, pToken))
        
    costOfAligningToken = min(max_cost, min(costs))
    return costOfAligningToken
    
# get the alignment costs for the catesian product of all hypothesis
# and premise tokens. These are stored in a dictionary for lookup.
def getAllAlignmentCosts(hTokens, pTokens):
    costs = {}
    for hToken in hTokens:
        for pToken in pTokens:
            p_cost = getWordAlignmentCost(hToken, pToken)
            costs[(hToken, pToken)] = p_cost
    return costs
       
# get the cost for aligning two sequences of tokens
def getTotalAlignmentCost(hSequence, pTokens):
    alignment = zip(hSequence, pTokens)
    totalCost = 0.0
    for i in alignment:
        totalCost += costs[i]
    return totalCost
        
costs = getAllAlignmentCosts(hTokens, pTokens)

    
    
# approximate the hypothesis that can be aligned to
# the premise with the least cost 
def simulateAnnealing(h, p):
    '''
    Keyword arguments:
        h -- hypothesis text
        p -- premise text
    Returns: the lowest cost alignment of h and p
    '''
    pTokens = nltk.tokenize.word_tokenize(p)    
    hTokens = nltk.tokenize.word_tokenize(h)
    
    hSequence = hTokens
    lowestCost = float("inf")
    cost_previous = float("inf")
    temp_start = 10000
    temp = temp_start
    temp_end = 10
    coolingFactor = 0.99
    shuffle(hSequence)
    lowestCostAlignment = hSequence
    while temp > temp_end:
        positionA = randint(0, len(pTokens)-1)
        positionB = randint(0, len(pTokens)-1)
        hSequence[positionA], hSequence[positionB] = hSequence[positionB], hSequence[positionA]
        newCost = getTotalAlignmentCost(hSequence, pTokens)
        if newCost < lowestCost:
            lowestCostAlignment = deepcopy(hSequence)
            print '%s: %s' % (lowestCostAlignment, newCost)
            lowestCost = newCost
        difference = newCost - cost_previous
        prob = exp(-difference / temp)
        if difference < 0 or prob > uniform(0,1):
            cost_previous = newCost
        temp = temp * coolingFactor
    return (lowestCost, lowestCostAlignment)
    
    
    
    
    
### helper junk

def getDocumentsFromCorpus(corpus):
    documents = nltk.tokenize.sent_tokenize(corpus)
    return documents
    
def getDocumentsLength(documents):
    return len(documents)
    
def getTokenIDFWeightFromDocuments(token, length, documents):
    #num = max(0.00000001, len([document for document in documents if token.lower() in document.lower()]))
    num = len([document for document in documents if token.lower() in document.lower()])
    if num == 0:
        num = 10000
    idf_weight = log(length / num)
    print idf_weight
    return idf_weight











    

    
    
    