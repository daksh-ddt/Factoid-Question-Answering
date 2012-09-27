# -*- coding: utf-8 -*-
"""
QA - Alder

Modified on Mon Sep 24 19:23:50 2012

@author: gavin hackeling

# check if query contains ne.
# if so, need to include as literal in query

# check if keyword is an NE type
# if so, need to expand search to include instances of NE type
# newspaper could be NE type
# need to include keywords that are names of newspapers

# need to store keywords as list initially
# so that candidate answers can be compared against the keywords
# and candidate answers that match a keyword can be exluded

# need to include alchemyapi concept tags
# paragraph tokenize instead of sent tokenize

# test if it is faster to filter documents before adding to solr

# need to work on query expansion ('temperature' -> 'degrees')

# need to selectively apply alchemyAPI. cannot detect dates so no need to apply
# for 'date' questions. apply alchemy for concept identification instead?
# (-) alchemy concept identification of dates is poor

# need to find or make rules for identifying dates

"""
import os

import answertype
import querybuilder
import binginterface
import documentcreator
import documentfilter
import solrinterface
import alchemy

import tornado.web, tornado.ioloop
from tornado.options import define, options

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("home_get.html")
        
class CleverHansHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("qa_get.html")
    
    def post(self):
        print options.apphome
        question = [self.get_argument("question")]
        print question
        
        keywordsList = querybuilder.buildKeywordsList(question, options.apphome)
        print keywordsList
        query = querybuilder.buildQueryString(keywordsList)
        print query
        
        classifier = answertype.Classifier(options.apphome)
        answerType = classifier.classifyAnswerType(question)
        
        solr_interface = solrinterface.SolrInterface(options.apphome)
        solr_interface.clearIndex()
        
        data = binginterface.search("'" + query + "'")
        document_descriptions = documentcreator.getDescriptions(data, 50)
        documents = documentcreator.createDocumentsFromDescriptions(document_descriptions)
        filteredDocuments = documentfilter.filterDocuments(documents, keywordsList)
        
        solr_interface.indexDocuments(filteredDocuments)
        solr_interface.si.commit()

        results = solr_interface.search(keywordsList)

        print "%s results" % len(results)
        for result in results:
            print 'Result: %s' % result['text'].encode('ascii', 'replace')
            
        rankedAnswerCandidates = alchemy.parseEntities(results, answerType, options.apphome)    
        
        rankedAnswerCandidatesList = []
        for answer in rankedAnswerCandidates:
            print "Answer Candidate: %s" % answer[0]
            rankedAnswerCandidatesList.append(answer[0])
            
        self.render("qa_post.html", question=question[0], answers=rankedAnswerCandidatesList)
        
handlers = [
            (r"/", MainHandler), 
            (r"/cleverhans",  CleverHansHandler), 
            ]
            
settings = dict(template_path=os.path.join(os.path.dirname(__file__), "templates"))
application = tornado.web.Application(handlers, **settings)
define("port", default=8000, help="run on the given port", type=int)
define("apphome", default="/home/ubuntu/www", help="the path to the application folder", type=str)
    
if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

    