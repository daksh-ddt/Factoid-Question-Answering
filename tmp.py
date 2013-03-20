# -*- coding: utf-8 -*-
import os
from nltk import word_tokenize

colors_file = os.path.join(os.path.dirname(__file__),
    'resources/gazetteer_colors.txt')
with open(colors_file) as f:
    colors = f.read().splitlines()

colors = [c.lower() for c in colors]
one_part_colors = [c for c in colors if c.count(' ')==0]

two_part_colors = [c for c in colors if c.count(' ')==1]
two_part_1of2 = [c.split(' ')[0] for c in two_part_colors]

three_part_colors = [c for c in colors if c.count(' ')==2]
three_part_1of3 = [c.split(' ')[0] for c in three_part_colors]

four_part_colors = [c for c in colors if c.count(' ')==3]
four_part_1of4 = [c.split(' ')[0] for c in four_part_colors]


s = "the University of California Gold and black dog went out to the warm".lower()
tokens = word_tokenize(s)

for index, token in enumerate(tokens):
    if token in one_part_colors:
        print 'found', token
    elif token in two_part_1of2:
        try:
            if (' '.join([token, tokens[index+1]])) in two_part_colors:
                print 'found', ' '.join([token, tokens[index+1]])
        except IndexError:
            print 'IndexError'
    elif token in three_part_1of3:
        try:
            full_color = (' '.join([token, tokens[index+1],tokens[index+2]]))
            if full_color in three_part_colors:
                print 'found', full_color
        except IndexError:
            print 'IndexError'
    elif token in four_part_1of4:
        print token
        try:
            full_color = (' '.join([token, tokens[index+1],tokens[index+2],
                tokens[index+3]]))
            if full_color in four_part_colors:
                print 'found', full_color
        except IndexError:
            print 'IndexError'