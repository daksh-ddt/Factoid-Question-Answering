# -*- coding: utf-8 -*-
'''

'''
import json
import urllib2
import unittest


class Test_pipeline(unittest.TestCase):

    def runTest(self):
        question = 'what country is ottawa in'
        print 'Starting test'
        d = {"question": "[%s]" % question}
        req = urllib2.Request('http://ec2-50-17-103-0.compute-1.amazonaws.com:8009/')
        req.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(req, json.dumps(d)).read()
        response = json.loads(response)
        best_answer = response['best_answer']
        all_answers = response['all_answers']
        print 'Best answer: %s' % best_answer
        print 'Other answers: %s' % all_answers
        self.assertEqual(best_answer.lower(), 'canada')

if __name__ == '__main__':
    unittest.main()