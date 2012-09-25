# -*- coding: utf-8 -*-
"""
Create an interface to the Solr server
Created on Thu Jun 14 20:34:44 2012

@author: gavin
"""
import sunburnt

class SolrInterface(object):
    def __init__(self):
        solrAddressFile = open("solr_address.txt", "r")
        solrAddress = solrAddressFile.read()
        solrAddressFile.close()
        self.si = sunburnt.SolrInterface(solrAddress)

    def indexDocuments(self, documents):
        addedDocs = 0;
        for document in documents:
            try:
                self.si.add(document)
                addedDocs += 1
            except UnicodeDecodeError:
                print 'UnicodeDecodeError for %s' % document.text
            #self.si.commit()
        #self.si.commit()
        print 'Added %s of %s documents' % (addedDocs, len(documents))
        
    
    # delete documents when complete    
    def clearIndex(self):
        self.si.delete_all()
        self.si.commit()
        print 'Solr index has been cleared'
        
        
    def search(self, keywordsList):
        queryTermList = []
        for keyword in keywordsList:
            queryTermList.append('self.si.Q("%s")' % keyword)
        
        queryString = " | ".join(queryTermList)
        print queryString
        
        results = self.si.query(eval(queryString)).execute()
        return results
        
    # results = solrInterface.query((solrInterface.Q("13th") | solrInterface.Q("president") | solrInterface.Q("united") | solrInterface.Q("states"))
