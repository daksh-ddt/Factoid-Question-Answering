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
        question = ['who is the president of mexico?']
        predicted_coarse, predicted_fine = classifier.predict_answer_type(
            question)
        print predicted_coarse, predicted_fine
        self.assertEqual(predicted_fine, 'ind')

if __name__ == '__main__':
    unittest.main()