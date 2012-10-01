import os
import nltk
os.chdir('/home/gavin/Documents/dev/ie/corpora/')
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

for line in doc:
    tokens = nltk.word_tokenize(line)
    coarse_category_path = os.path.join(curpath, tokens[0])
    fine_category = tokens[2]
    fine_category_path = os.path.join(coarse_category_path,  fine_category)
    if not os.path.exists(coarse_category_path):
        os.makedirs(coarse_category_path)
    if not os.path.exists(fine_category_path):
        os.makedirs(fine_category_path)
    string = ' '.join(tokens[3:])
    try:
        file = open('/%s/%s/%s.txt' % (coarse_category_path,  fine_category,  count),  'w')
        file.write(string)
        file.close()
    except Exception,  e:
        exception_name, exception_value = sys.exc_info()[:2]
        raise
    finally:
        count += 1
    
    
