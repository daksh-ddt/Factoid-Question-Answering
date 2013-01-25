# -*- coding: utf-8 *-*
'''

'''


class Answer:
    def __init__(self, question):
        self.predicted_coarse = None
        self.predicted_fine = None
        self.best_answer = None
        self.all_answers = None
        self.query = None
        self.question = question
