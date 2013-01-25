import os
import nltk
os.chdir('/home/gavin/Documents/dev/ie/corpora/data/coarse/')
file = open('train_5500.label')
doc = []
curpath = os.path.abspath(os.curdir)

while 1:
    line = file.readline()
    doc.append(line)
    if not line:
        break
    pass
    
count = 0

# need some exception handling

for line in doc:
    tokens = nltk.word_tokenize(line)
    category = os.path.join(curpath, tokens[0])
    if not os.path.exists(category):
        os.makedirs(category)
    string = ' '.join(tokens[3:])
    try:
        file = open('/%s/%s.txt' % (category,  count),  'w')
        file.write(string)
        file.close()
    except Exception,  e:
        exception_name, exception_value = sys.exc_info()[:2]
        raise
    finally:
        count += 1
    
    
