# -*- coding: utf-8 -*-
'''

'''
import json
import urllib2
import unittest


class Test_pipeline(unittest.TestCase):

    def runTest(self):
        question = 'who invented coca cola?'
        print 'Starting test'
        d = {"question": "[%s]" % question}
        req = urllib2.Request('http://ec2-50-17-103-0.compute-1.amazonaws.com:8009/')
        req.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(req, json.dumps(d)).read()
        response = json.loads(response)
        best_answer = response['best_answer']
        print 'Best answer: %s' % best_answer
        self.assertTrue(best_answer.lower() in [
            'doctor john pemberton','john pemberton'])

if __name__ == '__main__':
    unittest.main()