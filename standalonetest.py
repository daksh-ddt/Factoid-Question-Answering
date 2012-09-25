# -*- coding: utf-8 -*-
"""
Modified on Mon Sep 24 19:23:50 2012

@author: gavin hackeling
"""

import answertype
import querybuilder
import binginterface
import documentcreator
import documentfilter
import solrinterface
import alchemy

class StandAloneTest:
    def __init__(self):
        pass
    
    def runStandAloneTest(self, question):
        #question = ["who was the 13th president of the united states?"]
        #question = ["what is the capital of russia?"]
        question = [question]
        
        print "Question: %s\n" % question
        
        keywordsList = querybuilder.buildKeywordsList(question)
        print "Keywords: %s\n" % keywordsList
        
        query = querybuilder.buildQueryString(keywordsList)
        print "Query: %s\n" % query
        
        classifier = answertype.Classifier()
        answerType = classifier.classifyAnswerType(question)
        
        solr_interface = solrinterface.SolrInterface()
        solr_interface.clearIndex()
        
        data = binginterface.search("'" + query + "'")
        document_descriptions = documentcreator.getDescriptions(data, 20)
        documents = documentcreator.createDocumentsFromDescriptions(document_descriptions)
        
        filteredDocuments = documentfilter.filterDocuments(documents, keywordsList)    
        
        solr_interface.indexDocuments(filteredDocuments)
        #solr_interface.indexDocuments(documents)
        solr_interface.si.commit()
        
        results = solr_interface.search(keywordsList)
        
        print "%s results" % len(results)
        for result in results:
            print "Result: %s" % result['text']
            
        rankedAnswerCandidates = alchemy.parseEntities(results, answerType)
        for answer in rankedAnswerCandidates:
            print "Answer Candidate: %s" % answer[0]
        
        return rankedAnswerCandidates


if __name__ == "__main__":
    from sys import argv
    StandAloneTest().runStandAloneTest(argv)