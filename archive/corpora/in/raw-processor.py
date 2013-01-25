# -*- coding: utf-8 -*-

import csv, sys, os

count = 16000
os.chdir('/home/gavin/dev/spyder-workspace/shallowQA/corpora/in')
# add to fine corpus
#os.chdir('/home/gavin/dev/spyder-workspace/shallowQA/corpora/data/fine')
# add to coarse corpus
curpath = os.path.abspath(os.curdir)

with open('/home/gavin/dev/spyder-workspace/shallowQA/corpora/in/PROCESS.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        category = os.path.join(curpath, row[0])
        if not os.path.exists(category):
            os.makedirs(category)
        question= row[1]
        try:
            file = open('/%s/%s.txt' % (category,  count),  'w')
            file.write(question)
            file.close()
        except Exception,  e:
            exception_name, exception_value = sys.exc_info()[:2]
            raise
        finally:
            count += 1
