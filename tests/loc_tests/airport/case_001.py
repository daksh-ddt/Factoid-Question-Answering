# -*- coding: utf-8 -*-
'''

'''
import json
import urllib
import simplejson
import simplejson
import unittest


class Test_pipeline(unittest.TestCase):

    def runTest(self):
        question = 'what is Bostons airport?'
        print 'Starting test'
        url = 'http://127.0.0.1:8003/f?q=%s' % question
        # req = urllib2.Request('http://ec2-50-17-103-0.compute-1.amazonaws.com:8009/')
        response = simplejson.load(urllib.urlopen(url))
        best_answer = response['best_answer'][0]
        all_answers = response['all_answers']
        print 'Best answer: %s' % best_answer
        print 'Other answers: %s' % all_answers
        self.assertEqual(best_answer.lower(), 'logan')

if __name__ == '__main__':
    unittest.main()
