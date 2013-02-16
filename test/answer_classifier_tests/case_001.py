# -*- coding: utf-8 -*-
'''

'''
import unittest
import sys
sys.path.append('/home/gavin/dev/Factoid-Question-Answering')
import answer_classifier


class Test_pipeline(unittest.TestCase):

    def runTest(self):
        classifier = answer_classifier.Answer_classifier()
        question = ['who makes the surface pro?']
        predicted_coarse, predicted_fine = classifier.predict_answer_type(
            question)
        print predicted_coarse, predicted_fine
        self.assertEqual(predicted_fine, 'gr')

if __name__ == '__main__':
    unittest.main()