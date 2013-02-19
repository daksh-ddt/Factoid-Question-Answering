# -*- coding: utf-8 -*-
'''
7%
5 percent
3.90%
five percent
.45%

('seven', 'CD'), ('percent', 'NN')

'''
from __future__ import division
from collections import defaultdict
from math import ceil
import re


def extract(tokens, pos_tagged_documents, ranked_docs):
    '''
    '''
    numerals_regex = re.compile(r'^[0-9]+\.[0-9]+$')
    fraction_regex = re.compile(r'[0-9]+/[0-9]+')
    letters_regex = re.compile(r'[a-zA-Z ]+')
    int_regex = re.compile(r'[0-9]+')
    answer_freq = defaultdict(int)

    percent_surface_forms = ['%', 'percent']
    for doc in pos_tagged_documents:
        for index, (token, tag) in enumerate(doc):
            if tag == 'CD':
                print token
                if doc[i+1][0] in percent_surface_forms:
                    print token, '%'
                #if letters_regex.search(token) is not None:
                    #token = convert_to_numeral(token.lower())
                    #num = float(token)
                #elif fraction_regex.search(token) is not None:
                    #num = convert_fraction_to_numeral(token)
                #elif numerals_regex.search(token) is not None:
                    #num = float(token)
                    #num = round(num, 3)
                    #num = 'about ' + str(num)
                #elif int_regex.search(token) is not None:
                    #num = int(token)
                #else:
                    #print 'error on', token
                    #continue
                #answer_freq[num] += 1

    best_answer = sorted(
        answer_freq.items(), key=lambda x: x[1], reverse=True)[0][0]
    if str(best_answer).endswith('.0'):
        best_answer = int(best_answer)
    return best_answer




def convert_to_numeral(textnum, numwords={}):
    units = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen",
    ]
    tens = ["", "", "twenty", "thirty", "forty",
              "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales = ["hundred", "thousand", "million", "billion", "trillion"]

    numwords["and"] = (1, 0)
    for idx, word in enumerate(units):
        numwords[word] = (1, idx)
    for idx, word in enumerate(tens):
        numwords[word] = (1, idx * 10)
    for idx, word in enumerate(scales):
        numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current