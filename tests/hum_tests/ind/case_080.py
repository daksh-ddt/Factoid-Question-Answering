# -*- coding: utf-8 -*-
'''

'''
import json
import urllib2
import unittest


class Test_pipeline(unittest.TestCase):

    def runTest(self):
        question = 'who is nicknamed the black falcon?'
        print 'Starting test'
        d = {"question": "[%s]" % question}
        req = urllib2.Request('http://ec2-50-17-103-0.compute-1.amazonaws.com:8009/')
        # req = urllib2.Request('http://127.0.0.1:8009/')
        req.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(req, json.dumps(d)).read()
        response = json.loads(response)
        best_answer = response['best_answer']
        print 'Best answer: %s' % best_answer
        self.assertEqual(best_answer.lower(), 'harrison barnes')

if __name__ == '__main__':
    unittest.main()