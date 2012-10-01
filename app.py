# -*- coding: utf-8 -*-
"""
ShallowQA v0.5 Alder

Modified on Mon Sep 24 19:23:50 2012

@author: gavin hackeling

"""
import os
import logging

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

class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("about.html")
        
class ContactHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("contact.html")
        
class CleverHansHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("qa_get.html")
    
    def post(self):
        #logging.basicConfig(filename='%s/typed_questions.log' % options.apphome,level=logging.DEBUG)
#        logging.basicConfig(filename='typed_questions.log',
#                            filemode='a',
#                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
#                            datefmt='%H:%M:%S',
#                            level=logging.DEBUG)
      
        print options.apphome
        question = [self.get_argument("question")]
        print question
        
        keywordsList = querybuilder.buildKeywordsList(question, options.apphome)
        print keywordsList
        query = querybuilder.buildQueryString(keywordsList)
        print query
        
        classifier = answertype.Classifier(options.apphome)
        answerType = classifier.classifyAnswerType(question)
        #logging.info('%s    %s' % (answerType, question))     
        #self.logger = logging.getLogger('urbanGUI') 
        
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
            print "Answer Candidate: %s" % answer[0].encode('ascii', 'replace')
            rankedAnswerCandidatesList.append(answer[0])
            
        self.render("qa_post.html", question=question[0], answers=rankedAnswerCandidatesList)
        
handlers = [
            (r"/", CleverHansHandler), 
            (r"/cleverhans",  CleverHansHandler),
            (r"/about", AboutHandler),
            (r"/contact", ContactHandler) 
            ]
            
settings = dict(template_path=os.path.join(os.path.dirname(__file__), "templates"))
application = tornado.web.Application(handlers, **settings)
define("port", default=8000, help="run on the given port", type=int)
define("apphome", default="/home/ubuntu/www", help="the path to the application folder", type=str)
    
if __name__ == "__main__":
    #tornado.options.options['log_prefix'].set('%s/shallowQA.log%s' % (options.apphome))
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

    