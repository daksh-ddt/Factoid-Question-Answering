# -*- coding: utf-8 -*-

l = [1, 2, 3, 4, 7, 8, 9, 6]

a = [6, 4, 8]

contains_all = True
for token in a:
    if token not in l:
        contains_all = False

if contains_all:
    print 'yes'