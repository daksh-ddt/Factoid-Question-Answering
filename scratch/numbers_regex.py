# -*- coding: utf-8 -*-
import re

[m.start() for m in re.finditer('test', 'test test test test')]

s = 'hello world, this is the number 671 and then this is 212.87'




# find ints
r = r'\d+'

#find real numbers
d = r'\d+\.*\d*'

# 56%
# 55 percent



print re.findall(r,s)


# for numbers, first should convert all words to numerals
# convert all other words to symbols
# percent, percentage -> %
# dollars -> $
# # -*- coding: utf-8 -*-

