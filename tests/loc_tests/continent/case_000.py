# -*- coding: utf-8 -*-
'''

'''
import json
import urllib
import simplejson
import unittest


class Test_pipeline(unittest.TestCase):

    def runTest(self):
        question = 'which continent has the fewest people'
        print 'Starting test'
        url = 'http://127.0.0.1:8003/f?q=%s' % question
        response = simplejson.load(urllib.urlopen(url))
        best_answer = response['best_answer'][0]
        all_answers = response['all_answers']
        print 'Best answer: %s' % best_answer
        print 'Other answers: %s' % all_answers
        self.assertEqual(best_answer.lower(), 'antarctica')

if __name__ == '__main__':
    unittest.main()
