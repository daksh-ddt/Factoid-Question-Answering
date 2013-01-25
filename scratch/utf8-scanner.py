# -*- coding: utf-8 -*-

import os

directory = '/home/gavin/dev/spyder-workspace/shallowQA/corpora/data/coarse/NUM/'

print 'sacnning'
for root, dirs, files in os.walk(directory):
    for file in files:
        print file
        content = open(directory + file).read()
        try:
            content.encode('ascii')
        except UnicodeDecodeError:
            print "%s contains non-ascii characters" % file
print '\ncomplete'